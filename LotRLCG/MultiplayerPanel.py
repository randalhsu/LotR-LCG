from PyQt4.QtGui import *
from common import *
from Area import *


class _PlayerStatePanel(QWidget):
    def __init__(self, address, nickname, parent=None):
        super(_PlayerStatePanel, self).__init__(parent)
        self.address = address  # this panel is which player's state?
        self.nickname = nickname  # this panel is which player's state?
        self.createUI()
        
        self.nameAreaMapping = {
            'hero': self.heroArea,
            'engaged': self.engagedArea,
            'playerDP': self.discardPile,
        }
        
    def updateState(self, field, state):
        if field == 'threat':
            self.threatValue.display(str(state))
        elif field == 'hand':
            self.handValue.display(str(state))
        elif field == 'player':
            self.deckValue.display(str(state))
        elif field == 'hero':
            self.heroArea.setState(state)
        elif field == 'engaged':
            self.engagedArea.setState(state)
        elif field == 'playerDP':
            self.discardPile.setState(state)
            
    def getState(self):
        state = {}
        for (name, area) in self.nameAreaMapping.items():
            state[name] = area.getState()
        return state
        
    def resizeEvent(self, event):
        halfHieght = self.height() / 2
        self.engagedArea.setFixedHeight(halfHieght)
        self.heroArea.setFixedHeight(halfHieght)
        self.discardPile.setFixedHeight(halfHieght)
        
        ratio = float(self.discardPile.height()) / CARD_HEIGHT
        width = CARD_WIDTH * ratio
        
        self.nicknameLabel.setMaximumWidth(width * 1.1)
        self.discardPile.setMinimumWidth(width)
        self.discardPile.setMaximumWidth(width * 1.1)
        self.handValue.setMinimumWidth(width / 2)
        self.deckValue.setMinimumWidth(width / 2)
        self.threatValue.setMinimumWidth(width)
        for lcd in (self.threatValue, self.handValue, self.deckValue):
            lcd.setMinimumHeight(width * 2 / 5)
            lcd.setMaximumHeight(width * 3 / 5)
            
        # then we adjust nickanmeLabel's size
        def tooWide(fontMetrics):
            return fontMetrics.width(self.nicknameLabel.text()) > self.nicknameLabel.width() - 10
            
        def tooHigh(fontMetrics):
            return fontMetrics.height() > self.nicknameLabel.height() - 5
            
        font = self.nicknameLabel.font()
        pointSize = 80
        font.setPointSize(pointSize)
        fm = QFontMetrics(font)
        
        while tooWide(fm) or tooHigh(fm):
            if pointSize <= 10:
                break
            pointSize -= 2
            font.setPointSize(pointSize)
            fm = QFontMetrics(font)
        self.nicknameLabel.setFont(font)
        
    def createUI(self):
        self.nicknameLabel = QLabel(self.nickname)
        
        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.darkCyan)
        self.handValue = QLCDNumber(2)
        self.handValue.setPalette(palette)
        self.handValue.setSegmentStyle(QLCDNumber.Flat)
        self.handValue.setToolTip(self.tr('Hand Size'))
        self.handValue.display(6)
        
        palette.setColor(QPalette.WindowText, Qt.black)
        self.deckValue = QLCDNumber(2)
        self.deckValue.setPalette(palette)
        self.deckValue.setSegmentStyle(QLCDNumber.Flat)
        self.deckValue.setToolTip(self.tr('Deck Size'))
        self.deckValue.display(30)
        
        palette.setColor(QPalette.WindowText, Qt.red)
        self.threatValue = QLCDNumber(2)
        self.threatValue.setPalette(palette)
        self.threatValue.setSegmentStyle(QLCDNumber.Flat)
        self.threatValue.setToolTip(self.tr('Threat Level'))
        self.threatValue.display(20)
        
        self.engagedArea = Area('Engaged Area')
        self.engagedArea.setBackgroundBrush(QBrush(Qt.darkRed))
        self.heroArea = Area('Hero Area')
        self.heroArea.setBackgroundBrush(QBrush(Qt.darkBlue))
        self.discardPile = Deck('Player Discard Pile', self.tr('Player<br>Discard<br>Pile', 'Deck'))
        self.discardPile.setBackgroundBrush(QBrush(Qt.darkYellow))
        
        lcdLayout = QGridLayout()
        lcdLayout.addWidget(self.handValue, 0, 0, 1, 1)
        lcdLayout.addWidget(self.deckValue, 0, 1, 1, 1)
        lcdLayout.addWidget(self.threatValue, 1, 0, 1, 2)
        
        topLeftLayout = QVBoxLayout()
        topLeftLayout.addWidget(self.nicknameLabel, 1)
        topLeftLayout.addLayout(lcdLayout)
        
        layout = QGridLayout()
        layout.addLayout(topLeftLayout, 0, 0, 1, 1)
        layout.addWidget(self.discardPile, 1, 0, 1, 1)
        layout.addWidget(self.engagedArea, 0, 1, 1, 1)
        layout.addWidget(self.heroArea, 1, 1, 1, 1)
        layout.setRowStretch(0, 1)
        layout.setColumnStretch(1, 1)
        self.setLayout(layout)


