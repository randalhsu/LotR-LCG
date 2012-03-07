import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from Chatter import Chatter
from Messaging import *
from MultiplayerMainWindow import *
from xxxxGameDialog import *


class HostGameDialog(xxxxGameDialog):
    # Host game as a TCP server. It also has a Client connected to localhost, join as a TCP client, in order to unify messaging
    
    def __init__(self, parent=None):
        super(HostGameDialog, self).__init__(parent)
        self.server = Server(self)
        self.createUI()
        
    def hostGame(self):
        if self.nickLineEdit.text().isEmpty():
            QMessageBox.critical(self, 'Nickname?', 'Please give a nickname...')
            self.nickLineEdit.setFocus()
            return
            
        if not self.ipList.currentItem():
            QMessageBox.critical(self, 'IP?', 'Please select an IP...')
            return
            
        port = self.server.hostGame()
        if port == -1:
            QMessageBox.critical(self, 'Networking Failed', 'Unable to host game...')
            return
            
        ip = self.ipList.currentItem().text()
        port = str(port)
        self.hostingLineEdit.setText('{0}:{1}'.format(ip, port))
        self.bottomWidget.setEnabled(True)
        self.hostingLineEdit.selectAll()
        self.hostingLineEdit.setFocus()
        
        self.connectToSelf(port)
        QTimer.singleShot(100, self.appendWaitingMessage)
        
    def appendWaitingMessage(self):
        self.chatter.appendSystemMessage('Waiting for other players...')
        
    def connectToSelf(self, port):
        localhost = str(QHostAddress(QHostAddress.LocalHost).toString())
        nickname = str(self.nickLineEdit.text())
        self.client = Client(nickname, localhost, port, self)
        
    def clientSocketConnected(self):
        self.chatter.setSocket(self.client)
        self.hostButton.setEnabled(False)
        self.startButton.setDefault(True)
        
    def startGame(self):
        self.server.startGame()
        
    def createUI(self):
        username = QDir.homePath().split('/')[-1]
        nickLabel = QLabel(self.tr('Your &nickname:'))
        self.nickLineEdit = QLineEdit(username)
        self.nickLineEdit.setValidator(QRegExpValidator(QRegExp(r'[A-Za-z0-9_\-]{1,10}')))
        self.nickLineEdit.selectAll()
        nickLabel.setBuddy(self.nickLineEdit)
        
        selectLabel = QLabel(self.tr('Select an IP to host game:'))
        self.ipList = QListWidget()
        
        def isValidIP(ip):
            unusefuls = ['10.', '169.254.', '192.168.']
            for classC in range(16, 32):
                unusefuls.append('172.{0}.'.format(classC))
                
            for unuseful in unusefuls:
                if ip.startswith(unuseful):
                    return False
            return True
        
        for address in QNetworkInterface.allAddresses():
            if address.protocol() == QAbstractSocket.IPv4Protocol:
                ip = str(address.toString())
                if isValidIP(ip):
                    self.ipList.addItem(ip)
        if self.ipList.count() > 1:
            self.ipList.setCurrentRow(0)
            
        self.hostButton = QPushButton(self.tr('&Host Game!'))
        self.hostButton.clicked.connect(self.hostGame)
        
        hostingLabel = QLabel(self.tr('Hosting game at'))
        self.hostingLineEdit = QLineEdit()
        #self.chatter = Chatter(self)
        self.startButton = QPushButton(self.tr('&Start Game!'))
        self.startButton.clicked.connect(self.startGame)
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(nickLabel)
        topLayout.addWidget(self.nickLineEdit)
        
        littleLayout = QHBoxLayout()
        littleLayout.addWidget(hostingLabel)
        littleLayout.addWidget(self.hostingLineEdit)
        
        bottomLayout = QVBoxLayout()
        bottomLayout.addLayout(littleLayout)
        bottomLayout.addWidget(self.chatter)
        bottomLayout.addWidget(self.startButton)
        self.bottomWidget = QWidget()
        self.bottomWidget.setLayout(bottomLayout)
        self.bottomWidget.setEnabled(False)
        
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(selectLabel)
        layout.addWidget(self.ipList)
        layout.addWidget(self.hostButton)
        layout.addWidget(self.bottomWidget)
        self.setLayout(layout)
        self.setWindowTitle(self.tr('Host Multiplayer Game'))
        self.hostButton.setDefault(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = HostGameDialog()
    dialog.show()
    sys.exit(app.exec_())