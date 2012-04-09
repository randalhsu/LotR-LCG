'''
TODO: make dragging cursor correct
'''
import collections
import random
from common import *
from Draggable import *
from Area import *
from Deck import *
from TokenBank import *
from CardsTileView import *
from DeckManipulator import *
from ThreatDial import *
from SetupDialog import *
from JourneyLogger import *


class _ScoringDialog(QDialog):
    def __init__(self, parent=None):
        super(_ScoringDialog, self).__init__(parent)
        self.createUI()
        
    def updateContent(self):
        mainWindow = self.parentWidget()
        threat = mainWindow.threatDial.value
        dead = 0
        for card in mainWindow.playerDiscardPile.getList():  # dead heroes are in Player Discard Pile
            if isHeroCard(card.info['set'], card.info['id']):
                dead += card.info['cost']
                
        damages = 0
        for card in mainWindow.heroArea.getList():
            if isHeroCard(card.info['set'], card.info['id']):
                damages += card.getState().get('D', 0)  # damage tokens on hero
                
        victory = mainWindow.victorySpinBox.value()
        
        score = threat + dead + damages - victory
        
        content = QString('<tt><center>') + \
                  self.tr('  Final Threat Level: %1').arg(threat, 3) + QString('<br>') + \
                  self.tr('+   Dead Heroes Cost: %1').arg(dead, 3) + QString('<br>') + \
                  self.tr('+  Damages on Heroes: %1').arg(damages, 3) + QString('<br>') + \
                  self.tr('-     Victory Points: %1').arg(victory, 3) + \
                  QString('<hr>') + \
                  QString('<h2>%1</h2>').arg(self.tr('Final Score: %1').arg(score, 3)) + \
                  QString('</center><br></tt>')
        content = content.replace(' ', '&nbsp;')
        self.label.setText(content)
        
    def showEvent(self, event):
        if hasattr(self, 'lastGeometry'):
            self.setGeometry(self.lastGeometry)
        self.updateContent()
        
    def closeEvent(self, event):
        self.lastGeometry = self.geometry()
        event.accept()
        
    def createUI(self):
        self.label = QLabel()
        closeButton = QPushButton(QCoreApplication.translate('QObject', '&Close'))
        closeButton.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(closeButton)
        self.setLayout(layout)
        self.resize(300, 300)
        self.setWindowTitle(self.tr('Scoring'))


class _PhaseTips(QDialog):
    def __init__(self, parent=None):
        super(_PhaseTips, self).__init__(parent)
        phaseData = {
            'Resource': 'Add 1 resource to each hero.<br>Draw 1 card.',
            'Planning': 'Play ally and attachment cards. (Resource type must match.)',
            'Quest': '<b>Commit Characters</b>: Exhaust and commit characters to quest.<br><br><b>Staging</b>: Reveal 1 encounter card per player.<br><br><b>Quest Resolution</b>: Compare total committed willpower with total staging threat, add progress tokens to location/quest or raise threat.',
            'Travel': 'May travel to 1 location if there is no active location.',
            'Encounter': '<b>Player Engagement</b>: Players may choose to engage 1 enemy each.<br><br><b>Engagement Checks</b>: Check for each enemy if it engages a player (Engagement cost &lt;= Player\'s threat level).',
            'Combat': 'Deal 1 shadow card to each enemy (from highest engagement cost).<br><br><b>Resolve Enemy Attacks</b>:<br>    Choose an enemy<br>    Declare defender<br>    Resolve shadow effect<br>    Determine combat damage<br><br><b>Attack Enemies</b>:<br>    Choose an enemy and declare attackers<br>    Determine attack strength<br>    Determine combat damage',
            'Refresh': 'Each player raises threat level by 1.<br>Ready all cards.<br>Pass First-player token.',
        }
        
        self.tabWidget = QTabWidget()
        for phase in ('Resource', 'Planning', 'Quest', 'Travel', 'Encounter', 'Combat', 'Refresh'):
            text = phaseData[phase]
            label = QLabel(text)
            label.setMargin(10)
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self.tabWidget.addTab(label, phase)
        
        closeButton = QPushButton(QCoreApplication.translate('QObject', '&Close'))
        closeButton.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(self.tabWidget)
        layout.addWidget(closeButton)
        self.setLayout(layout)
        self.resize(500, 300)
        self.setWindowTitle(self.tr('Phase Tips'))
        
    def showEvent(self, event):
        if hasattr(self, 'lastGeometry'):
            self.setGeometry(self.lastGeometry)
            
    def closeEvent(self, event):
        self.lastGeometry = self.geometry()
        event.accept()


class _About(QMessageBox):
    def __init__(self, parent=None):
        text = '<br><center><h2>The Lord of the Rings: The Card Game</h2><big>version {0}</big><br><br>Program written by amulet (Taiwan)</center><br><br>Try <b>Left / Right / Double Click</b> and <b>Drag & Drop</b> everywhere.<br><br><a href="http://www.fantasyflightgames.com/edge_minisite_sec.asp?eidm=129&esem=4">Game rules</a> available at Fantasy Flight Games website.<br><br><code><a href="https://github.com/amulet-tw/LotR-LCG">Source code</a> licensed under GNU GPL v2.</code>'.format(VERSION)
        super(_About, self).__init__(QMessageBox.Information, QCoreApplication.translate('_About', 'About'), text, QMessageBox.Ok, parent)