class MultiplayerPanel(QDialog):
    def __init__(self, addresses, nicknames, chatter, parent):
        super(MultiplayerPanel, self).__init__(parent)
        
        self.deckManipulatorList = []  # for bookkeeping existing DeckManipulator instances
        self.addressToPanel = {}
        self.chatter = chatter
        self.createUI(addresses, nicknames)
        
    def addDeckManipulator(self, widget):
        self.deckManipulatorList.append(widget)
        
    def cleanupDeckManipulators(self):
        for widget in self.deckManipulatorList:
            try:
                widget.close()
            except RuntimeError:
                pass
        self.deckManipulatorList = []
        
    def updateState(self, address, field, state):
        self.addressToPanel[address].updateState(field, state)
        
    def getState(self):
        state = {}
        for (address, panel) in self.addressToPanel.items():
            state[address] = panel.getState()
        return state
        
    def setLargeImage(self, card):
        self.parentWidget().setLargeImage(card)
        
    def log(self, message):
        self.parentWidget().log(message)
        
    def keyPressEvent(self, event):
        self.chatter.setFocus()
        super(MultiplayerPanel, self).keyPressEvent(event)
        
    def showEvent(self, event):
        if hasattr(self, 'lastGeometry'):
            self.setGeometry(self.lastGeometry)
        super(MultiplayerPanel, self).showEvent(event)
        self.chatter.setFocus()
        
    def hideEvent(self, event):
        self.setWindowTitle(self.windowTitle)
        self.lastGeometry = self.geometry()
        self.cleanupDeckManipulators()
        super(MultiplayerPanel, self).hideEvent(event)
        
    def closeEvent(self, event):
        self.setWindowTitle(self.windowTitle)
        self.lastGeometry = self.geometry()
        self.cleanupDeckManipulators()
        super(MultiplayerPanel, self).closeEvent(event)
        event.accept()
        
    def resizeEvent(self, event):
        size = QSize(self.parentWidget().width() / 3, self.parentWidget().height() / 3)
        self.setMinimumSize(size)
        self.setMaximumSize(self.parentWidget().size())
        
        playerCount = len(self.addressToPanel)
        for (address, panel) in self.addressToPanel.items():
            panel.setMaximumHeight(self.height() / playerCount)
            panel.resizeEvent(None)
            
    def createUI(self, addresses, nicknames):
        self.chatter.setMinimumWidth(200)
        
        phaseLabel = QLabel(self.tr('Phase:'))
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(phaseLabel)
        
        phaseNames = ('Resource', 'Planning', 'Quest', 'Travel', 'Encounter', 'Combat', 'Refresh')
        maxPhaseNameLength = len(max(phaseNames, key=lambda name: len(name)))
        
        def sendPhase(phaseName):
            def sendPhase_():
                separators = '=' * (maxPhaseNameLength - len(phaseName))
                message = '====={0} {1} Phase ======='.format(separators, phaseName)
                self.parentWidget().client.sendSystemMessage(message)
            return sendPhase_
            
        for name in phaseNames:
            button = QPushButton(name[0])
            button.clicked.connect(sendPhase(name))
            button.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum))
            button.setFocusPolicy(Qt.NoFocus)  # otherwise pressing Enter while chatting will trigger button
            button.setToolTip(name)
            buttonsLayout.addWidget(button)
            
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.chatter, 1)
        leftLayout.addLayout(buttonsLayout)
        
        rightLayout = QVBoxLayout()
        for (address, nickname) in zip(addresses, nicknames):
            panel = _PlayerStatePanel(address, nickname)
            rightLayout.addWidget(panel)
            self.addressToPanel[address] = panel
            
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout, 1)
        self.setLayout(layout)
        self.windowTitle = self.tr('Player States')
        self.setWindowTitle(self.tr('%1  (Press ESC to hide this panel)').arg(self.windowTitle))