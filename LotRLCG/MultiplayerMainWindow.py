import json
from MainWindow import MainWindow
from MultiplayerPanel import MultiplayerPanel
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
        
        self.address = '{0}:{1}'.format(self.client.localAddress().toString(), self.client.localPort())
        
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
        self.stateFields = tuple(['threat', 'hand', 'player'] + list(self.nameAreaMapping.keys()))
        
        if self.isServer:
            self.server.startNewGame()
        
        self.prevState = self.getState()
        
        timer = QTimer(self)
        timer.timeout.connect(self.checkStateChange)
        timer.start(MultiplayerMainWindow.INTERVAL)
        
    def changeWindowTitle(self):
        title = str(self.windowTitle())
        if self.isServer:
            title += ' [Server]'
        else:
            title += ' [Client]'
            
        self.windowTitle = title
        title += '  (Press any key to bring up Multiplayer Panel)'
        self.setWindowTitle(title)
        
    def cleanup(self):
        if hasattr(self, 'panel'):
            self.panel.close()
            del self.panel
        super(MultiplayerMainWindow, self).cleanup()
        
    def restartGameAction(self):
        if self.isServer:
            self.server.setup()
            
    def startNewGameAction(self):
        if self.isServer:
            self.server.startNewGame()
            
    def startNewGame(self):
        self.cleanup()
        
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
        
    def setup(self):
        super(MultiplayerMainWindow, self).setup()
        
        state = self.getState()
        for field in self.stateFields:
            jsonState = self.dumpState(state[field])
            data = 'STATE:{0}:{1}:{2}\n'.format(self.address, field, jsonState)
            self.client.sendData(data)
            
        self.panel = MultiplayerPanel(self.addresses, self.nicknames, self.chatter, self)
        
    def getState(self):
        state = {}
        state['threat'] = self.threatDial.value
        state['hand'] = len(self.handArea.getList())  # hand size
        state['player'] = len(self.playerDeck.getList())  # deck size
        for (name, area) in self.nameAreaMapping.items():
            state[name] = area.getState()
            
        if hasattr(self, 'panel'):
            state.update(self.panel.getState())
        return state
        
    def dumpState(self, dictObject):
        return json.dumps(dictObject, separators=(',', ':'), encoding='ascii')
        
    def checkStateChange(self):
        state = self.getState()
        if state == self.prevState:
            return
            
        for field in state:
            try:
                if state[field] != self.prevState[field]:
                    if ':' in field:  # field is an address, modifying other player's state
                        address = field
                        for field_ in state[address]:
                            if state[address][field_] != self.prevState[address][field_]:
                                jsonState = self.dumpState(state[address][field_])
                                data = 'STATE:{0}:{1}:{2}\n'.format(address, field_, jsonState)
                                self.client.sendData(data)
                                self.prevState[address][field_] = state[address][field_]
                    else:
                        jsonState = self.dumpState(state[field])
                        data = 'STATE:{0}:{1}:{2}\n'.format(self.address, field, jsonState)
                        self.client.sendData(data)
                        self.prevState[field] = state[field]
            except KeyError:
                pass
        
    def handleStateChange(self, jsonState):
        (ip, port, field, content) = jsonState.split(':', 3)
        sourceAddress = '{0}:{1}'.format(ip, port)
        state = json.loads(content, encoding='ascii')
        
        if field in ('threat', 'hand', 'player', 'hero', 'engaged', 'playerDP'):
            if sourceAddress == self.address:
                self.nameAreaMapping[field].setState(state)
            else:
                if hasattr(self, 'panel'):
                    self.panel.updateState(sourceAddress, field, state)
        elif field in ('staging', 'location', 'quest', 'encounter', 'encounterDP', 'prepare', 'removed'):
            self.nameAreaMapping[field].setState(state)
            
        self.prevState = self.getState()
        
    def appendMessage(self, message):
        self.chatter.appendMessage(message)
        
    def appendSystemMessage(self, message):
        self.chatter.appendSystemMessage(message)
        
    def recordPlayerAddresses(self, playerAddresses):
        # example playerAddresses: '127.0.0.1:1234,140.116.39.40:1235,210.23.32.1:57649'
        self.addresses = playerAddresses.split(',')
        myAddress = '{0}:{1}'.format(self.client.localAddress().toString(), self.client.localPort())
        
        self.nthPlayer = self.addresses.index(myAddress)  # just for self.recordPlayerNicknames()
        self.addresses.remove(myAddress)
        
    def recordPlayerNicknames(self, playerNicknames):
        # example playerNicknames: 'amulet,nick,name'
        self.nicknames = playerNicknames.split(',')
        del self.nicknames[self.nthPlayer]
        
    def keyPressEvent(self, event):
        '''press any normal key to show MultiplayerPanel'''
        if event.modifiers() == Qt.NoModifier:
            if hasattr(self, 'panel'):
                self.setWindowTitle(self.windowTitle)
                self.panel.show()
        else:
            super(MultiplayerMainWindow, self).keyPressEvent(event)
            
    def resizeEvent(self, event):
        super(MultiplayerMainWindow, self).resizeEvent(event)
        if hasattr(self, 'panel'):
            self.panel.resizeEvent(None)
            
    def closeEvent(self, event):
        if hasattr(self, 'panel'):
            self.panel.close()
        self.client.disconnectFromHost()
        if self.server:
            self.server.farewell()
        event.accept()
        
    def createUI(self):
        super(MultiplayerMainWindow, self).createUI()
        if not self.isServer:
            self.newGameAct.setEnabled(False)
            self.restartGameAct.setEnabled(False)