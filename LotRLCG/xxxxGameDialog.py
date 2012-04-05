from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from Chatter import Chatter
from MultiplayerMainWindow import *


mainWindows = []


class xxxxGameDialog(QWidget):
    def __init__(self, parent=None):
        super(xxxxGameDialog, self).__init__(parent)
        
        self.chatter = Chatter(self)
        self.client = None
        self.isManuallyClosing = True
        self.setWindowIcon(QIcon(':/images/icons/LotRLCG_MP.ico'))
        
        self.nicknameRegExp = QRegExp(r'[A-Za-z0-9_\-]{1,10}')
        username = QDir.homePath().split('/')[-1]
        nickname = username if self.nicknameRegExp.exactMatch(username) else ''
        self.nickLineEdit = QLineEdit(nickname)
        self.nickLineEdit.setValidator(QRegExpValidator(self.nicknameRegExp))
        
    def appendMessage(self, message):
        self.chatter.appendMessage(message)
        
    def appendSystemMessage(self, message):
        self.chatter.appendSystemMessage(message)
        
    def validateNickname(self):
        nickname = self.nickLineEdit.text()
        if nickname.isEmpty():
            QMessageBox.critical(self, self.tr('Nickname?'), self.tr('Please give a nickname!'))
            self.nickLineEdit.setFocus()
            return False
            
        if not self.nicknameRegExp.exactMatch(nickname):
            QMessageBox.critical(self, self.tr('Nickname?'), self.tr('Valid characters: A-Z, a-z, 0-9, dash, underscore'))
            self.nickLineEdit.setFocus()
            return False
            
        return True
        
    def clientSocketConnected(self):
        raise NotImplementedError
        
    def initializeMainWindow(self):
        className = self.__class__.__name__
        server = self.server if className == 'HostGameDialog' else None
        
        self.isManuallyClosing = False
        self.close()
        
        global mainWindows
        mainWindow = MultiplayerMainWindow(server, self.client, self.chatter)
        mainWindow.show()
        mainWindows.append(mainWindow)  # make it survive after this method ends...
        
    def closeEvent(self, event):
        className = self.__class__.__name__
        if self.isManuallyClosing:
            if self.client is not None:
                self.client.disconnectFromHost()
            if className == 'HostGameDialog':
                self.server.farewell()
        event.accept()