import glob
import re
from common import *
import cards


CARD_FIELDS = ('set', 'id', 'title', 'type', 'icon', 'cost', 'strength', 'attack', 'defense', 'hp', 'traits', 'effect')
EFFECT_TYPES = ('normal', 'travel', 'action', 'quest action', 'combat action', 'when revealed', 'forced', 'response', 'shadow')
TABLE_HEADER = ('Qty', 'Set', 'ID', 'Title', 'Type', 'Icon', 'Cost', 'WP', 'ATK', 'DEF', 'HP', 'Traits', 'Description')

# EXPANSION
setShort = {'core': 'core', 'mirkwood': 'mirk', 'osgiliath': 'osgi', 'khazaddum': 'khaz', 'dwarrowdelf': 'dwar'}  # for saving column space. max len == 4
setFull = {
    'core': 'core',
    'mirk': 'mirkwood',
    'mirkwood': 'mirkwood',
    'osgi': 'osgiliath',
    'osgiliath': 'osgiliath',
    'khaz': 'khazaddum',
    'khazaddum': 'khazaddum',
    'dwar': 'dwarrowdelf',
    'dwarrowdelf': 'dwarrowdelf',
}


icons = {'neutral': QIcon()}  # this will contain all  name: QIcon instance

def getIcon(name):
    global icons
    if name in icons:
        return icons[name]
        
    icon = QIcon(':/images/icons/{0}.png'.format(name))
    icons[name] = icon
    return icon


class TableWidget(QTableWidget):
    HEADER = ('Set', 'ID', 'Title', 'Type', 'Sph', 'Cost', 'WP', 'ATK', 'DEF', 'HP', 'Traits', 'Description')
    
    def __init__(self, row=0, col=0, parent=None):
        super(TableWidget, self).__init__(row, col, parent)
        self.setMouseTracking(True)
        self.setAlternatingRowColors(True)
        self.verticalHeader().hide()
        self.setColumnCount(len(self.HEADER))  # different HEADER for different subclasses
        
        for (col, text) in enumerate(self.HEADER):
            item = None
            if text in ('Threat', 'WP', 'ATK', 'DEF'):
                item = QTableWidgetItem(QIcon(':/images/icons/{0}.png'.format(text)), '')
            else:
                item = QTableWidgetItem(text)
            self.setHorizontalHeaderItem(col, item)
            
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
    def rowToCard(self, row):
        set_ = str(self.item(row, self.HEADER.index('Set')).data(Qt.DisplayRole).toString())
        set_ = setFull[set_]
        id = self.item(row, self.HEADER.index('ID')).data(Qt.DisplayRole).toInt()[0]
        return (set_, id)
        
    def selectedCard(self):
        row = self.currentIndex().row()
        if row == -1:
            return None
        #return self.rowToCard(row)
        return self.item(row, 0).card
        
    def mouseMoveEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            self.window().setLargeImage(item.card)
            
    def leaveEvent(self, event):
        if self.currentItem():
            self.window().setLargeImage(self.currentItem().card)
            
    def focusOutEvent(self, event):
        pass  # reimplementing this method makes the selected row still highlighted


class DeckTableWidget(TableWidget):
    HEADER = ('Qty', 'Set', 'ID', 'Title', 'Type', 'Sph', 'Cost', 'WP', 'ATK', 'DEF', 'HP', 'Traits', 'Description')
    
    def currentQuantity(self):
        row = self.currentIndex().row()
        if row == -1:
            return None
        return self.item(row, 0).data(Qt.DisplayRole).toInt()[0]


class EncounterTableWidget(TableWidget):
    HEADER = ('Set', 'ID', 'Qty', 'Title', 'Type', 'Icon', 'Thld', 'Threat', 'ATK', 'DEF', 'HP', 'Traits', 'Description')


class SetItem(QTableWidgetItem):
    def __init__(self, text):
        text = setShort[text]
        super(SetItem, self).__init__(text)
        
    def __lt__(self, rhs):
        (set_, id) = self.card
        (rhsSet, rhsId) = rhs.card
        if set_ != rhsSet:
            return SETS.index(set_) < SETS.index(rhsSet)
        return id < rhsId


