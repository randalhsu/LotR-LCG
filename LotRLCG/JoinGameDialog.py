import sys
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from Messaging import Client
from xxxxGameDialog import *


class JoinGameDialog(xxxxGameDialog):
    # Join game as a TCP client
    
    TIMEOUT = 5000  # milliseconds timeout before considered connecting failed
    
    def __init__(self, parent=None):
        super(JoinGameDialog, self).__init__(parent)
        self.createUI()
        
    def connectToServer(self):
        if not self.validateNickname():
            return
            
        def validateAddress(address):
            try:
                (ip, port) = address.split(':')
                bytes = ip.split('.')
                if len(bytes) != 4:
                    return False
                for number in bytes:
                    if not number.isdigit():
                        return False
                    if not (0 <= int(number, 10) <= 255):
                        return False
                if not port.isdigit():
                    return False
            except:
                return False
            return True
            
        address = str(self.addressLineEdit.text()).strip()
        if not validateAddress(address):
            QMessageBox.critical(self, self.tr('Address?'), QString('%1<br>%2 <b>140.116.39.240:57258</b>').arg(self.tr('Invalid address!')).arg(self.tr('Example address:')))
            self.addressLineEdit.setFocus()
            return
            
        nickname = str(self.nickLineEdit.text())
        (host, port) = address.split(':')
        self.client = Client(nickname, host, port, self)
        
        self.joinButton.setText(self.tr('Connecting to server...'))
        self.joinButton.setEnabled(False)
        
        QTimer.singleShot(JoinGameDialog.TIMEOUT, self.checkIfConnectedToServer)
        
    def checkIfConnectedToServer(self):
        if self.client.state() != QAbstractSocket.ConnectedState:
            self.client.abort()
            QMessageBox.critical(self, self.tr('Connection Timeout'), QString('%1<br>%2').arg(self.tr('Cannot connect to server!')).arg(self.tr('(Wrong address maybe?)')))
            self.joinButton.setText(self.tr('&Join Game!'))
            self.joinButton.setEnabled(True)
            
    def clientSocketConnected(self):
        self.topWidget.setEnabled(False)
        self.joinButton.setText(self.tr('Connected to server!'))
        self.chatter.setEnabled(True)
        self.chatter.setSocket(self.client)
        self.chatter.setFocus()
        self.waitingLabel.setText(self.tr('Waiting for server to start game...'))
        
    def createUI(self):
        nickLabel = QLabel(self.tr('Your &nickname:'))
        nickLabel.setBuddy(self.nickLineEdit)
        
        addressLabel = QLabel(self.tr('Server address (IP:port):'))
        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.selectAll()
        self.addressLineEdit.returnPressed.connect(self.connectToServer)
        
        self.joinButton = QPushButton(self.tr('&Join Game!'))
        self.joinButton.clicked.connect(self.connectToServer)
        
        self.chatter.setEnabled(False)
        self.waitingLabel = QLabel()
        
        topLayout = QGridLayout()
        topLayout.addWidget(nickLabel, 0, 0, 1, 1)
        topLayout.addWidget(self.nickLineEdit, 0, 1, 1, 1)
        topLayout.addWidget(addressLabel, 1, 0, 1, 1)
        topLayout.addWidget(self.addressLineEdit, 1, 1, 1, 1)
        topLayout.addWidget(self.joinButton, 2, 0, 1, 2)
        self.topWidget = QWidget()
        self.topWidget.setLayout(topLayout)
        
        layout = QVBoxLayout()
        layout.addWidget(self.topWidget)
        layout.addWidget(self.chatter)
        layout.addWidget(self.waitingLabel)
        
        self.setLayout(layout)
        self.setWindowTitle(self.tr('Join Multiplayer Game'))
        self.addressLineEdit.setFocus()
        self.joinButton.setDefault(True)
        self.restoreGeometry()


if __name__ == '__main__':
     app = QApplication(sys.argv)
     dialog = JoinGameDialog()
     dialog.show()
     sys.exit(app.exec_())