'''
TODO: unicode chatting
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Chatter(QWidget):
    def __init__(self, parent):
        super(Chatter, self).__init__(parent)
        self.parent = parent
        self.socket = None
        self.createUI()
        
    def setSocket(self, socket):
        self.socket = socket
        
    def appendMessage(self, message):
        self.textBrowser.append(message)
        
    def appendSystemMessage(self, message):
        self.textBrowser.setFontWeight(QFont.Bold)
        self.textBrowser.append(message)
        self.textBrowser.setFontWeight(QFont.Normal)
        
    def send(self):
        if self.socket is None:
            QMessageBox.critical(self.parent, 'Not Connected', 'Not connected to server...')
            return
            
        message = str(self.messageLineEdit.text())
        self.socket.sendChatMessage(message)
        self.messageLineEdit.clear()
        
    def createUI(self):
        self.textBrowser = QTextBrowser()
        self.messageLineEdit = QLineEdit()
        sendButton = QPushButton(self.tr('&Send'))
        sendButton.clicked.connect(self.send)
        self.messageLineEdit.returnPressed.connect(self.send)
        
        layout = QGridLayout()
        layout.addWidget(self.textBrowser, 0, 0, 4, 4)
        layout.addWidget(self.messageLineEdit, 4, 0, 1, 3)
        layout.addWidget(sendButton, 4, 3, 1, 1)
        self.setLayout(layout)