class TypeItem(QTableWidgetItem):
    PLAYERS = ('Hero', 'Ally', 'Event', 'Att.')  # <
    ENCOUNTERS = ('Objective', 'Enemy', 'Location', 'Treachery', 'Quest')
    
    def __lt__(self, rhs):
        value = str(self.data(Qt.DisplayRole).toString())
        rhsValue = str(rhs.data(Qt.DisplayRole).toString())
        if value in TypeItem.PLAYERS:
            return TypeItem.PLAYERS.index(value) < TypeItem.PLAYERS.index(rhsValue)
        else:
            return TypeItem.ENCOUNTERS.index(value) < TypeItem.ENCOUNTERS.index(rhsValue)


class IconItem(QTableWidgetItem):
    PLAYERS = ('neutral', 'leadership', 'tactics', 'spirit', 'lore')
    ENCOUNTERS = ('spiders', 'wilderlands', 'orcs', 'passage', 'escape', 'anduin', 'sauron', 'gollum', 'carrock', 'rhosgobel', 'emynmuil', 'marshes', 'return', 'osgiliath', 'pit', 'seventh', 'flight', 'plundering', 'twists', 'moria', 'hazards', 'misty', 'goblin', 'redhorn')  # EXPANSION
    
    def __init__(self, iconName):
        text = 'N' if iconName == 'neutral' else ''
        super(IconItem, self).__init__(getIcon(iconName), text)
        self.name = iconName
        
    def __lt__(self, rhs):
        if self.name in self.PLAYERS:
            return IconItem.PLAYERS.index(self.name) < IconItem.PLAYERS.index(rhs.name)
        return IconItem.ENCOUNTERS.index(self.name) < IconItem.ENCOUNTERS.index(rhs.name)


class NumericItem(QTableWidgetItem):
    def __lt__(self, rhs):
        '''empty string < numbers < X'''
        (value, ok) = self.data(Qt.DisplayRole).toInt()
        if not ok:  # conversion failed
            if not str(self.data(Qt.DisplayRole).toString()):
                return True  # empty string is smallest
            return False  # X is largest
            
        (rhsValue, ok) = rhs.data(Qt.DisplayRole).toInt()
        if not ok:
            if not str(rhs.data(Qt.DisplayRole).toString()):
                return False
            return True
        
        return value < rhsValue
        # TODO: nobody cares empty string


