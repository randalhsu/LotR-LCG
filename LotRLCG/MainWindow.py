'''
TODO: make dragging cursor correct
TODO: journey logging
'''
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
        
        closeButton = QPushButton(self.tr('&Close'))
        closeButton.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(self.tabWidget)
        layout.addWidget(closeButton)
        self.setLayout(layout)
        self.setMinimumWidth(500)
        self.setWindowTitle(self.tr('Phase Tips'))


class _About(QMessageBox):
    def __init__(self, parent=None):
        text = '<br><center><h2>The Lord of the Rings: The Card Game</h2><big>version {0}</big><br><br>Program written by amulet (Taiwan)</center><br><br>Try <b>Left / Right / Double Click</b> and <b>Drag & Drop</b> everywhere.<br><br><a href="http://www.fantasyflightgames.com/edge_minisite_sec.asp?eidm=129&esem=4">Game rules</a> available at Fantasy Flight Games website.<br><br><code><a href="https://github.com/amulet-tw/LotR-LCG">Source code</a> licensed under GNU GPL v2.</code>'.format(VERSION)
        super(_About, self).__init__(QMessageBox.Information, 'About', text, QMessageBox.Ok, parent)


class _MulliganDialog(QMessageBox):
    def __init__(self, parent=None):
            super(_MulliganDialog, self).__init__(QMessageBox.Question, 'Take MULLIGAN?', '<b>Redraw hand?</b>', parent=parent)
            self.addButton(self.tr("OF COURSE!"), QMessageBox.AcceptRole)
            no = self.addButton(self.tr("I'll keep them"), QMessageBox.RejectRole)
            self.setDefaultButton(no)
            self.setMinimumWidth(150)


