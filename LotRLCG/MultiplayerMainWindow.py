import json
from MainWindow import MainWindow
from SetupDialog import *


class MultiplayerMainWindow(MainWindow):
    INTERVAL = 500  # milliseconds interval to check Area-states change and sync between clients
    
    def __init__(self, server, client, chatter, parent=None):
        self.isServer = False if server is None else True
        self.server = server
        self.client = client
        self.chatter = chatter
        
        if server:
            server.setParent(self)
        client.setParent(self)
        
        super(MultiplayerMainWindow, self).__init__(parent)
        self.changeWindowTitle()
        
        self.nameAreaMapping = {
            'hero': self.heroArea,
            'engaged': self.engagedArea,
            'staging': self.stagingArea,
            'location': self.locationDeck,
            'quest': self.questDeck,
            'encounter': self.encounterDeck,
            'encounterDP': self.encounterDiscardPile,
            'prepare': self.prepareDeck,
            'removed': self.removedPile,
            'playerDP': self.playerDiscardPile,
        }
        self.stateFields = tuple(['threat', 'player'] + list(self.nameAreaMapping.keys()))
        
        self.prevState = self.getState()
        
        timer = QTimer(self)
        timer.timeout.connect(self.checkStateChange)
        timer.start(MultiplayerMainWindow.INTERVAL)
        
    def changeWindowTitle(self):
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
            self.playerDeckId = setupDialog.selectedDeckId()
        
        data = 'CLIENT:READY\n'
        self.client.sendData(data)
        
    def checkStateChange(self):
        state = self.getState()
        if state == self.prevState:
            return
            
        def dumpState(state):
            return json.dumps(state, separators=(',', ':'), encoding='ascii')
            
        for field in self.stateFields:
            if state[field] != self.prevState[field]:
                print 'prev   ', self.prevState[field]
                print 'current', state[field]
                jsonState = dumpState(state[field])
                data = 'STATE:{0}:{1}\n'.format(field, jsonState)
                self.client.sendData(data)
        self.prevState = self.getState()
        
    def getState(self):
        state = {}
        state['threat'] = self.threatDial.value
        state['player'] = len(self.playerDeck.getList())
        for (name, area) in self.nameAreaMapping.items():
            state[name] = area.getState()
        return state
        
    def handleStateChange(self, jsonState):
        (field, content) = jsonState.split(':', 1)
        state = json.loads(content, encoding='ascii')
        
        if field == 'threat':
            pass
        elif field == 'player':
            pass
        elif field in ('hero', 'engaged', 'playerDP'):
            pass
        elif field in ('staging', 'location', 'quest', 'encounter', 'encounterDP', 'prepare', 'removed'):
            self.nameAreaMapping[field].setState(state)
            print len(self.nameAreaMapping[field].getList())
            
        self.prevState = self.getState()
        
    def appendMessage(self, message):
        self.chatter.appendMessage(message)
        
    def appendSystemMessage(self, message):
        self.chatter.appendSystemMessage(message)
        
    def clientSocketDisconnected(self):
        pass
        
    def closeEvent(self, event):
        self.client.disconnectFromHost()
        if self.server:
            self.server.farewell()
        event.accept()