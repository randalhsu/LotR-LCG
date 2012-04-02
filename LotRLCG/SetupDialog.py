from common import *


class SetupDialog(QDialog):
    def __init__(self, parent=None):
        super(SetupDialog, self).__init__(parent)
        self.createUI()
        warnIfDecksCorrupted(parent)
        
    def selectedScenarioId(self):
        for (id, button) in enumerate(self.scenarioButtons):
            if button.isChecked():
                return id
            
    def selectedDeckId(self):
        for (id, button) in enumerate(self.deckButtons):
            if button.isChecked():
                return id
                
    def _deckContentToText(self, cardList):
        iconToDisplay = {
            'leadership': 'Leadership',
               'tactics': '   Tactics',
                'spirit': '    Spirit',
                  'lore': '      Lore',
        }
        typeToDisplay = {
                  'ally': 'Ally ',
                 'event': 'Event',
            'attachment': 'Att  ',
        }
        counter = collections.Counter()
        deckSize = len(cardList)
        
        heroes = []
        for (set_, id) in cardList:
            if isHeroCard(set_, id):
                deckSize -= 1
                heroes.append((set_, id))
            else:
                counter['{0} {1}'.format(cardsInfo[set_][id]['icon'], cardsInfo[set_][id]['type'])] += 1
                
        maxHeroNameLength = 0
        for (set_, id) in heroes:
            length = len(cardsInfo[set_][id]['title'])
            if length > maxHeroNameLength:
                maxHeroNameLength = length
                
        text = ''
        for (set_, id) in heroes:
            name = cardsInfo[set_][id]['title']
            spaces = ' ' * (maxHeroNameLength - len(name))
            text += '{0}{1}  ({2})<br>'.format(spaces, name, cardsInfo[set_][id]['icon'].title())
            
        text += '<br>      Deck Size : {0}<br>'.format(deckSize)
        
        for icon in ('leadership', 'tactics', 'spirit', 'lore'):
            for type_ in ('ally', 'event', 'attachment'):
                text += '{0} {1}: {2}<br>'.format(iconToDisplay[icon], typeToDisplay[type_], counter['{0} {1}'.format(icon, type_)])
                
        return '<pre>{0}</pre>'.format(text)
        
    def createUI(self):
        class RadioButton(QRadioButton):
            def enterEvent(self, event):
                self.topLevelWidget().descriptionLabel.setText(self.description)
                
        self.scenarioButtons = []
        self.scenarioGroupBox = QGroupBox(QCoreApplication.translate('QObject', 'Scenario:'))
        scenarioLayout = QGridLayout()
        scenarioNames = [scenario['icon'] for scenario in scenariosInfo]
        
        for (i, scenario) in enumerate(scenariosInfo):
            button = RadioButton(scenario['name'])
            button.description = '{0}\nDifficulty = {1}\n\n{2}'.format(scenario['name'], scenario['difficulty'], scenario['description'])
            if i == 0:
                button.setChecked(True)
            button.setIcon(QIcon(QPixmap('./resource/image/icon/{0}.png'.format(scenarioNames[i]))))
            scenarioLayout.addWidget(button, i % 10, i // 10, 1, 1)  # 10 buttons in a column
            if i % 10 == 9:
                scenarioLayout.addWidget(QLabel())
            self.scenarioButtons.append(button)
            if CARD_TASTE and (i >= 7 and i != 9):
                button.hide()
        scenarioLayout.setRowStretch(10, 1)
        self.scenarioGroupBox.setLayout(scenarioLayout)
        self.scenarioGroupBox.leaveEvent = lambda _: self.descriptionLabel.setText(self.scenarioButtons[self.selectedScenarioId()].description)
        
        self.deckButtons = []
        decksGroupBox = QGroupBox(QCoreApplication.translate('QObject', 'Player Deck:'))
        decksLayout = QVBoxLayout()
        for (i, deck) in enumerate(playerDecksInfo):
            button = RadioButton(deck['name'])
            button.description = self._deckContentToText(deck['deck'])
            if i == 0:
                button.setChecked(True)
            decksLayout.addWidget(button)
            self.deckButtons.append(button)
        decksLayout.addStretch(1)
        decksGroupBox.setLayout(decksLayout)
        decksGroupBox.leaveEvent = lambda _: self.descriptionLabel.setText(self.deckButtons[self.selectedDeckId()].description)
        
        descriptionGroupBox = QGroupBox(QCoreApplication.translate('QObject', 'Description:'))
        self.descriptionLabel = QLabel(self.scenarioButtons[0].description)
        self.descriptionLabel.setMinimumWidth(200)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        littleLayout = QVBoxLayout()
        littleLayout.addWidget(self.descriptionLabel)
        descriptionGroupBox.setLayout(littleLayout)
        self.startButton = QPushButton(QCoreApplication.translate('QObject', 'Start!'))
        self.startButton.clicked.connect(self.accept)
        
        midLayout = QVBoxLayout()
        midLayout.addWidget(descriptionGroupBox)
        midLayout.addWidget(self.startButton)
        
        layout = QHBoxLayout()
        layout.addWidget(self.scenarioGroupBox)
        layout.addLayout(midLayout)
        layout.addWidget(decksGroupBox)
        self.setLayout(layout)
        self.setWindowTitle(QCoreApplication.translate('QObject', 'Setting Game'))


class ClientSetupDialog(SetupDialog):
    def __init__(self, parent=None):
        super(ClientSetupDialog, self).__init__(parent)
        self.scenarioGroupBox.hide()
        self.descriptionLabel.setText(self.deckButtons[0].description)
        self.startButton.setText(QCoreApplication.translate('QObject', 'Ready!'))
        
    def selectedScenarioId(self):
        return -1