class MainWindow(QMainWindow):
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
        if self.__class__.__name__ == 'MainWindow':  # not true in MultiplayerMainWindow
            self.startNewGame()
        
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
        
    def startNewGame(self):
        self.cleanup()
        setupDialog = SetupDialog(self)
        setupDialog.exec_()
        self.scenarioId = setupDialog.selectedScenarioId()
        self.playerDeckId = setupDialog.selectedDeckId()
        self.setup()
        
    def restartGame(self):
        self.cleanup()
        self.setup()
        
    def startNewGameAction(self):
        self.startNewGame()
        
    def restartGameAction(self):
        self.restartGame()
        
    def saveGame(self):
        jsonState = self.dumpState(self.getState())
        fileName = QFileDialog.getSaveFileName(self, self.tr('Save game'), 'LotRLCG.sav', 'Game Save (*.sav)')
        if fileName:
            try:
                f = open(fileName, 'w')
                f.write(jsonState)
                f.close()
            except IOError:
                QMessageBox.critical(self, self.tr("Can't save game"), self.tr('Failed to write file!'))
                
    def loadGame(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr('Load game'), '.', 'Game Save (*.sav)')
        if fileName:
            with open(fileName) as f:
                jsonState = f.read()
                try:
                    state = json.loads(jsonState, encoding='ascii')
                except ValueError:
                    QMessageBox.critical(self, self.tr("Can't load game"), self.tr('Game save corrupted!'))
                    return
                    
                self.threatDial.setValue(state['threat'])
                for (name, area) in self.nameAreaMapping.items():
                    area.setState(state[name])
                    
    def dumpState(self, dictObject):
        return json.dumps(dictObject, separators=(',', ':'), encoding='ascii')
        
    def getState(self):
        state = {}
        state['threat'] = self.threatDial.value
        for (name, area) in self.nameAreaMapping.items():
            state[name] = area.getState()
        return state
        
    def setup(self):
        scenarioId = self.scenarioId
        questList = []
        encounterList = []
        stagingList = []
        prepareList = []
        heroList = []
        playerList = []
        
        for encounterName in scenariosInfo[scenarioId]['encounters']:
            for set_ in SETS:
                for (id, card) in enumerate(cardsInfo[set_]):
                    if card['icon'] == encounterName and card['type'] != 'quest':
                        for i in range(card['quantity']):
                            encounterList.append((set_, id))
        
        for (set_, id) in playerDecksInfo[self.playerDeckId]['deck']:
            if isHeroCard(set_, id):
                heroList.append((set_, id))
            else:
                playerList.append((set_, id))
                
        random.shuffle(encounterList)
        random.shuffle(playerList)
        
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
                
        elif scenarioId == 1:  # Journey Along the Anduin
            questList = [(s, 126), (s, 127), (s, 128)]
            hillTroll = (s, 82)
            stagingList.append(encounterList.pop(-1))  # draw one card from encounter deck to staging area. 1 card per player.
            if stagingList[0] != hillTroll:
                stagingList.append(hillTroll)
                encounterList.remove(hillTroll)
                
        elif scenarioId == 2:  # Escape From Dol Guldur
            questList = [(s, 123), (s, 124), (s, 125)]
            prepareList = [(s, 102)]  # Nazgul of Dol Guldur
            encounterList.remove((s, 102))
            stagingList = [(s, 108), (s, 109), (s, 110)]  # Gandalf's Map, Dungeon Torch, Shadow Key
            for card in stagingList:
                encounterList.remove(card)
            for i in range(3):
                stagingList.append(encounterList.pop(-1))  # objective cards will be attached to their guarders later
            stagingList.reverse()
            
        elif scenarioId == 3:  # The Hunt for Gollum
            questList = [(s, 11), (s, 12), (s, 13)]
            stagingList.append(encounterList.pop(-1))  # 1 card per player
            
        elif scenarioId == 4:  # Conflict at the Carrock
            questList = [(s, 35), (s, 36)]
            stagingList = [(s, 43)]  # The Carrock
            encounterList.remove((s, 43))
            prepareList = [(s, 38), (s, 39), (s, 40), (s, 41), (s, 48), (s, 48), (s, 48), (s, 48)]  # 4 Trolls and 4 Sacked!s
            for card in prepareList:
                encounterList.remove(card)
                
        elif scenarioId == 5:  # A Journey to Rhosgobel
            questList = [(s, 60), (s, 61), (s, 62)]
            stagingList = [(s, 65), (s, 64)]  # Rhosgobel, Wilyador
            for card in stagingList:
                encounterList.remove(card)
            # Wilyador's damage tokens will be placed later
            
        elif scenarioId == 6:  # The Hills of Emyn Muil
            questList = [(s, 82)]
            stagingList = [(s, 83), (s, 84)]  # Amon Hen, Amon Lhaw
            for card in stagingList:
                encounterList.remove(card)
                
        elif scenarioId == 7:  # The Dead Marshes
            questList = [(s, 105), (s, 106)]
            stagingList = [(s, 107)]  # Gollum
            encounterList.remove((s, 107))
            stagingList.append(encounterList.pop(-1))  # 1 card per player
            
        elif scenarioId == 8:  # Return to Mirkwood
            questList = [(s, 126), (s, 127), (s, 128), (s, 129)]
            heroList.append((s, 130))  # Gollum
            encounterList.remove((s, 130))
            stagingList.append(encounterList.pop(-1))  # 1 card per player
            
        elif scenarioId == 9:  # The Massing at Osgiliath
            questList = [(s, 16), (s, 17), (s, 18), (s, 19)]
            stagingList = [(s, 2), (s, 3), (s, 4)]  # 3 Scouts per player
            prepareList = [(s, 1)]  # The Witch-king
            for card in stagingList:
                encounterList.remove(card)
            encounterList.remove((s, 1))
            
        elif scenarioId == 10:  # Into the Pit
            questList = [(s, 64), (s, 65), (s, 66)]
            stagingList = [(s, 16)]  # East-gate, put it to staging area and draw to location deck later
            encounterList.remove((s, 16))
            heroList.append((s, 41))  # Cave Torch, for first player
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
            while foe in encounterList:
                encounterList.remove(foe)
            encounterList.append(foe)  # 1 "A Foe Beyond" per player
            random.shuffle(encounterList)
            
            stagingList.append(encounterList.pop(-1))  # 1 card per player
            self.victorySpinBox.setValue(2)
            
        elif scenarioId == 13:  # The Redhorn Gate
            questList = [(s, 11), (s, 12), (s, 13)]
            stagingList = [(s, 15)]  # Caradhras
            encounterList.remove((s, 15))
            prepareList = [(s, 22), (s, 22), (s, 22), (s, 22), (s, 22)]  # 5 Snowstorms
            for card in prepareList:
                encounterList.remove(card)
            heroList.append((s, 14))  # Arwen Undomiel, for first player
            encounterList.remove((s, 14))
            stagingList.append(encounterList.pop(-1))  # 1 card per player
        # EXPANSION
        
        prepareList.reverse()
        
        # start creating Card instances
        for (set_, id) in reversed(questList):
            self.questDeck.addCard(Card(cardsInfo[set_][id], revealed=True))
            
        for (set_, id) in encounterList:
            self.encounterDeck.addCard(Card(cardsInfo[set_][id]))
            
        for (set_, id) in stagingList:
            self.stagingArea.addCard(Card(cardsInfo[set_][id], revealed=True))
            
        for (set_, id) in prepareList:
            self.prepareDeck.addCard(Card(cardsInfo[set_][id], revealed=True))
            
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
        
        
        if scenarioId == 2:  # Escape From Dol Guldur
            for i in range(3):
                objectiveCard = self.stagingArea.draw()
                self.stagingArea.getList()[i].attach(objectiveCard)
            
            hero = random.choice(self.heroArea.getList())
            hero.attach(Token('damage'))
            hero.flip()
            
        elif scenarioId == 5:  # A Journey to Rhosgobel
            for i in range(2):
                self.stagingArea.getList()[1].attach(Token('damage'))
                
        elif scenarioId == 10:  # Into the Pit
            self.locationDeck.addCard(self.stagingArea.draw())
        # EXPANSION
        
        #self.promptMulligan()
        
    def promptMulligan(self):
        if _MulliganDialog(self).exec_() == QMessageBox.AcceptRole:
            for i in range(6):
                card = self.handArea.draw()
                card.flip()
                self.playerDeck.addCard(card)
            self.playerDeck.shuffle()
            for i in range(6):
                card = self.playerDeck.draw()
                card.flip()
                self.handArea.addCard(card)
                
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
        card = self.playerDeck.draw()
        if card:
            if not card.revealed():
                card.flip()
            self.handArea.addCard(card)
        
    def proceedRefreshPhase(self):
        for card in self.heroArea.getList():
            card.ready()
            for child in card.attachedItems.equipments:
                child.ready()
        self.heroArea.update()
        self.heroArea.update()  # don't ask me why...
        self.threatDial.increaseValue()
        # TODO: pass first player token in multiplayer game
        
    def showPhaseTips(self):
        phaseTips = _PhaseTips(self)
        phaseTips.show()
        
    def showAbout(self):
        about = _About(self)
        about.show()
        
    def createUI(self):
        self.newGameAct = QAction(self.tr('&New Journey...'), self)
        self.newGameAct.triggered.connect(self.startNewGameAction)
        self.restartGameAct = QAction(self.tr('&Restart Journey'), self)
        self.restartGameAct.triggered.connect(self.restartGameAction)
        self.saveGameAct = QAction(self.tr('&Save Game'), self)
        self.saveGameAct.triggered.connect(self.saveGame)
        self.loadGameAct = QAction(self.tr('&Load Game'), self)
        self.loadGameAct.triggered.connect(self.loadGame)
        quitAct = QAction(self.tr('&Quit'), self)
        quitAct.triggered.connect(self.close)
        
        gameMenu = self.menuBar().addMenu(self.tr('&Game'))
        gameMenu.addAction(self.newGameAct)
        gameMenu.addAction(self.restartGameAct)
        gameMenu.addSeparator()
        gameMenu.addAction(self.saveGameAct)
        gameMenu.addAction(self.loadGameAct)
        gameMenu.addSeparator()
        gameMenu.addAction(quitAct)
        
        phaseTipsAct = QAction(self.tr('&Phase Tips'), self)
        phaseTipsAct.triggered.connect(self.showPhaseTips)
        aboutAct = QAction(self.tr('&About'), self)
        aboutAct.triggered.connect(self.showAbout)
        
        helpMenu = self.menuBar().addMenu(self.tr('&Help'))
        helpMenu.addAction(phaseTipsAct)
        helpMenu.addAction(aboutAct)
        
        self.largeImageLabel = QLabel()
        self.largeImageLabel.setFixedSize(CARD_WIDTH, CARD_HEIGHT)
        self.largeImageLabel.setPixmap(scaledCardPixmap('./resource/image/player_card_back.jpg'))
        self.largeImageLabel.currentCard = None
        
        self.threatDial = ThreatDial()
        self.threatDial.setFixedWidth(CARD_WIDTH)
        
        resourcePhaseButton = QPushButton(self.tr('Resource Phase'))
        resourcePhaseButton.clicked.connect(self.proceedResourcePhase)
        refreshPhaseButton = QPushButton(self.tr('Refresh Phase'))
        refreshPhaseButton.clicked.connect(self.proceedRefreshPhase)
        self.victorySpinBox = QSpinBox()
        victoryLabel = QLabel(self.tr('&Victory:'))
        victoryLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        victoryLabel.setBuddy(self.victorySpinBox)
        
        self.engagedArea = Area('Engaged Area')
        self.heroArea = Area('Hero Area')
        self.handArea = Area('Hand Area')
        self.stagingArea = Area('Staging Area', orientation=Qt.Vertical)
        
        self.locationDeck = Deck('Active Location')
        self.questDeck = Deck('Quest Deck')
        self.encounterDeck = Deck('Encounter Deck')
        self.encounterDiscardPile = Deck('Encounter Discard Pile')
        self.tokenBank = TokenBank()
        self.prepareDeck = Deck('Prepare Area', Qt.Horizontal)
        self.removedPile = Deck('Removed From Play', Qt.Horizontal)
        self.playerDeck = Deck('Player Deck')
        self.playerDiscardPile = Deck('Player Discard Pile')
        
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
        littleLayout.addWidget(refreshPhaseButton, 0, 2, 1, 2)
        littleLayout.addWidget(victoryLabel, 0, 4, 1, 1)
        littleLayout.addWidget(self.victorySpinBox, 0, 5, 1, 1)
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
        self.setWindowTitle(self.tr('The Lord of the Rings: The Card Game'))
        self.setWindowIcon(QIcon('./resource/image/LotRLCG.ico'))
        self.showMaximized()  # will trigger resizeEvent()
        
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())