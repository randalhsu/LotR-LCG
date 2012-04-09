import sys
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from Messaging import *
from xxxxGameDialog import *


class HostGameDialog(xxxxGameDialog):
    # Host game as a TCP server. It also has a Client connected to localhost, join as a TCP client, in order to unify messaging
    
    def __init__(self, parent=None):
        super(HostGameDialog, self).__init__(parent)
        self.server = Server(self)
        self.createUI()
        
    def hostGame(self):
        if not self.validateNickname():
            return
            
        if not self.ipList.currentItem():
            QMessageBox.critical(self, self.tr('IP Address?'), self.tr('Please select an IP address'))
            return
            
        specificPort = 0
        if self.portSpinBox.isEnabled():
            specificPort = self.portSpinBox.value()
        port = self.server.hostGame(specificPort)
        if port == -1:
            QMessageBox.critical(self, self.tr('Networking Failed'), self.tr('Unable to host game...'))
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
        self.chatter.appendSystemMessage(self.tr('Waiting for other players...'))
        
    def connectToSelf(self, port):
        localhost = str(QHostAddress(QHostAddress.LocalHost).toString())
        nickname = str(self.nickLineEdit.text())
        self.client = Client(nickname, localhost, port, self)
        
    def clientSocketConnected(self):
        self.chatter.setSocket(self.client)
        self.topWidget.setEnabled(False)
        self.startButton.setDefault(True)
        
    def createUI(self):
        nickLabel = QLabel(self.tr('Your &nickname:'))
        nickLabel.setBuddy(self.nickLineEdit)
        self.nickLineEdit.selectAll()
        
        selectIPLabel = QLabel(self.tr('Select an IP address:'))
        self.ipList = QListWidget()
        
        for address in QNetworkInterface.allAddresses():
            if address.protocol() == QAbstractSocket.IPv4Protocol:
                ip = str(address.toString())
                self.ipList.addItem(ip)
        if self.ipList.count() > 1:
            self.ipList.setCurrentRow(0)
            
        selectPortLabel = QLabel(self.tr('Select a port:'))
        autoPortButton = QRadioButton(self.tr('Auto'))
        autoPortButton.setChecked(True)
        self.portSpinBox = QSpinBox()
        self.portSpinBox.setRange(0, 65535)
        self.portSpinBox.setValue(5566)
        self.portSpinBox.setEnabled(False)
        specificPortButton = QRadioButton(self.tr('Specific:'))
        specificPortButton.toggled.connect(self.portSpinBox.setEnabled)
        
        self.hostButton = QPushButton(self.tr('&Host Game!'))
        self.hostButton.clicked.connect(self.hostGame)
        
        hostingLabel = QLabel(self.tr('Hosting game at'))
        self.hostingLineEdit = QLineEdit()
        self.startButton = QPushButton(self.tr('&Start Game!'))
        self.startButton.clicked.connect(self.server.startGame)
        
        nicknameLayout = QHBoxLayout()
        nicknameLayout.addWidget(nickLabel)
        nicknameLayout.addWidget(self.nickLineEdit)
        portLayout = QHBoxLayout()
        portLayout.addWidget(selectPortLabel)
        portLayout.addWidget(autoPortButton)
        portLayout.addWidget(specificPortButton)
        portLayout.addWidget(self.portSpinBox)
        
        topLayout = QVBoxLayout()
        topLayout.addLayout(nicknameLayout)
        topLayout.addWidget(selectIPLabel)
        topLayout.addWidget(self.ipList)
        topLayout.addLayout(portLayout)
        topLayout.addWidget(self.hostButton)
        self.topWidget = QWidget()
        self.topWidget.setLayout(topLayout)
        
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
        layout.addWidget(self.topWidget)
        layout.addWidget(self.bottomWidget)
        self.setLayout(layout)
        self.setWindowTitle(self.tr('Host Multiplayer Game'))
        self.hostButton.setDefault(True)
        self.restoreGeometry()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = HostGameDialog()
    dialog.show()
    sys.exit(app.exec_())