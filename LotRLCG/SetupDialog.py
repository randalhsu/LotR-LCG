from common import *


class SetupDialog(QDialog):
    def __init__(self, parent=None):
        super(SetupDialog, self).__init__(parent)
        
        class RadioButton(QRadioButton):
            def enterEvent(self, event):
                self.topLevelWidget().descriptionLabel.setText(self.description)
        
        def deckContentToText(cardList):
            counter = collections.Counter()
            for (set_, id) in cardList:
                counter[cardsInfo[set_][id]['title']] += 1
            text = ''
            for card in counter:
                text += '{0}x  {1}\n'.format(counter[card], card)
            return text
            
        self.scenarioButtons = []
        self.scenarioGroupBox = QGroupBox(self.tr('Scenario:'))
        scenarioLayout = QVBoxLayout()
        scenarioNames = [scenario['icon'] for scenario in scenariosInfo]
        
        for (i, scenario) in enumerate(scenariosInfo):
            button = RadioButton(scenario['name'])
            button.description = '{0}\nDifficulty = {1}\n\n{2}'.format(scenario['name'], scenario['difficulty'], scenario['description'])
            if i == 0:
                button.setChecked(True)
            button.setIcon(QIcon(QPixmap('./resource/image/icon/{0}.png'.format(scenarioNames[i]))))
            scenarioLayout.addWidget(button)
            self.scenarioButtons.append(button)
            if CARD_TASTE and (i >= 6 and i != 9):
                button.hide()
        scenarioLayout.addStretch(1)
        self.scenarioGroupBox.setLayout(scenarioLayout)
        self.scenarioGroupBox.leaveEvent = lambda _: self.descriptionLabel.setText(self.scenarioButtons[self.selectedScenarioId()].description)
        
        self.deckButtons = []
        decksGroupBox = QGroupBox(self.tr('Player Deck:'))
        decksLayout = QVBoxLayout()
        for (i, deck) in enumerate(playerDecksInfo):
            button = RadioButton(deck['name'])
            button.description = deckContentToText(deck['deck'])
            if i == 0:
                button.setChecked(True)
            decksLayout.addWidget(button)
            self.deckButtons.append(button)
        decksLayout.addStretch(1)
        decksGroupBox.setLayout(decksLayout)
        decksGroupBox.leaveEvent = lambda _: self.descriptionLabel.setText(self.deckButtons[self.selectedDeckId()].description)
        
        descriptionGroupBox = QGroupBox(self.tr('Description:'))
        self.descriptionLabel = QLabel(self.scenarioButtons[0].description)
        self.descriptionLabel.setMinimumWidth(200)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        littleLayout = QVBoxLayout()
        littleLayout.addWidget(self.descriptionLabel)
        descriptionGroupBox.setLayout(littleLayout)
        self.startButton = QPushButton(self.tr('Start!'))
        self.startButton.clicked.connect(self.accept)
        
        midLayout = QVBoxLayout()
        midLayout.addWidget(descriptionGroupBox)
        midLayout.addWidget(self.startButton)
        
        layout = QHBoxLayout()
        layout.addWidget(self.scenarioGroupBox)
        layout.addLayout(midLayout)
        layout.addWidget(decksGroupBox)
        self.setLayout(layout)
        self.setWindowTitle(self.tr('Setting Game'))
        
        warnIfDecksCorrupted()
        
    def selectedScenarioId(self):
        for (id, button) in enumerate(self.scenarioButtons):
            if button.isChecked():
                return id
            
    def selectedDeckId(self):
        for (id, button) in enumerate(self.deckButtons):
            if button.isChecked():
                return id


class ClientSetupDialog(SetupDialog):
    def __init__(self, parent=None):
        super(ClientSetupDialog, self).__init__(parent)
        self.scenarioGroupBox.hide()
        self.descriptionLabel.setText(self.deckButtons[0].description)
        self.startButton.setText(self.tr('Ready!'))
        
    def selectedScenarioId(self):
        return -1
