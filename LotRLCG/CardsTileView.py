from Area import *


class CardsTileView(Area):
    def __init__(self, deck, mainWindow, parent=None):
        super(CardsTileView, self).__init__(name='', parent=parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setBackgroundBrush(deck.backgroundBrush())
        self.textList = []
        self.mainWindow = mainWindow
        
        while deck.getList():
            self.addCard(deck.draw())
            
        rows = int(len(self.cardList) / 6) + 1
        rows = min(5, rows)
        self.setMinimumSize(370, rows * 96)
        self.dragSource = None
        
    def removeCard(self, card):
        if card in self.cardList:
            lastTextItem = self.textList.pop(-1)
            self.scene.removeItem(lastTextItem)
            super(CardsTileView, self).removeCard(card)
            
    # When card is dragged from outside and hovered over CardsTileView, it will temporarily take ownership of card.
    # These drag & drop event handlers implement this behavior.
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-lotrlcg'):
            item = event.source().draggingItem
            if item not in self.cardList:
                purify(item)
                self.dndHandler(item, event.source(), None)
                self.draggingItem = item
                self.dragSource = event.source()
            super(CardsTileView, self).dragEnterEvent(event)
            self.update()
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-lotrlcg'):
            assert(self.draggingItem in self.cardList or isinstance(self.draggingItem, Token))
            
            if not isinstance(self.draggingItem, Card):
                return
                
            item = self.itemAt(event.pos())
            if not item:
                return
                
            if item != self.draggingItem:  # changing cards' orders
                # put draggingItem to the position currently occupied by hovered item
                indexFrom = self.cardList.index(self.draggingItem)
                indexTo = self.cardList.index(item)
                self.cardList.remove(self.draggingItem)
                if indexFrom < indexTo:
                    self.cardList.insert(self.cardList.index(item) + 1, self.draggingItem)
                else:
                    index = max(0, self.cardList.index(item) - 1)
                    self.cardList.insert(index, self.draggingItem)
                self.update()
            
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-lotrlcg'):
            if event.source() == self:
                return
            if event.source().draggingItem not in self.cardList:
                super(CardsTileView, self).dropEvent(event)
            self.dragSource.draggingItem = None
            
    def dragLeaveEvent(self, event):
        purify(self.draggingItem)
        self.removeCard(self.draggingItem)
        if self.dragSource:
            self.dragSource.addCard(self.draggingItem)
        
    def createTextItem(self, text):
        item = QGraphicsSimpleTextItem(text)
        item.setFont(QFont('Times', 50, QFont.Bold))
        item.setBrush(QBrush(Qt.white))
        item.shape = lambda: QPainterPath()
        item.setZValue(Z_INDEX_TOP)
        return item
        
    def calcCardPos(self, i):
        return QPointF((i % 5) * (CARD_WIDTH + PADDING * 2), int(i / 5) * (CARD_HEIGHT + PADDING * 2))
        
    def calcTextPos(self, i, textItem):
        rect = textItem.boundingRect()
        return self.calcCardPos(i) + QPointF(CARD_WIDTH - rect.width() * 1.2, CARD_HEIGHT - rect.height())
        
    def update(self):
        self.scrollBarValue = self.verticalScrollBar().value()
        
        # make len(self.textList) == len(self.cardList)
        while len(self.textList) < len(self.cardList):
            i = len(self.textList) + 1
            textItem = self.createTextItem(str(i))
            textItem.setPos(self.calcTextPos(i - 1, textItem))
            self.textList.append(textItem)
            self.scene.addItem(textItem)
            
        while len(self.textList) > len(self.cardList):
            lastTextItem = self.textList.pop(-1)
            self.scene.removeItem(lastTextItem)
            
        for (i, card) in enumerate(self.cardList):
            card.setPos(self.calcCardPos(i))
            
        sceneRect = QRectF(0, 0, (CARD_WIDTH + PADDING * 2) * 5, (CARD_HEIGHT + PADDING * 2) * 5)
        sceneRect.adjust(-PADDING, -PADDING, PADDING, PADDING)
        self.fitInView(sceneRect, Qt.KeepAspectRatioByExpanding)
        
        self.verticalScrollBar().setValue(self.scrollBarValue)