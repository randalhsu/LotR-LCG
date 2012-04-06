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
        
    def setFocus(self):
        self.messageLineEdit.setFocus(Qt.PopupFocusReason)
        
    def appendMessage(self, message):
        self.textBrowser.append(message)
        
    def appendSystemMessage(self, message):
        self.textBrowser.append(QString('<tt><b>%1</b></tt>').arg(message))
        
    def send(self):
        if self.socket is None:
            QMessageBox.critical(self.parent, self.tr('Not Connected'), self.tr('Not connected to server...'))
            return
            
        message = self.messageLineEdit.text().toUtf8()
        self.socket.sendChatMessage(message)
        self.messageLineEdit.clear()
        
    def createUI(self):
        self.textBrowser = QTextBrowser()
        self.messageLineEdit = QLineEdit()
        self.messageLineEdit.returnPressed.connect(self.send)
        
        layout = QGridLayout()
        layout.addWidget(self.textBrowser, 0, 0, 5, 5)
        layout.addWidget(self.messageLineEdit, 5, 0, 1, 5)
        self.setLayout(layout)
        self.appendSystemMessage(self.tr('Type in and press Enter to send message.'))