class DeckBuilder(QMainWindow):
    def __init__(self, parent=None):
        super(DeckBuilder, self).__init__(parent)
        self.imageDict = {}  # this will contain all  (set_, id): QPixmap instance
        
        self.decks = playerDecksInfo
        self.currentDeck = collections.Counter()
        self.dirty = False  # are there unsaved changes?
        self.currentTab = 0  # 0: player cards, 1: encounter cards
        self.createUI()
        
        self.timer = QTimer()  # for clearing state label automatically
        self.timer.setSingleShot(True)
        self.timer.setInterval(6000)
        self.timer.timeout.connect(self.clearStateLabel)
        
        warnIfDecksCorrupted(self)
        
        QTimer.singleShot(0, self.loadPlayerCards)
        
    def loadPlayerCards(self):
        self.loadCards('player')
        
    def loadEncounterCards(self):
        self.loadCards('encounter')
        
    def loadCards(self, type_):
        assert(type_ in ('player', 'encounter'))  # split loading into two types, in order to speed up program startup time
        translations = {
            'player': self.tr('player'),
            'encounter': self.tr('encounter'),
        }
        
        self.setCursor(Qt.WaitCursor)
        self.loadingLabel.setText(self.tr('Loading %1 card images...').arg(translations[type_]))
        QApplication.processEvents()  # force visual label text update
        
        for set_ in SETS:
            for i in range(200):
                id = i + 1
                if QFile(':/{0}/{1}.jpg'.format(set_, id)).exists():
                    if (type_ == 'player' and isPlayerCard(set_, id)) or (type_ == 'encounter' and isEncounterCard(set_, id)):
                        pixmap = getCardPixmap(':/{0}/{1}.jpg'.format(set_, id))
                        self.imageDict[(set_, id)] = pixmap
                else:
                    break
                    
        # patch the fucked up Dwarrowdelf No.76
        if QFile(':/dwarrowdelf/0.jpg').exists():
            pixmap = getCardPixmap(':/dwarrowdelf/0.jpg')
            self.imageDict[('dwarrowdelf', 0)] = pixmap
            
        self.loadingLabel.setText('')
        self.setCursor(Qt.ArrowCursor)
        
    def setLargeImage(self, (set_, id)):
        if self.largeImageLabel.currentCard != (set_, id):
            try:
                # patch the fucked up Dwarrowdelf No.76
                if (set_, id) == ('dwarrowdelf', 76) and self.currentTab == 1:
                    self.largeImageLabel.setPixmap(self.imageDict[('dwarrowdelf', 0)])
                else:
                    self.largeImageLabel.setPixmap(self.imageDict[(set_, id)])
                self.largeImageLabel.currentCard = (set_, id)
            except KeyError:  # occurs right after program startup but before images are loaded
                pass
                
    def clearStateLabel(self):
        self.stateLabel.setText('')
        
    def setStateLabel(self, text):
        self.timer.stop()
        self.stateLabel.setText(text)
        self.timer.start()
        
    def convertEffectText(self, effect):
        text = ''
        if 'A' in effect:  # quest card
            for side in ('A', 'B'):
                for type_ in EFFECT_TYPES:  # ensure orders
                    if type_ in effect[side]:
                        if type_ != 'normal':
                            text += type_.title() + ': '
                        text += effect[side][type_] + ' '
        for type_ in EFFECT_TYPES:  # ensure orders
            if type_ in effect:
                if type_ != 'normal':
                    text += type_.title() + ': '
                text += effect[type_] + ' '
        return text
        
    def createTableItem(self, set_, id, field):
        
        def titlecase(s):
            return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)
        
        set_ = setFull[set_]
        
        try:
            value = cardsInfo[set_][id][field]
            if field == 'quantity':
                if isPlayerCard(set_, id):
                    value = self.currentDeck[(set_, id)]
                else:
                    value = cardsInfo[set_][id]['quantity']
            elif field in ('title', 'type'):
                if value == 'attachment':
                    value = 'Att.'
                else:
                    value = titlecase(value)
            elif field in ('cost', 'strength', 'attack', 'defense', 'hp'):
                if value == -1:
                    value = 'X'
            elif field == 'traits':
                value = '. '.join(value) + '.'
            elif field == 'effect':
                value = self.convertEffectText(value)
        except KeyError:
            value = ''
            
        if isinstance(value, int) or field in ('quantity', 'id', 'cost', 'strength', 'attack', 'defense', 'hp'):
            # patch the fucked up Dwarrowdelf No.76
            if (set_, id) == ('dwarrowdelf', 0) and field == 'id':
                value = 76
                
            item = NumericItem(str(value))
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            if field == 'quantity':
                item.setForeground(QBrush(QColor(Qt.red)))
        elif field == 'set':
            item = SetItem(value)
        elif field == 'type':
            item = TypeItem(value)
        elif field == 'icon':
            item = IconItem(value)
        else:
            item = QTableWidgetItem(value)
            
        #item.setSizeHint(QSize(0, 12))
        item.card = (set_, id)  # append this info for convenience
        
        # patch the fucked up Dwarrowdelf No.76
        if (set_, id) == ('dwarrowdelf', 0):
            item.card = ('dwarrowdelf', 76)
            
        return item
        
    def updateDeckTable(self):
        self.deckTable.clearContents()
        if self.deckComboBox.currentIndex() == -1:
            self.currentDeck = collections.Counter()
            self.updateSizeLabel()
            return
            
        self.deckTable.setSortingEnabled(False)
        deck = self.decks[self.deckComboBox.currentIndex()]['deck']
        self.currentDeck = collections.Counter()
        for card in deck:
            self.currentDeck[tuple(card)] += 1
        self.updateSizeLabel()
        
        self.deckTable.setRowCount(len(self.currentDeck))
        
        for (row, (set_, id)) in enumerate(self.currentDeck):
            for (col, field) in enumerate(['quantity'] + list(CARD_FIELDS)):
                item = self.createTableItem(set_, id, field)
                self.deckTable.setItem(row, col, item)
                
        self.adjustTableWidget(self.deckTable)
        
    def createPlayerCardsTable(self):
        playerCards = []
        for set_ in SETS:
            for (id, card) in enumerate(cardsInfo[set_]):
                if isPlayerCard(set_, id):
                    if QFile(':/{0}/{1}.jpg'.format(set_, id)).exists():
                        playerCards.append((set_, id))
                        
        tableWidget = TableWidget(len(playerCards), 0, self)
        
        for (row, (set_, id)) in enumerate(playerCards):
            for (col, field) in enumerate(CARD_FIELDS):
                item = self.createTableItem(set_, id, field)
                tableWidget.setItem(row, col, item)
        
        tableWidget.sortByColumn(tableWidget.HEADER.index('Set'), Qt.AscendingOrder)
        self.adjustTableWidget(tableWidget)
        # save some column space...
        width = tableWidget.columnWidth(tableWidget.HEADER.index('Title')) * 0.6
        tableWidget.setColumnWidth(tableWidget.HEADER.index('Title'), width)
        return tableWidget
        
    def createEncounterCardsTable(self):
        encounterCards = []
        for set_ in SETS:
            for (id, card) in enumerate(cardsInfo[set_]):
                # patch the fucked up Dwarrowdelf No.76
                if (set_, id) == ('dwarrowdelf', 0):
                    continue
                    
                if isEncounterCard(set_, id):
                    if QFile(':/{0}/{1}.jpg'.format(set_, id)).exists():
                        encounterCards.append((set_, id))
                        
                # patch the fucked up Dwarrowdelf No.76
                if (set_, id) == ('dwarrowdelf', 75):
                    if QFile(':/dwarrowdelf/0.jpg').exists():
                        encounterCards.append(('dwarrowdelf', 76))
                        
        tableWidget = EncounterTableWidget(len(encounterCards), 0, self)
        
        for (row, (set_, id)) in enumerate(encounterCards):
            for (col, field) in enumerate(['set', 'id', 'quantity'] + list(CARD_FIELDS[2:])):
                # patch the fucked up Dwarrowdelf No.76
                if (set_, id) == ('dwarrowdelf', 76):
                    id = 0
                    
                item = self.createTableItem(set_, id, field)
                tableWidget.setItem(row, col, item)
        
        self.adjustTableWidget(tableWidget)
        tableWidget.sortByColumn(tableWidget.HEADER.index('Set'), Qt.AscendingOrder)
        return tableWidget
        
    def adjustTableWidget(self, tableWidget):
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()
        tableWidget.setSortingEnabled(True)
        tableWidget.resizeRowsToContents()  # it's not working properly...
        
    def currentDeckSize(self):
        size = 0
        for card in self.currentDeck:
            (set_, id) = card
            if not isHeroCard(set_, id):
                size += self.currentDeck[card]
        return size
        
    def updateSizeLabel(self):
        dirtyMark = ' (*)' if self.dirty else ''
        self.sizeLabel.setText(QString('%1: %2%3').arg(self.tr('Size')).arg(self.currentDeckSize()).arg(dirtyMark))
        
    def makeRedFont(self, text):
        return QString('<font color="red">%1</font>').arg(text)
        
    def addToDeck(self):
        idx = self.deckComboBox.currentIndex()
        if idx == -1:
            self.setStateLabel(self.makeRedFont(self.tr('No deck. Try to Add New Deck first')))
            return
            
        card = self.playerCardsTable.selectedCard()
        if not card:
            self.setStateLabel(self.makeRedFont(self.tr('Nothing selected...')))
            return
            
        (set_, id) = card
        
        if isHeroCard(set_, id):
            if self.currentDeck[card] >= 1:
                self.setStateLabel(self.makeRedFont(self.tr('Error: Hero already in deck')))
                return
            
            heroCount = 0
            for (set__, id_) in self.currentDeck:
                if isHeroCard(set__, id_) and self.currentDeck[(set__, id_)] >= 1:
                    heroCount += 1
            if heroCount >= 3:
                self.setStateLabel(self.makeRedFont(self.tr('Error: Max = 3 Heroes')))
                return
                
        if self.currentDeck[card] >= 3:
            self.setStateLabel(self.makeRedFont(self.tr('Error: Max = 3 copies of any card')))
            return
            
        self.currentDeck[card] += 1
        self.decks[idx]['deck'].append(list(card))
        self.dirty = True
        
        for row in range(self.deckTable.rowCount()):
            if (set_, id) == self.deckTable.rowToCard(row):
                item = self.deckTable.item(row, TABLE_HEADER.index('Qty'))
                item.setText(str(self.currentDeck[card]))
                self.deckTable.setCurrentItem(item)
                self.deckTable.scrollToItem(item)
                self.setStateLabel('{0} = {1}'.format(cardsInfo[set_][id]['title'], self.currentDeck[card]))
                break
        else:  # card not in deck yet
            self.deckTable.setSortingEnabled(False)  # I debugged this shit for 2 hrs. Should have RTFD carefully
            row = self.deckTable.rowCount()
            self.deckTable.insertRow(row)
            for (col, field) in enumerate(['quantity'] + list(CARD_FIELDS)):
                item = self.createTableItem(set_, id, field)
                self.deckTable.setItem(row, col, item)
                if col == 0:
                    self.deckTable.setCurrentItem(item)
                    self.deckTable.scrollToItem(item)
            self.deckTable.setSortingEnabled(True)
            #self.deckTable.resizeColumnsToContents()
            self.setStateLabel(self.tr('%1 joined the deck!').arg(cardsInfo[setFull[set_]][id]['title']))
            
        # TODO: highlight deckTable's current row
        # ISSUE: adding a card to empty deck cause strange colspan
        self.updateSizeLabel()
        
    def removeFromDeck(self):
        idx = self.deckComboBox.currentIndex()
        if idx == -1:
            self.setStateLabel(self.makeRedFont(self.tr('No deck. Try to Add New Deck first.')))
            return
            
        card = self.deckTable.selectedCard()
        if not card:
            self.setStateLabel(self.makeRedFont(self.tr('Nothing selected...')))
            return
            
        (set_, id) = card
        self.currentDeck[card] -= 1
        self.decks[idx]['deck'].remove(list(card))
        self.dirty = True
        
        row = self.deckTable.currentIndex().row()
        if self.deckTable.currentQuantity() > 1:
            self.deckTable.item(row, 0).setText(str(self.currentDeck[card]))
            self.setStateLabel('{0} = {1}'.format(cardsInfo[set_][id]['title'], self.currentDeck[card]))
        else:
            self.deckTable.removeRow(row)
            self.setStateLabel(self.tr('%1 has gone...').arg(cardsInfo[set_][id]['title']))
            #self.deckTable.setCurrentItem(None)
        self.updateSizeLabel()
        
    def addNewDeck(self):
        (deckName, ok) = QInputDialog.getText(self, self.tr('Add New Deck'), self.tr('Deck Name:'))
        if ok and deckName:
            try:
                deckName = str(deckName)
            except UnicodeEncodeError:
                msgBox = QMessageBox(QMessageBox.Critical, self.tr('ASCII Only'), self.tr('Please use alphanumeric characters'), QMessageBox.Ok, self)
                msgBox.exec_()
                return
                
            if '"' in deckName or '\\' in deckName:  # these characters may break json format
                msgBox = QMessageBox(QMessageBox.Critical, self.tr('Invalid Characters'), self.tr('Invalid characters: " and \\'), QMessageBox.Ok, self)
                msgBox.exec_()
                return
            for deck in self.decks:
                if deckName == deck['name']:
                    msgBox = QMessageBox(QMessageBox.Critical, self.tr('Add New Deck Failed'), self.tr('Deck name occupied!'), QMessageBox.Ok, self)
                    msgBox.exec_()
                    return
                    
            deck = {'name': deckName, 'deck': []}
            self.decks.append(deck)
            self.deckComboBox.addItem(deckName)
            self.deckComboBox.setCurrentIndex(self.deckComboBox.count() - 1)
            self.dirty = True
            self.updateDeckTable()
            self.setStateLabel(self.tr('New deck "%1" added').arg(deckName))
        
    def removeDeck(self):
        idx = self.deckComboBox.currentIndex()
        if idx == -1:
            return
        deckName = self.decks[idx]['name']
        msgBox = QMessageBox(QMessageBox.Warning, self.tr('Remove Deck'), self.tr('Remove "%1"?').arg(deckName), QMessageBox.Ok | QMessageBox.Cancel, self)
        if msgBox.exec_() == QMessageBox.Ok:
            self.decks.pop(idx)
            self.deckComboBox.removeItem(idx)
            self.dirty = True
            self.updateDeckTable()
            self.setStateLabel(self.tr('Deck "%1" removed').arg(deckName))
        
    def duplicateDeck(self):
        idx = self.deckComboBox.currentIndex()
        if idx == -1:
            return
        deckName = self.decks[idx]['name']
        deckName = re.sub(r' (\([0-9]+\))$', '', deckName)  # strip existing suffix
        suffix = 1
        occupiedDeckNames = [deck['name'] for deck in self.decks]
        while '{0} ({1})'.format(deckName, suffix) in occupiedDeckNames:
            suffix += 1
            
        deckName += ' ({0})'.format(suffix)
        deckCards = self.decks[idx]['deck']
        
        newDeck = {'name': deckName, 'deck': deckCards}
        self.decks.append(newDeck)
        self.deckComboBox.addItem(deckName)
        self.deckComboBox.setCurrentIndex(self.deckComboBox.count() - 1)
        self.deckComboBox.update()
        self.dirty = True
        self.updateDeckTable()
        self.setStateLabel(self.tr('Deck "%1" duplicated').arg(deckName))
        
    def updateDeckName(self, deckName):
        self.deckComboBox.setItemText(self.deckComboBox.currentIndex(), deckName)
        allDeckNames = []
        for i in range(self.deckComboBox.count()):
            allDeckNames.append(str(self.deckComboBox.itemText(i)))
            
        for deck in self.decks:
            if deck['name'] not in allDeckNames:
                deck['name'] = str(deckName)
                self.dirty = True
                self.updateSizeLabel()
                self.setStateLabel(self.tr('Deck name changed'))
                return
            
    def save(self):
        with open('decks.json', 'w') as f:
            json.dump(self.decks, f, separators=(',', ':'), indent=2)
            
        info = ''
        if self.currentDeckSize() < 30:
            info = self.makeRedFont(QString('%1<br>').arg(self.tr('Warning: Deck size must be at least 30')))
            
        self.setStateLabel(info + self.tr('Decks saved to "decks.json"!'))
        self.dirty = False
        self.updateSizeLabel()
        
    def filterChanged(self, keyword):
        if keyword.isEmpty():
            for row in range(self.playerCardsTable.rowCount()):
                self.playerCardsTable.setRowHidden(row, False)
            return
            
        for row in range(self.playerCardsTable.rowCount()):
            matched = False
            for col in range(self.playerCardsTable.columnCount()):
                if self.playerCardsTable.item(row, col).text().contains(keyword, Qt.CaseInsensitive):
                    matched = True
                    break
            self.playerCardsTable.setRowHidden(row, not matched)
            
    def encounterFilterChanged(self, keyword):
        if keyword.isEmpty():
            for row in range(self.encounterCardsTable.rowCount()):
                self.encounterCardsTable.setRowHidden(row, False)
            return
            
        if keyword.toLower() == 'victory':
            for row in range(self.encounterCardsTable.rowCount()):
                set_ = setFull[str(self.encounterCardsTable.item(row, 0).text())]
                id = int(self.encounterCardsTable.item(row, 1).text())
                matched = 'victory' in cardsInfo[set_][id]
                for col in range(self.encounterCardsTable.columnCount()):
                    if self.encounterCardsTable.item(row, col).text().contains(keyword, Qt.CaseInsensitive):
                        matched = True
                self.encounterCardsTable.setRowHidden(row, not matched)
            return
            
        for row in range(self.encounterCardsTable.rowCount()):
            matched = False
            for col in range(self.encounterCardsTable.columnCount()):
                if self.encounterCardsTable.item(row, col).text().contains(keyword, Qt.CaseInsensitive):
                    matched = True
                    break
            self.encounterCardsTable.setRowHidden(row, not matched)
        
    def changeTab(self, index_):
        self.currentTab = index_
        self.changeDefaultImage(index_)
        if index_ == 1 and ('core', 74) not in self.imageDict:  # check if Encounter Cards are not loaded yet
            QTimer.singleShot(10, self.loadEncounterCards)
            
    def changeDefaultImage(self, index_):
        if index_ == 0:  # is showing playerTab
            self.largeImageLabel.setPixmap(getCardPixmap(':/images/player_card_back.jpg'))
        else:
            self.largeImageLabel.setPixmap(getCardPixmap(':/images/encounter_card_back.jpg'))
        self.largeImageLabel.currentCard = None
        
    def createUI(self):
        self.largeImageLabel = QLabel()
        self.largeImageLabel.setFixedSize(CARD_WIDTH, CARD_HEIGHT)
        self.largeImageLabel.setPixmap(getCardPixmap(':/images/player_card_back.jpg'))
        self.largeImageLabel.currentCard = None
        
        self.loadingLabel = QLabel()
        infoLabel = QLabel(self.tr('Program written by amulet'))
        
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.largeImageLabel)
        leftLayout.addStretch(1)
        leftLayout.addWidget(self.loadingLabel)
        leftLayout.addWidget(infoLabel)
        
        playerTab = QWidget()
        playerCardsLabel = QLabel(self.tr('Player Cards'))
        filterLabel = QLabel(self.tr('Filter:'))
        filterComboBox = QComboBox()
        filterComboBox.addItems(('', 'Dwarf', 'Eagle', 'Gondor', 'Hobbit', 'Istari', 'Noldor', 'Ranged', 'Rohan', 'Secrecy', 'Sentinel', 'Silvan', 'Song'))
        filterComboBox.setEditable(True)
        filterComboBox.setMaxVisibleItems(100)
        filterComboBox.setMinimumContentsLength(10)
        filterComboBox.editTextChanged.connect(self.filterChanged)
        self.playerCardsTable = self.createPlayerCardsTable()
        
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        addButton = QPushButton(QIcon(QPixmap(':/images/icons/right_arrow.png')), '')
        addButton.setSizePolicy(sizePolicy)
        addButton.clicked.connect(self.addToDeck)
        removeButton = QPushButton(QIcon(QPixmap(':/images/icons/left_arrow.png')), '')
        removeButton.setSizePolicy(sizePolicy)
        removeButton.clicked.connect(self.removeFromDeck)
        
        self.deckComboBox = QComboBox()
        for deck in self.decks:
            self.deckComboBox.addItem(deck['name'])
        self.deckComboBox.setEditable(True)
        self.deckComboBox.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.deckComboBox.currentIndexChanged.connect(self.updateDeckTable)
        self.deckComboBox.editTextChanged.connect(self.updateDeckName)
        
        self.sizeLabel = QLabel()
        addNewDeckButton = QPushButton(self.tr('Add New Deck'))
        addNewDeckButton.clicked.connect(self.addNewDeck)
        removeDeckButton = QPushButton(self.tr('Remove This Deck'))
        removeDeckButton.clicked.connect(self.removeDeck)
        self.deckTable = DeckTableWidget(parent=self)
        self.updateDeckTable()
        self.deckTable.sortByColumn(self.deckTable.HEADER.index('Set'), Qt.AscendingOrder)
        self.stateLabel = QLabel()
        duplicateDeckButton = QPushButton(self.tr('Duplicate This Deck'))
        duplicateDeckButton.clicked.connect(self.duplicateDeck)
        saveDeckButton = QPushButton(self.tr('Save Decks'))
        saveDeckButton.clicked.connect(self.save)
        
        playerLayout = QGridLayout()
        playerLayout.addWidget(playerCardsLabel, 0, 0, 1, 1)
        playerLayout.addWidget(filterLabel, 0, 2, 1, 1, Qt.AlignRight)
        playerLayout.addWidget(filterComboBox, 0, 3, 1, 1)
        playerLayout.addWidget(self.playerCardsTable, 1, 0, 4, 4)
        playerLayout.addWidget(addButton, 2, 4, 1, 1)
        playerLayout.addWidget(removeButton, 3, 4, 1, 1)
        playerLayout.addWidget(self.deckComboBox, 0, 5, 1, 1)
        playerLayout.addWidget(self.sizeLabel, 0, 6, 1, 1)
        playerLayout.addWidget(addNewDeckButton, 0, 7, 1, 1)
        playerLayout.addWidget(removeDeckButton, 0, 8, 1, 1)
        playerLayout.addWidget(self.deckTable, 1, 5, 4, 4)
        playerLayout.addWidget(self.stateLabel, 5, 5, 1, 2)
        playerLayout.addWidget(duplicateDeckButton, 5, 7, 1, 1)
        playerLayout.addWidget(saveDeckButton, 5, 8, 1, 1)
        playerTab.setLayout(playerLayout)
        
        encounterFilterLabel = QLabel(self.tr('Filter:'))
        encounterFilterComboBox = QComboBox()
        encounterFilterComboBox.addItems(('', 'Forced', 'Response', 'Shadow', 'Travel', 'When Revealed', 'Victory'))
        encounterFilterComboBox.insertSeparator(encounterFilterComboBox.count())
        encounterFilterComboBox.addItems(('Ambush', 'Doomed', 'Surge'))
        encounterFilterComboBox.insertSeparator(encounterFilterComboBox.count())
        encounterFilterComboBox.addItems(('Ally', 'Clue', 'Dark', 'Condition', 'Creature', 'Goblin', 'Mountain', 'Orc', 'Scout', 'Snow', 'Tentacle', 'Troll', 'Underground'))
        encounterFilterComboBox.insertSeparator(encounterFilterComboBox.count())
        encounterFilterComboBox.addItems(('Escape', 'Lost'))
        encounterFilterComboBox.insertSeparator(encounterFilterComboBox.count())
        encounterFilterComboBox.addItems(('attachment', 'character', 'deal', 'discard', 'draw', 'exhaust', 'player', 'progress', 'raise', 'ranged', 'resource', 'staging'))
        
        encounterFilterComboBox.setEditable(True)
        encounterFilterComboBox.setMaxVisibleItems(100)
        encounterFilterComboBox.setMinimumContentsLength(10)
        encounterFilterComboBox.editTextChanged.connect(self.encounterFilterChanged)
        encounterFilterLayout = QHBoxLayout()
        encounterFilterLayout.addWidget(encounterFilterLabel)
        encounterFilterLayout.addWidget(encounterFilterComboBox)
        encounterFilterLayout.addStretch(1)
        
        self.encounterCardsTable = self.createEncounterCardsTable()
        encounterLayout = QVBoxLayout()
        encounterLayout.addLayout(encounterFilterLayout)
        encounterLayout.addWidget(self.encounterCardsTable)
        encounterTab = QWidget()
        encounterTab.setLayout(encounterLayout)
        
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(playerTab, self.tr('Construct Player Decks'))
        self.tabWidget.addTab(encounterTab, self.tr('View Encounter Cards'))
        self.tabWidget.currentChanged.connect(self.changeTab)
        
        centralWidget = QWidget()
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addWidget(self.tabWidget)
        centralWidget.setLayout(layout)
        
        self.setCentralWidget(centralWidget)
        self.setWindowTitle(self.tr('LotR LCG Deck Builder'))
        self.setWindowIcon(QIcon(':/images/icons/DeckBuilder.ico'))
        self.showMaximized()
        
    def focusOutEvent(self, event):
        pass  # reimplementing this method makes the selected row still highlighted
        
    def closeEvent(self, event):
        if self.dirty:
            msgBox = QMessageBox(QMessageBox.Warning, self.tr('Unsaved Changes'), QString('%1<br>%2').arg(self.tr('Some changes are not saved yet.')).arg(self.tr('Save now?')), QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, self)
            choice = msgBox.exec_()
            if choice == QMessageBox.Save:
                self.save()
                event.accept()
            elif choice == QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DeckBuilder()
    widget.show()
    sys.exit(app.exec_())