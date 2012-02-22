from CardsTileView import *


class DeckManipulator(QDialog):
    def __init__(self, deck, parent):
        super(DeckManipulator, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        parent.addDeckManipulator(self)
        self.parent = parent
        
        self.name = deck.name
        self.deck = deck
        self.tileView = CardsTileView(self.deck, parent, self)
        self.createUI()
        
    def revealAll(self):
        for card in self.tileView.getList():
            if self.name == 'Quest Deck':
                if card.revealed():
                    card.flip()
            else:
                if not card.revealed():
                    card.flip()
        self.tileView.update()
        
    def coverAll(self):
        for card in self.tileView.getList():
            if self.name == 'Quest Deck':
                if not card.revealed():
                    card.flip()
            else:
                if card.revealed():
                    card.flip()
        self.tileView.update()
        
    def clearStateLabel(self):
        self.stateLabel.setText('')
        
    def setStateLabel(self, text):
        self.stateLabel.setText(text)
        QTimer.singleShot(2000, self.clearStateLabel)
        
    def shuffle(self):
        self.tileView.shuffle()
        self.setStateLabel(self.tr('Shuffled!'))
        
    def moveToEncounterDeck(self):
        encounterDeck = self.parent.encounterDeck
        while self.tileView.getList():
            encounterDeck.addCard(self.tileView.draw())
        for textItem in self.tileView.scene.items():
            self.tileView.scene.removeItem(textItem)
        self.setStateLabel(self.tr('Cards moved'))
        
    def setLargeImage(self, card):
        self.parent.setLargeImage(card)
        
    def createUI(self):
        self.setMaximumWidth(500)
        revealAllButton = QPushButton(self.tr('&Reveal All'))
        coverAllButton = QPushButton(self.tr('Co&ver All'))
        self.stateLabel = QLabel()
        shuffleButton = QPushButton(self.tr('&Shuffle'))
        closeButton = QPushButton(self.tr('&Close'))
        
        revealAllButton.clicked.connect(self.revealAll)
        coverAllButton.clicked.connect(self.coverAll)
        shuffleButton.clicked.connect(self.shuffle)
        closeButton.clicked.connect(self.close)
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(revealAllButton)
        topLayout.addWidget(coverAllButton)
        topLayout.addStretch(1)
        topLayout.addWidget(self.stateLabel)
        topLayout.addWidget(shuffleButton)
        
        bottomLayout = QHBoxLayout()
        if self.deck.name == 'Encounter Discard Pile':
            moveButton = QPushButton(self.tr('Move to &Encounter Deck'))
            moveButton.clicked.connect(self.moveToEncounterDeck)
            bottomLayout.addWidget(moveButton)
        bottomLayout.addStretch(1)
        bottomLayout.addWidget(closeButton)
        
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(self.tileView)
        layout.addLayout(bottomLayout)
        self.setLayout(layout)
        self.setWindowTitle(self.name.replace(' ', '\n'))
        
    def closeEvent(self, event):
        cardList = [card for card in self.tileView.cardList if isinstance(card, Card)]
        cardList.reverse()
        for card in cardList:
            self.tileView.removeCard(card)
            self.deck.addCard(card)
        event.accept()