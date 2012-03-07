from MainWindow import MainWindow
from SetupDialog import *


class MultiplayerMainWindow(MainWindow):
    def __init__(self, server, client, chatter, parent=None):
        self.isServer = False if server is None else True
        self.server = server
        self.client = client
        self.chatter = chatter
        
        if server:
            server.setParent(self)
        client.setParent(self)
        
        super(MultiplayerMainWindow, self).__init__(parent)
        
        title = str(self.windowTitle())
        if self.isServer:
            title += ' (Server)'
        else:
            title += ' (Client)'
        self.setWindowTitle(title)
        
    def startNewGame(self):
        self.cleanup()
        setupDialog = None
        if self.isServer:
            setupDialog = SetupDialog(self)
            setupDialog.startButton.setText(self.tr('Ready!'))
            setupDialog.exec_()
            self.scenarioId = setupDialog.selectedScenarioId()
            self.playerDeckId = setupDialog.selectedDeckId()
        else:
            setupDialog = ClientSetupDialog(self)
            setupDialog.exec_()
        
        data = 'CLIENT:READY\n'
        self.client.sendData(data)
        #self.setup()
        
    def clientSocketConnected(self):
        pass
        
    def clientSocketDisconnected(self):
        pass
        