from common import *


class SetupDialog(QDialog):
    def __init__(self, parent=None):
        super(SetupDialog, self).__init__(parent)
        self.createUI()
        warnIfDecksCorrupted(parent)
        
    def selectedScenarioId(self):
        for button in self.scenarioButtons:
            if button.isChecked():
                return button.scenarioId
                
    def selectedDeckId(self):
        for (id, button) in enumerate(self.deckButtons):
            if button.isChecked():
                return id
                
    def _deckContentToText(self, cardList):
        sphereColor = {
            'neutral': '969696',
            'leadership': '9d489b',
            'tactics': 'b71f25',
            'spirit': '00b6e3',
            'lore': '00a651',
        }
        alignedSphere = {
               'neutral': '   Neutral',
            'leadership': 'Leadership',
               'tactics': '   Tactics',
                'spirit': '    Spirit',
                  'lore': '      Lore',
        }
        alignedType = {
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
            sphere = cardsInfo[set_][id]['icon']
            text += '<font color="#{0}">{1}{2}  ({3})</font><br>'.format(sphereColor[sphere], spaces, name, sphere.title())
            
        text += '<br>      Deck Size = {0}<br>'.format(deckSize)
        
        for sphere in ('neutral', 'leadership', 'tactics', 'spirit', 'lore'):
            for type_ in ('ally', 'event', 'attachment'):
                quantity = counter['{0} {1}'.format(sphere, type_)]
                if quantity > 0:
                    text += '<font color="#{0}">{1} {2}: {3:2}</font><br>'.format(sphereColor[sphere], alignedSphere[sphere], alignedType[type_], quantity)
                    
        return '<pre>{0}</pre>'.format(text)
        
    def createUI(self):
        class RadioButton(QRadioButton):
            def enterEvent(self, event):
                self.topLevelWidget().descriptionLabel.setText(self.description)
                
        self.scenarioButtons = []
        self.scenarioGroupBox = QGroupBox(QCoreApplication.translate('SetupDialog', 'Scenario:'))
        scenarioLayout = QGridLayout()
        scenarioNames = [scenario['icon'] for scenario in scenariosInfo]
        
        testCases = (('core', 119), ('core', 126), ('core', 123), ('mirkwood', 11), ('mirkwood', 35), ('mirkwood', 60), ('mirkwood', 82), ('mirkwood', 105), ('mirkwood', 126), ('osgiliath', 16), ('khazaddum', 64), ('khazaddum', 67), ('khazaddum', 69), ('dwarrowdelf', 11), ('dwarrowdelf', 38))
        scenarioExists = [QFile(':/{0}/{1}.jpg'.format(set_, id)).exists() for (set_, id) in testCases]
        
        for (i, scenario) in enumerate(scenariosInfo):
            if not scenarioExists[i]:
                continue
            n = len(self.scenarioButtons)
            button = RadioButton(scenario['name'])
            button.description = '<h3>{0}</b></h3>Difficulty = {1}<hr>{2}'.format(scenario['name'], scenario['difficulty'], scenario['description'])
            if n == 0:
                button.setChecked(True)
            button.setIcon(QIcon(QPixmap(':/images/icons/{0}.png'.format(scenarioNames[i]))))
            scenarioLayout.addWidget(button, n % 10, n // 10, 1, 1)  # 10 buttons in a column
            if n % 10 == 9:
                scenarioLayout.addWidget(QLabel())
            self.scenarioButtons.append(button)
            button.scenarioId = i
        scenarioLayout.setRowStretch(10, 1)
        self.scenarioGroupBox.setLayout(scenarioLayout)
        
        def setScenarioText(event):
            n = self.selectedScenarioId()
            shift = 0
            for i in range(n):
                if not scenarioExists[i]:
                    shift += 1
            self.descriptionLabel.setText(self.scenarioButtons[n - shift].description)
        self.scenarioGroupBox.leaveEvent = setScenarioText
        
        self.deckButtons = []
        decksGroupBox = QGroupBox(QCoreApplication.translate('SetupDialog', 'Player Deck:'))
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
        
        descriptionGroupBox = QGroupBox(QCoreApplication.translate('SetupDialog', 'Description:'))
        self.descriptionLabel = QLabel(self.scenarioButtons[0].description)
        self.descriptionLabel.setMinimumWidth(200)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        littleLayout = QVBoxLayout()
        littleLayout.addWidget(self.descriptionLabel)
        descriptionGroupBox.setLayout(littleLayout)
        self.startButton = QPushButton(QCoreApplication.translate('SetupDialog', 'Start!'))
        self.startButton.clicked.connect(self.accept)
        
        midLayout = QVBoxLayout()
        midLayout.addWidget(descriptionGroupBox)
        midLayout.addWidget(self.startButton)
        
        layout = QHBoxLayout()
        layout.addWidget(self.scenarioGroupBox)
        layout.addLayout(midLayout)
        layout.addWidget(decksGroupBox)
        self.setLayout(layout)
        self.setWindowTitle(QCoreApplication.translate('SetupDialog', 'Setting Game'))


class ClientSetupDialog(SetupDialog):
    def __init__(self, parent=None):
        super(ClientSetupDialog, self).__init__(parent)
        self.scenarioGroupBox.hide()
        self.descriptionLabel.setText(self.deckButtons[0].description)
        self.startButton.setText(QCoreApplication.translate('SetupDialog', 'Ready!'))
        
    def selectedScenarioId(self):
        return -1