class _MulliganDialog(QMessageBox):
    def __init__(self, parent=None):
        super(_MulliganDialog, self).__init__(QMessageBox.Question, QCoreApplication.translate('_MulliganDialog', 'Take MULLIGAN?'), QString('<b>%1</b>').arg(QCoreApplication.translate('_MulliganDialog', 'Redraw hand?')), parent=parent)
        yesButton = self.addButton(self.tr("OF COURSE!"), QMessageBox.YesRole)
        yesButton.clicked.connect(self.parentWidget().takeMulligan)
        noButton = self.addButton(self.tr("I'll keep them"), QMessageBox.NoRole)
        noButton.clicked.connect(self.parentWidget().giveUpMulligan)
        self.setDefaultButton(noButton)
        
        self.setModal(False)
        self.setMinimumWidth(200)
            
    def closeEvent(self, event):
        self.parentWidget().giveUpMulligan()
        event.accept()


class MainWindow(QMainWindow):
    AUTOSAVE_INTERVAL = 10000
    AUTOSAVE_PATH = './resource/AutoSave.sav'
    CONFIG_PATH = './resource/config.ini'
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.createUI()
        
        self.nameAreaMapping = {
            'hand': self.handArea,
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
        
        self.deckManipulatorList = []  # for bookkeeping existing DeckManipulator instances
        
        self.scenarioId = 0
        self.playerDeckId = 0
        self.isFirstPlayer = True  # might change in MultiplayerMainWindow
        self.playerCount = 1  # might change in MultiplayerMainWindow
        
        
        if self.__class__.__name__ == 'MainWindow':  # not true in MultiplayerMainWindow
            if self.checkIfprogramCrashed():
                self.loadGame(MainWindow.AUTOSAVE_PATH)
            else:
                self.startNewGame()
                
            # auto save just work in Solo game
            self.prevState = self.getState()
            def autoSave():
                state = self.getState()
                if state != self.prevState:
                    jsonState = self.dumpState(state)
                    with open(MainWindow.AUTOSAVE_PATH, 'w') as f:
                        f.write(jsonState)
                    self.prevState = state
                    
            timer = QTimer(self)
            timer.timeout.connect(autoSave)
            timer.start(MainWindow.AUTOSAVE_INTERVAL)
        
    def addDeckManipulator(self, widget):
        self.deckManipulatorList.append(widget)
        
    def cleanupDeckManipulators(self):
        for widget in self.deckManipulatorList:
            try:
                widget.close()
            except RuntimeError:
                pass
        self.deckManipulatorList = []
        
    def cleanup(self):
        self.victorySpinBox.setValue(0)
        self.cleanupDeckManipulators()
        
        for area in (self.engagedArea, self.heroArea, self.handArea, self.stagingArea, self.locationDeck, self.questDeck, self.encounterDeck, self.encounterDiscardPile, self.prepareDeck, self.removedPile, self.playerDeck, self.playerDiscardPile):
            area.setList([])
            while True:  # remove Card from scene until none left
                for card in area.scene.items():
                    if isinstance(card, Card):
                        area.scene.removeItem(card)
                        del card
                        break
                else:
                    break
            area.update()
            
        self.log('<hr><br>')
        
    def startNewGame(self):
        self.cleanup()
        setupDialog = SetupDialog(self)
        setupDialog.exec_()
        self.scenarioId = setupDialog.selectedScenarioId()
        self.playerDeckId = setupDialog.selectedDeckId()
        self.setup()
        
        self.prisonAct.setEnabled(self.scenarioId == 2)  # is it Escape From Dol Guldur?
        
    def restartGame(self):
        self.cleanup()
        self.setup()
        self.prisonAct.setEnabled(self.scenarioId == 2)  # is it Escape From Dol Guldur?
        
    def startNewGameAction(self):
        self.startNewGame()
        
    def restartGameAction(self):
        self.restartGame()
        
    def saveGame(self):
        state = self.getState()
        state['version'] = VERSION
        jsonState = self.dumpState(state)
        filePath = QFileDialog.getSaveFileName(self, QCoreApplication.translate('MainWindow', 'Save game'), 'LotRLCG.sav', QCoreApplication.translate('MainWindow', 'Game Save (*.sav)'))
        if filePath:
            if not saveFile(filePath, jsonState):
                QMessageBox.critical(self, QCoreApplication.translate('MainWindow', "Can't save game"), QCoreApplication.translate('MainWindow', 'Failed to write file!'))
                
    def loadGame(self, filePath=''):
        if not filePath:
            filePath = QFileDialog.getOpenFileName(self, QCoreApplication.translate('MainWindow', 'Load game'), '.', QCoreApplication.translate('MainWindow', 'Game Save (*.sav)'))
            
        if filePath:
            file = QFile(filePath)
            if file.open(QIODevice.ReadOnly | QIODevice.Text):
                jsonState = str(file.readAll())
                try:
                    state = json.loads(jsonState, encoding='ascii')
                except ValueError:
                    QMessageBox.critical(self, QCoreApplication.translate('MainWindow', "Can't load game"), QCoreApplication.translate('MainWindow', 'Game save corrupted!'))
                    return
                    
                self.victorySpinBox.setValue(state['victory'])
                self.threatDial.setValue(state['threat'])
                for (name, area) in self.nameAreaMapping.items():
                    area.setState(state[name])
                    
                file.close()
            else:
                QMessageBox.critical(self, QCoreApplication.translate('MainWindow', "Can't load game"), QCoreApplication.translate('MainWindow', 'Failed to open file!'))
                
    def dumpState(self, dictObject):
        return json.dumps(dictObject, separators=(',', ':'), encoding='ascii')
        
    def getState(self):
        state = {}
        state['victory'] = self.victorySpinBox.value()
        state['threat'] = self.threatDial.value
        for (name, area) in self.nameAreaMapping.items():
            state[name] = area.getState()
        return state
        
    def setup(self):
        self.setupPlayerCards()
        self.promptMulligan()
        
    def setupPlayerCards(self):
        heroList = []
        playerList = []
        
        for (set_, id) in playerDecksInfo[self.playerDeckId]['deck']:
            if isHeroCard(set_, id):
                heroList.append((set_, id))
            else:
                playerList.append((set_, id))
                
        random.shuffle(playerList)
        
        # start creating Card instances
        for (set_, id) in heroList:
            self.heroArea.addCard(Card(cardsInfo[set_][id], revealed=True))
            
        for (set_, id) in playerList:
            self.playerDeck.addCard(Card(cardsInfo[set_][id]))
            
        for i in range(6):
            if self.playerDeck.getList():
                card = self.playerDeck.draw()
                if not card.revealed():
                    card.flip()
                self.handArea.addCard(card)
                
        threatValue = 0
        for card in self.heroArea.getList():
           threatValue += card.info.get('cost', 0)
        self.threatDial.setValue(threatValue)
        
    def promptMulligan(self):
        mulliganDialog = _MulliganDialog(self)
        mulliganDialog.show()
        
    def takeMulligan(self):
        for i in range(6):
            card = self.handArea.draw()
            card.flip()
            self.playerDeck.addCard(card)
        self.playerDeck.shuffle()
        for i in range(6):
            card = self.playerDeck.draw()
            card.flip()
            self.handArea.addCard(card)
            
        self.mulliganDecisionIsMade()
        
    def giveUpMulligan(self):
        self.mulliganDecisionIsMade()
        
    def mulliganDecisionIsMade(self):
        self.setupEncounterCards()
        self.logInitialState()
        
    def setupEncounterCards(self):
        assert(self.isFirstPlayer)
        
        scenarioId = self.scenarioId
        heroList = []  # additional cards that First Player gains control, according to quest card's instructions
        questList = []
        encounterList = []
        stagingList = []
        prepareList = []
        
        for encounterName in scenariosInfo[scenarioId]['encounters']:
            for set_ in SETS:
                for (id, card) in enumerate(cardsInfo[set_]):
                    if card['icon'] == encounterName and card['type'] != 'quest':
                        for i in range(card['quantity']):
                            encounterList.append((set_, id))
        random.shuffle(encounterList)
        
        s = ''
        if scenarioId <= 2:
            s = 'core'
        elif scenarioId <= 8:
            s = 'mirkwood'
        elif scenarioId == 9:
            s = 'osgiliath'
        elif scenarioId <= 12:
            s = 'khazaddum'
        else:
            s = 'dwarrowdelf'
        # EXPANSION
        
        if scenarioId == 0:  # Passage Through Mirkwood
            questList = [(s, 119), (s, 120), (s, 121 + random.choice((0, 1)))]
            stagingList = [(s, 96), (s, 99)]
            for card in stagingList:
                encounterList.remove(card)
            random.shuffle(encounterList)
                
        elif scenarioId == 1:  # Journey Along the Anduin
            questList = [(s, 126), (s, 127), (s, 128)]
            hillTroll = (s, 82)
            for i in range(self.playerCount):
                stagingList.append(encounterList.pop(-1))  # draw one card from encounter deck to staging area. 1 card per player.
                
            hillTrollAppeared = False
            for card in stagingList:
                if card == hillTroll:
                    hillTrollAppeared = True
            if not hillTrollAppeared:
                stagingList.append(hillTroll)
                encounterList.remove(hillTroll)
                random.shuffle(encounterList)
                
        elif scenarioId == 2:  # Escape From Dol Guldur
            questList = [(s, 123), (s, 124), (s, 125)]
            prepareList = [(s, 102)]  # Nazgul of Dol Guldur
            encounterList.remove((s, 102))
            stagingList = [(s, 108), (s, 109), (s, 110)]  # Gandalf's Map, Dungeon Torch, Shadow Key
            for card in stagingList:
                encounterList.remove(card)
                
        elif scenarioId == 3:  # The Hunt for Gollum
            questList = [(s, 11), (s, 12), (s, 13)]
            if self.playerCount == 1:
                stagingList.append(encounterList.pop(-1))  # 1 card per player
                
        elif scenarioId == 4:  # Conflict at the Carrock
            questList = [(s, 35), (s, 36)]
            stagingList = [(s, 43)]  # The Carrock
            encounterList.remove((s, 43))
            prepareList = [(s, 38), (s, 39), (s, 40), (s, 41)]  # 4 Trolls
            for card in prepareList:
                encounterList.remove(card)
                
            sacked = (s, 48)
            while encounterList.count(sacked) > self.playerCount:  # 1 Sacked! per player
                encounterList.remove(sacked)
            random.shuffle(encounterList)
            
        elif scenarioId == 5:  # A Journey to Rhosgobel
            questList = [(s, 60), (s, 61), (s, 62)]
            heroList.append((s, 64))  # Wilyador, damage tokens will be placed after Card instance created  # TODO: this is for first player
            encounterList.remove((s, 64))
            stagingList = [(s, 65)]  # Rhosgobel
            encounterList.remove((s, 65))
            
        elif scenarioId == 6:  # The Hills of Emyn Muil
            questList = [(s, 82)]
            stagingList = [(s, 83), (s, 84)]  # Amon Hen, Amon Lhaw
            for card in stagingList:
                encounterList.remove(card)
                
        elif scenarioId == 7:  # The Dead Marshes
            questList = [(s, 105), (s, 106)]
            stagingList = [(s, 107)]  # Gollum
            encounterList.remove((s, 107))
            if self.playerCount == 1:
                stagingList.append(encounterList.pop(-1))  # 1 card per player
            
        elif scenarioId == 8:  # Return to Mirkwood
            questList = [(s, 126), (s, 127), (s, 128), (s, 129)]
            gollum = (s, 130)
            encounterList.remove(gollum)
            if self.playerCount == 1:
                heroList.append(gollum)
                stagingList.append(encounterList.pop(-1))  # 1 card per player
            else:
                stagingList.append(gollum)
                
        elif scenarioId == 9:  # The Massing at Osgiliath
            questList = [(s, 16), (s, 17), (s, 18), (s, 19)]
            scouts = ((s, 2), (s, 3), (s, 4))  # 3 Scouts per player
            for scout in scouts:
                for i in range(min(4, self.playerCount)):
                    stagingList.append(scout)
            for card in stagingList:
                encounterList.remove(card)
            random.shuffle(encounterList)
            prepareList = [(s, 1)]  # The Witch-king
            encounterList.remove((s, 1))
            
        elif scenarioId == 10:  # Into the Pit
            questList = [(s, 64), (s, 65), (s, 66)]
            stagingList = [(s, 16)]  # East-gate, put it to staging area and draw to location deck later
            encounterList.remove((s, 16))
            heroList.append((s, 41))  # Cave Torch, for first player  # TODO: this is for first player
            encounterList.remove((s, 41))
            prepareList = [(s, 17), (s, 18)]  # First Hall, Bridge of Khazad-dum
            for card in prepareList:
                encounterList.remove(card)
                
        elif scenarioId == 11:  # The Seventh Level
            questList = [(s, 67), (s, 68)]
            heroList.append((s, 24))  # Book of Mazarbul, for first player
            encounterList.remove((s, 24))
            
        elif scenarioId == 12:  # Flight from Moria
            questList = [(s, i) for i in range(70, 77)]
            random.shuffle(questList)
            questList.insert(0, (s, 69))
            
            stagingList = [(s, 25)]  # The Nameless Fear
            encounterList.remove((s, 25))
            
            foe = (s, 28)  # A Foe Beyond
            while encounterList.count(foe) > self.playerCount:  # 1 "A Foe Beyond" per player
                encounterList.remove(foe)
            random.shuffle(encounterList)
            if self.playerCount == 1:
                stagingList.append(encounterList.pop(-1))  # 1 card per player
                
        elif scenarioId == 13:  # The Redhorn Gate
            questList = [(s, 11), (s, 12), (s, 13)]
            stagingList = [(s, 15)]  # Caradhras
            encounterList.remove((s, 15))
            prepareList = [(s, 22), (s, 22), (s, 22), (s, 22), (s, 22)]  # 5 Snowstorms
            for card in prepareList:
                encounterList.remove(card)
            heroList.append((s, 14))  # Arwen Undomiel, for first player  # TODO: this is for first player
            encounterList.remove((s, 14))
            if self.playerCount == 1:
                stagingList.append(encounterList.pop(-1))  # 1 card per player
                
        elif scenarioId == 14:  # Road to Rivendell
            questList = [(s, 38), (s, 39), (s, 40)]
            heroList.append((s, 41))  # Arwen Undomiel, for first player  # TODO: this is for first player
            encounterList.remove((s, 41))
            if self.playerCount == 1:
                stagingList.append(encounterList.pop(-1))  # 1 card per player
        # EXPANSION
        
        prepareList.reverse()
        
        # start creating Card instances
        for (set_, id) in heroList:
            self.heroArea.addCard(Card(cardsInfo[set_][id], revealed=True))
            
        for (set_, id) in reversed(questList):
            self.questDeck.addCard(Card(cardsInfo[set_][id], revealed=True))
            
        for (set_, id) in encounterList:
            self.encounterDeck.addCard(Card(cardsInfo[set_][id]))
            
        for (set_, id) in stagingList:
            self.stagingArea.addCard(Card(cardsInfo[set_][id], revealed=True))
            
        for (set_, id) in prepareList:
            self.prepareDeck.addCard(Card(cardsInfo[set_][id], revealed=True))
        
        
        # post processing
        title = QCoreApplication.translate('MainWindow', 'Manually Setup Required')
        if scenarioId == 2:  # Escape From Dol Guldur
            QMessageBox.information(self, title, QCoreApplication.translate('MainWindow', 'Objective cards are Guarded!'))
            
        elif scenarioId in (3, 7, 12, 13, 14):  # The Hunt for Gollum, The Dead Marshes, Flight from Moria, The Redhorn Gate, Road to Rivendell
            if self.playerCount > 1:
                QMessageBox.information(self, title, QCoreApplication.translate('MainWindow', 'Reveal 1 card per player!'))
                
        elif scenarioId == 5:  # A Journey to Rhosgobel
            for i in range(2):  # attach 2 damage token to Wilyador
                self.heroArea.getList()[-1].attach(Token('damage'))
                
        elif scenarioId == 8:  # Return to Mirkwood
            if self.playerCount > 1:
                QMessageBox.information(self, title, QString('%1<br>%2').arg(QCoreApplication.translate('MainWindow', 'Choose a player to guard %1,').arg('<b>"Gollum"</b>')).arg(QCoreApplication.translate('MainWindow', 'then reveal 1 card per player.')))
                
        elif scenarioId == 10:  # Into the Pit
            self.locationDeck.addCard(self.stagingArea.draw())  # make East-gate as active location
            QMessageBox.information(self, title, QString('%1<br>%2').arg(QCoreApplication.translate('MainWindow', 'Attach %1 to a hero,').arg('<b>"Cave Torch"</b>')).arg(QCoreApplication.translate('MainWindow', 'then reveal 1 card per player.')))
            
        elif scenarioId == 11:  # The Seventh Level
            QMessageBox.information(self, title, QString('%1<br>%2').arg(QCoreApplication.translate('MainWindow', 'Attach %1 to a hero,').arg('<b>"Book of Mazarbul"</b>')).arg(QCoreApplication.translate('MainWindow', 'then reveal 1 card per player.')))
        # EXPANSION
        
    def logInitialState(self):
        heroes = [repr(card) for card in self.heroArea.getList()]
        heroesString = ''
        pronoun = 'their'
        if len(heroes) == 1:
            heroesString = heroes[0]
            pronoun = 'his/her'
        elif len(heroes) == 2:
            heroesString = '{0} and {1}'.format(heroes[0], heroes[1])
        elif len(heroes) >= 3:
            heroesString = '{0} and {1}'.format(', '.join(heroes[:-1]), heroes[-1])
        self.log('<h3>{0} started {1} journey on <b>[{2}]</b>...</h3>'.format(heroesString, pronoun, scenariosInfo[self.scenarioId]['name']))
        self.logCurrentState()
        if self.questDeck.getList():
            self.log('Questing {0}'.format(repr(self.questDeck.getList()[-1])))
            
    def logCurrentState(self):
        self.log('<br>')
        self.threatDial.appendLog()
        hand = [repr(card) for card in self.handArea.getList()]
        self.log('Hand: {0}'.format(', '.join(hand)))
        staging = [repr(card) for card in self.stagingArea.getList()]
        self.log('Staging: {0}'.format(', '.join(staging)))
        self.log('<br>')
        
    def setLargeImage(self, card):
        if card.info['type'] != 'quest':
            if self.largeImageLabel.currentCard == (card, card.revealed()):
                return
                
        if card.info['type'] == 'quest':
            ratio = float(CARD_WIDTH) / CARD_HEIGHT
            transform = QTransform.fromScale(ratio, ratio)
            transform = transform.rotate(90)
            pixmap = card.pixmap().transformed(transform, Qt.SmoothTransformation)
        else:
            pixmap = card.currentImage()
            
        self.largeImageLabel.setPixmap(pixmap)
        self.largeImageLabel.currentCard = (card, card.revealed())
        
    def proceedResourcePhase(self):
        for card in self.heroArea.getList():
            if card.info['type'] == 'hero' and card.revealed():
                card.attach(Token('resource'))
                tokenCount = card.getState().get('R', 0)
                self.log('{0}->{1}({2})'.format('resource', repr(card), tokenCount))
        card = self.playerDeck.draw()
        if card:
            if not card.revealed():
                card.flip()
            self.handArea.addCard(card)
            self.log('Draw {0}'.format(repr(card)))
            
    def proceedRefreshPhase(self):
        for card in self.heroArea.getList():
            card.ready()
            for child in card.attachedItems.equipments:
                child.ready()
        self.heroArea.update()
        self.heroArea.update()  # don't ask me why...
        self.log('All card readied')
        self.threatDial.increaseValue()
        self.threatDial.appendLog()
        # TODO: pass first player token in multiplayer game
        
    def proceedDealShadows(self):
        enemies = filter(lambda card: 'cost' in card.info, list(self.engagedArea.getList()))
        enemies.sort(reverse=True, key=lambda card: card.info['cost'])  # sort from highest to lowest engagement cost
        for enemy in enemies:
            card = self.encounterDeck.draw()
            if card:
                enemy.attach(card)
                shadow = repr(card) if card.revealed() else '[???]'
                self.log('Deal shadow {0} to {1}'.format(shadow, enemy))
                
    def writeSettings(self):
        settings = QSettings(MainWindow.CONFIG_PATH, QSettings.IniFormat)
        
        settings.beginGroup('Localization')
        settings.setValue('Interface', self.locale)
        settings.endGroup()
        
        settingMapping = {
            'MainWindow': self,
            'JourneyLogger': self.journeyLogger,
            'ScoringDialog': self.scoringDialog,
            'PhaseTips': self.phaseTips,
        }
        settings.beginGroup('Geometry')
        for (name, widget) in settingMapping.items():
            settings.beginGroup(name)
            if name == 'MainWindow':
                settings.setValue('maximized', widget.isMaximized())
            settings.setValue('size', widget.size())
            settings.setValue('pos', widget.pos())
            settings.endGroup()
        settings.endGroup()
        
        settings.beginGroup('ProgramState')
        settings.setValue('crashed', False)  # if program ended up normally, this flag is set to False
        settings.endGroup()
        
    def readSettings(self):
        settings = QSettings(MainWindow.CONFIG_PATH, QSettings.IniFormat)
        settings.beginGroup('Geometry')
        settings.beginGroup('MainWindow')
        maximized = settings.value('maximized', True).toBool()
        if maximized:
            self.showMaximized()
        else:
            self.resize(settings.value('size', QSize(1024, 728)).toSize())
            self.move(settings.value('pos', QPoint(0, 0)).toPoint())
        settings.endGroup()
        
        settingMapping = {
            'JourneyLogger': self.journeyLogger,
            'PhaseTips': self.phaseTips,
        }
        for (name, widget) in settingMapping.items():
            settings.beginGroup(name)
            widget.resize(settings.value('size', QSize(500, 300)).toSize())
            pos = settings.value('pos').toPoint()
            if pos != QPoint():
                widget.move(pos)
            settings.endGroup()
            
        settings.beginGroup('ScoringDialog')
        self.scoringDialog.resize(settings.value('size', QSize(300, 300)).toSize())
        pos = settings.value('pos').toPoint()
        if pos != QPoint():
            self.scoringDialog.move(pos)
        settings.endGroup()
        settings.endGroup()  # Geometry
        
    def checkIfprogramCrashed(self):
        '''did program crash on last time running?'''
        settings = QSettings(MainWindow.CONFIG_PATH, QSettings.IniFormat)
        settings.beginGroup('ProgramState')
        crashed = settings.value('crashed', False).toBool()
        settings.setValue('crashed', True)  # set it to True to detect next crash
        settings.endGroup()
        return crashed
        
    def log(self, message):
        '''method for logging what happened. Will be rebinded to JourneyLogger in createUI()'''
        pass
        
    def createUI(self):
        self.newGameAct = QAction(QCoreApplication.translate('MainWindow', '&New Journey...'), self)
        self.newGameAct.triggered.connect(self.startNewGameAction)
        self.newGameAct.setShortcut(QKeySequence.New)
        self.restartGameAct = QAction(QCoreApplication.translate('MainWindow', '&Restart Journey'), self)
        self.restartGameAct.triggered.connect(self.restartGameAction)
        self.restartGameAct.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_R))
        self.saveGameAct = QAction(QCoreApplication.translate('MainWindow', '&Save Game'), self)
        self.saveGameAct.triggered.connect(self.saveGame)
        self.saveGameAct.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_S))
        self.loadGameAct = QAction(QCoreApplication.translate('MainWindow', '&Load Game'), self)
        self.loadGameAct.triggered.connect(self.loadGame)
        self.loadGameAct.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))
        quitAct = QAction(QCoreApplication.translate('MainWindow', '&Quit'), self)
        quitAct.triggered.connect(self.close)
        quitAct.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q))
        
        gameMenu = self.menuBar().addMenu(QCoreApplication.translate('MainWindow', '&Game'))
        gameMenu.addAction(self.newGameAct)
        gameMenu.addAction(self.restartGameAct)
        gameMenu.addSeparator()
        gameMenu.addAction(self.saveGameAct)
        gameMenu.addAction(self.loadGameAct)
        gameMenu.addSeparator()
        gameMenu.addAction(quitAct)
        
        self.journeyLogger = JourneyLogger(self)
        self.log = self.journeyLogger.append  # this 'log' function will be called by those who wants to write journey log
        
        self.journeyLoggerAct = QAction(QCoreApplication.translate('MainWindow', '&Journey Logger'), self)
        self.journeyLoggerAct.triggered.connect(lambda: self.journeyLogger.show())
        self.journeyLoggerAct.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_J))
        self.journeyLoggerAct.setIcon(QIcon(':/images/tokens/progress.png'))
        
        self.phaseTips = _PhaseTips(self)
        phaseTipsAct = QAction(QCoreApplication.translate('MainWindow', '&Phase Tips'), self)
        phaseTipsAct.triggered.connect(lambda: self.phaseTips.show())
        phaseTipsAct.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_P))
        
        def prisonRandomHero():
            hero = random.choice(self.heroArea.getList())
            self.log('{0} is prisoned!'.format(hero))
            hero.flip()
            hero.attach(Token('damage'))
            
        self.prisonAct = QAction(QCoreApplication.translate('MainWindow', 'Prison a random Hero'), self)
        self.prisonAct.triggered.connect(prisonRandomHero)
        self.prisonAct.setToolTip(QCoreApplication.translate('MainWindow', 'For "Escape From Dol Guldur" scenario'))
        
        self.scoringDialog = _ScoringDialog(self)
        self.scoringAct = QAction(QCoreApplication.translate('MainWindow', 'Scoring...'), self)
        self.scoringAct.triggered.connect(lambda: self.scoringDialog.show())
        
        utilityMenu = self.menuBar().addMenu(QCoreApplication.translate('MainWindow', '&Utility'))
        utilityMenu.addAction(self.journeyLoggerAct)
        utilityMenu.addAction(phaseTipsAct)
        utilityMenu.addSeparator()
        utilityMenu.addAction(self.prisonAct)
        utilityMenu.addAction(self.scoringAct)
        
        self.about = _About(self)
        aboutAct = QAction(QCoreApplication.translate('MainWindow', '&About'), self)
        aboutAct.triggered.connect(lambda: self.about.show())
        
        helpMenu = self.menuBar().addMenu(QCoreApplication.translate('MainWindow', '?'))
        
        def currentLocaleSetting():
            settings = QSettings(MainWindow.CONFIG_PATH, QSettings.IniFormat)
            settings.beginGroup('Localization')
            locale = str(settings.value('Interface', 'None').toString())
            settings.endGroup()
            return locale
            
        def detectUsableLocalization():
            locale = QLocale().system().name()
            for qmFilePath in glob.glob('./resource/translations/*.qm'):
                qmFilePath = qmFilePath.replace('\\', '/')
                qm = qmFilePath[qmFilePath.rindex('/') + 1 : -3]
                qm = qm.replace('qt_', '')
                if locale == qm:
                    return locale
            return 'en_US'
            
        self.locale = currentLocaleSetting()
        if self.locale == 'None':  # first start up
            self.locale = detectUsableLocalization()
            
        def changeLocale(locale):
            def changeLocale_():
                self.locale = locale
                QMessageBox.information(self, QCoreApplication.translate('MainWindow', 'Setting Changed'), QCoreApplication.translate('MainWindow', 'Restart program to apply change.'))
            return changeLocale_
            
        languages = collections.OrderedDict()
        languages[QCoreApplication.translate('MainWindow', 'English')] = 'en_US'
        languages[QCoreApplication.translate('MainWindow', 'Traditional Chinese')] = 'zh_TW'
        languages[QCoreApplication.translate('MainWindow', 'Simplified Chinese')] = 'zh_CN'
        
        interfaceLanguageMenu = helpMenu.addMenu(QCoreApplication.translate('MainWindow', 'Interface Langauge'))
        languageGroup = QActionGroup(self)
        for (language, locale) in languages.items():
            changeLanguageAct = QAction(language, self, checkable=True)
            changeLanguageAct.triggered.connect(changeLocale(locale))
            languageGroup.addAction(changeLanguageAct)
            
            interfaceLanguageMenu.addAction(changeLanguageAct)
            if locale == self.locale:
                changeLanguageAct.setChecked(True)
                
        helpMenu.addAction(aboutAct)
        
        self.largeImageLabel = QLabel()
        self.largeImageLabel.setFixedSize(CARD_WIDTH, CARD_HEIGHT)
        self.largeImageLabel.setPixmap(QPixmap(':/images/player_card_back.jpg'))
        self.largeImageLabel.currentCard = None
        
        self.threatDial = ThreatDial()
        self.threatDial.setFixedWidth(CARD_WIDTH)
        
        resourcePhaseButton = QPushButton(QCoreApplication.translate('MainWindow', 'Resource Phase'))
        resourcePhaseButton.clicked.connect(self.proceedResourcePhase)
        resourcePhaseButton.setToolTip(QString('%1<br>%2').arg(QCoreApplication.translate('MainWindow', 'Add 1 resource to each hero and draw 1 card.')).arg(QCoreApplication.translate('MainWindow', 'Special card-effects are not concerned.')))
        resourcePhaseButton.setFocusPolicy(Qt.NoFocus)
        dealShadowsButton = QPushButton(QCoreApplication.translate('MainWindow', 'Deal Shadows'))
        dealShadowsButton.clicked.connect(self.proceedDealShadows)
        dealShadowsButton.setToolTip(QString('%1<br>%2').arg(QCoreApplication.translate('MainWindow', 'Deal 1 shadow card to each engaged enemy.')).arg(QCoreApplication.translate('MainWindow', 'Special card-effects are not concerned.')))
        dealShadowsButton.setFocusPolicy(Qt.NoFocus)
        refreshPhaseButton = QPushButton(QCoreApplication.translate('MainWindow', 'Refresh Phase'))
        refreshPhaseButton.clicked.connect(self.proceedRefreshPhase)
        refreshPhaseButton.setToolTip(QString('%1<br>%2').arg(QCoreApplication.translate('MainWindow', 'Ready all cards and raise 1 threat.')).arg(QCoreApplication.translate('MainWindow', 'Special card-effects are not concerned.')))
        refreshPhaseButton.setFocusPolicy(Qt.NoFocus)
        
        self.victorySpinBox = QSpinBox()
        self.victorySpinBox.valueChanged.connect(lambda: self.log('<font color="#3f48cc">Victory Points: {0}</font>'.format(self.victorySpinBox.value())))
        victoryLabel = QLabel(QCoreApplication.translate('MainWindow', '&Victory:'))
        victoryLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        victoryLabel.setBuddy(self.victorySpinBox)
        
        self.engagedArea = Area('Engaged Area')
        self.heroArea = Area('Hero Area')
        self.handArea = Area('Hand Area')
        self.stagingArea = Area('Staging Area', orientation=Qt.Vertical)
        
        self.locationDeck = Deck('Active Location', QCoreApplication.translate('MainWindow', 'Active<br>Location', 'Deck'))
        self.questDeck = Deck('Quest Deck', QCoreApplication.translate('MainWindow', 'Quest<br>Deck', 'Deck'))
        self.encounterDeck = Deck('Encounter Deck', QCoreApplication.translate('MainWindow', 'Encounter<br>Deck', 'Deck'))
        self.encounterDiscardPile = Deck('Encounter Discard Pile', QCoreApplication.translate('MainWindow', 'Encounter<br>Discard<br>Pile', 'Deck'))
        self.tokenBank = TokenBank()
        self.prepareDeck = Deck('Prepare Deck', QCoreApplication.translate('MainWindow', 'Prepare<br>Deck', 'Deck'), Qt.Horizontal)
        self.removedPile = Deck('Removed From Play', QCoreApplication.translate('MainWindow', 'Removed<br>From<br>Play', 'Deck'), Qt.Horizontal)
        self.playerDeck = Deck('Player Deck', QCoreApplication.translate('MainWindow', 'Player<br>Deck', 'Deck'))
        self.playerDiscardPile = Deck('Player Discard Pile', QCoreApplication.translate('MainWindow', 'Player<br>Discard<br>Pile', 'Deck'))
        
        self.engagedArea.setBackgroundBrush(QBrush(Qt.darkRed))
        self.heroArea.setBackgroundBrush(QBrush(Qt.darkBlue))
        self.handArea.setBackgroundBrush(QBrush(Qt.darkCyan))
        self.stagingArea.setBackgroundBrush(QBrush(Qt.black))
        self.locationDeck.setBackgroundBrush(QBrush(Qt.darkGreen))
        self.questDeck.setBackgroundBrush(QBrush(Qt.darkGreen))
        self.encounterDeck.setBackgroundBrush(QBrush(Qt.gray))
        self.encounterDiscardPile.setBackgroundBrush(QBrush(Qt.darkGray))
        self.prepareDeck.setBackgroundBrush(QBrush(Qt.gray))
        self.removedPile.setBackgroundBrush(QBrush(Qt.black))
        self.playerDeck.setBackgroundBrush(QBrush(Qt.yellow))
        self.playerDiscardPile.setBackgroundBrush(QBrush(Qt.darkYellow))
        
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.largeImageLabel)
        leftLayout.addStretch(1)
        leftLayout.addWidget(self.threatDial)
        littleLayout = QGridLayout()
        littleLayout.addWidget(resourcePhaseButton, 0, 0, 1, 2)
        littleLayout.addWidget(dealShadowsButton, 0, 2, 1, 2)
        littleLayout.addWidget(refreshPhaseButton, 0, 4, 1, 2)
        littleLayout.addWidget(victoryLabel, 0, 6, 1, 1)
        littleLayout.addWidget(self.victorySpinBox, 0, 7, 1, 1)
        leftLayout.addLayout(littleLayout)
        
        midLayout = QVBoxLayout()
        midLayout.addWidget(self.engagedArea)
        midLayout.addWidget(self.heroArea)
        midLayout.addWidget(self.handArea)
        
        rightLayout = QGridLayout()
        rightLayout.addWidget(self.locationDeck, 0, 0, 1, 1)
        rightLayout.addWidget(self.questDeck, 0, 1, 1, 1)
        rightLayout.addWidget(self.encounterDeck, 1, 0, 1, 1)
        rightLayout.addWidget(self.encounterDiscardPile, 1, 1, 1, 1)
        rightLayout.addWidget(self.prepareDeck, 2, 0, 1, 1)
        rightLayout.addWidget(self.removedPile, 2, 1, 1, 1)
        rightLayout.addWidget(self.tokenBank, 3, 0, 1, 2)
        rightLayout.addWidget(self.playerDeck, 4, 0, 1, 1)
        rightLayout.addWidget(self.playerDiscardPile, 4, 1, 1, 1)
        
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(midLayout)
        layout.addWidget(self.stagingArea)
        layout.addLayout(rightLayout)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        
        self.setCentralWidget(centralWidget)
        self.setWindowTitle(QCoreApplication.translate('MainWindow', 'The Lord of the Rings: The Card Game'))
        self.setWindowIcon(QIcon(':/images/icons/LotRLCG.ico'))
        self.showMaximized()  # will trigger resizeEvent()
        self.readSettings()
        
    def resizeEvent(self, event):
        if hasattr(self, 'locationDeck'):  # if self.createUI() is called
            for deck in (self.locationDeck, self.questDeck, self.encounterDeck, self.encounterDiscardPile, self.playerDeck, self.playerDiscardPile):
                ratio = float(deck.height()) / CARD_HEIGHT
                deck.setFixedWidth((CARD_WIDTH + PADDING * 2) * ratio)
                
            for deck in (self.prepareDeck, self.removedPile):
                deck.setFixedSize(self.locationDeck.width(), self.locationDeck.height() * 2 / 5)
                
            self.stagingArea.setMinimumWidth(self.locationDeck.width())
            self.stagingArea.setMaximumWidth(self.locationDeck.width() * 1.1)
            
            self.engagedArea.setMinimumHeight(self.height() / 3)
            self.heroArea.setMinimumHeight(self.height() / 3)
            self.handArea.setMinimumHeight(self.height() / 4)
            
            width = self.stagingArea.width() * 2
            self.engagedArea.setMinimumWidth(width)
            self.heroArea.setMinimumWidth(width)
            self.handArea.setMinimumWidth(width)
            QApplication.processEvents()  # force immediate update
            
    def closeEvent(self, event):
        self.writeSettings()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())