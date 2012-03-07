import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from Chatter import Chatter
from Messaging import Client
from MultiplayerMainWindow import *
from xxxxGameDialog import *


class JoinGameDialog(xxxxGameDialog):
    # Join game as a TCP client
    
    def __init__(self, parent=None):
        super(JoinGameDialog, self).__init__(parent)
        self.createUI()
        
    def connectToServer(self):
        if self.nickLineEdit.text().isEmpty():
            QMessageBox.critical(self, 'Nickname?', 'Please give a nickname...')
            self.nickLineEdit.setFocus()
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
            QMessageBox.critical(self, 'Address?', 'Invalid address...')
            self.addressLineEdit.setFocus()
            return
            
        nickname = str(self.nickLineEdit.text())
        (host, port) = address.split(':')
        self.client = Client(nickname, host, port, self)
        
    def clientSocketConnected(self):
        self.chatter.setEnabled(True)
        self.chatter.setSocket(self.client)
        self.joinButton.setEnabled(False)
        
    def createUI(self):
        username = QDir.homePath().split('/')[-1]
        nickLabel = QLabel(self.tr('Your &nickname:'))
        self.nickLineEdit = QLineEdit(username)
        self.nickLineEdit.setValidator(QRegExpValidator(QRegExp(r'[A-Za-z0-9_\-]{1,10}')))
        nickLabel.setBuddy(self.nickLineEdit)
        
        addressLabel = QLabel(self.tr('Server address (IP:port):'))
        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.selectAll()
        
        self.joinButton = QPushButton('&Join Game!')
        self.joinButton.clicked.connect(self.connectToServer)
        
        #self.chatter = Chatter(self)
        self.chatter.setEnabled(False)
        
        topLayout = QGridLayout()
        topLayout.addWidget(nickLabel, 0, 0, 1, 1)
        topLayout.addWidget(self.nickLineEdit, 0, 1, 1, 1)
        topLayout.addWidget(addressLabel, 1, 0, 1, 1)
        topLayout.addWidget(self.addressLineEdit, 1, 1, 1, 1)
        topLayout.addWidget(self.joinButton, 2, 0, 1, 2)
        
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(self.chatter)
        
        self.setLayout(layout)
        self.setWindowTitle(self.tr('Join Multiplayer Game'))
        self.addressLineEdit.setFocus()
        self.joinButton.setDefault(True)


if __name__ == '__main__':
     app = QApplication(sys.argv)
     dialog = JoinGameDialog()
     dialog.show()
     sys.exit(app.exec_())