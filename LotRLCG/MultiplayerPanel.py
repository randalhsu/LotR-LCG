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
            self.handSizeLabel.setText(str(state))
        elif field == 'player':
            self.deckSizeLabel.setText(str(state))
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
        self.discardPile.setFixedWidth(width)
        self.threatValue.setFixedWidth(width)
        self.threatValue.setMinimumHeight(width * 2 / 5)
        self.threatValue.setMaximumHeight(width * 3 / 5)
        
    def createUI(self):
        text = '<h3>{0}</h3>'.format(self.nickname)
        nicknameLabel = QLabel(text)
        handLabel = QLabel(self.tr('Hand:'))
        self.handSizeLabel = QLabel('0')
        deckLabel = QLabel(self.tr('Deck:'))
        self.deckSizeLabel = QLabel('0')
        
        palette = QPalette()
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
        self.discardPile = Deck('Player Discard Pile')
        self.discardPile.setBackgroundBrush(QBrush(Qt.darkYellow))
        
        labelsLayout = QGridLayout()
        labelsLayout.addWidget(handLabel, 0, 0, 1, 1)
        labelsLayout.addWidget(self.handSizeLabel, 0, 1, 1, 1)
        labelsLayout.addWidget(deckLabel, 1, 0, 1, 1)
        labelsLayout.addWidget(self.deckSizeLabel, 1, 1, 1, 1)
        
        topLeftLayout = QVBoxLayout()
        topLeftLayout.addWidget(nicknameLabel)
        topLeftLayout.addStretch(1)
        topLeftLayout.addLayout(labelsLayout)
        topLeftLayout.addWidget(self.threatValue)
        
        layout = QGridLayout()
        layout.addLayout(topLeftLayout, 0, 0, 1, 1)
        layout.addWidget(self.discardPile, 1, 0, 1, 1)
        layout.addWidget(self.engagedArea, 0, 1, 1, 1)
        layout.addWidget(self.heroArea, 1, 1, 1, 1)
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
            
    def createUI(self, addresses, nicknames):
        rightLayout = QVBoxLayout()
        for (address, nickname) in zip(addresses, nicknames):
            panel = _PlayerStatePanel(address, nickname)
            rightLayout.addWidget(panel)
            self.addressToPanel[address] = panel
            
        self.chatter.setMinimumWidth(200)
        layout = QHBoxLayout()
        layout.addWidget(self.chatter)
        layout.addLayout(rightLayout, 1)
        self.setLayout(layout)
        self.windowTitle = self.tr('Player States')
        self.setWindowTitle(self.windowTitle + '  (Press ESC to hide this panel)')