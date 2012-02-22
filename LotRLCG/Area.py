import random
from Draggable import *


def purify(item):
    '''Reset a QGraphicsPixmapItem's every attributes'''
    if isinstance(item, Card):
        item.setPos(0, 0)
        item.setZValue(0)
        item.setRotation(0)
        item.ready()
        item.setFlag(QGraphicsItem.ItemStacksBehindParent, False)
    if item.parentItem():
        item.parentItem().detach(item)
    if item.scene():
        item.scene().removeItem(item)


class Area(QGraphicsView):
    '''Where Card instances are placed'''
    def __init__(self, name, orientation=Qt.Horizontal, parent=None):
        super(Area, self).__init__(parent)
        self.setMouseTracking(True)
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.highlightEffect = None
        
        self.name = name
        self.cardList = []
        self.orientation = orientation
        
        self.draggingItem = None
        
    def addCard(self, card):
        assert(isinstance(card, QGraphicsPixmapItem))
        purify(card)
        self.cardList.append(card)
        self.scene.addItem(card)
        self.update()
        
    def removeCard(self, card):
        assert(isinstance(card, QGraphicsPixmapItem))
        if card in self.cardList:
            purify(card)
            self.cardList.remove(card)
            self.update()
        
    def getList(self):
        return self.cardList
        
    def setList(self, cardList):
        for card in self.cardList:
            self.removeCard(card)
        self.cardList = []
        
        for card in cardList:
            self.addCard(card)
        
    def shuffle(self):
        random.shuffle(self.cardList)
        self.update()
        
    def draw(self):
        '''draw one card from cardList'''
        if self.cardList:
            card = self.cardList[-1]
            self.removeCard(card)
            return card
        return None
        
    def mouseDoubleClickEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
            
        item = self.itemAt(event.pos())
        if isinstance(item, Card):
            card = item
            card.flip()
            self.window().setLargeImage(card)
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragStartPos = event.pos()
        elif event.button() == Qt.RightButton:
            item = self.itemAt(event.pos())
            if isinstance(item, Token):
                item.parentItem().detach(item)
                return
            elif self.name == 'Hand Area' or isinstance(self, Deck):
                if self.cardList:
                    manipulator = DeckManipulator(self, self.topLevelWidget())
                    manipulator.show()
                    return
            elif isinstance(item, Card) and self.name in ('Engaged Area', 'Hero Area'):
                if item.exhausted():
                    item.ready()
                else:
                    item.exhaust()
            self.update()
            self.update()  # don't ask me why...
            
    def mouseMoveEvent(self, event):
        item = self.itemAt(event.pos())
        if not item:
            if self.draggingItem is None:
                self.setCursor(Qt.ArrowCursor)
            return
        self.setCursor(Qt.OpenHandCursor)
        
        if isinstance(item, Card):
            self.window().setLargeImage(item)
            
        if event.buttons() != Qt.LeftButton:
            return
            
        if (event.pos() - self.dragStartPos).manhattanLength() < QApplication.startDragDistance():
            return
        
        # start dragging...
        scaleFactor = self.viewportTransform().m11() * 0.5  # m11 is horizontal scaling factor
        baseWidth, baseHeight = (CARD_WIDTH, CARD_HEIGHT) if isinstance(item, Card) else (TOKEN_WIDTH, TOKEN_HEIGHT)
        thumbnailWidth, thumbnailHeight = baseWidth * scaleFactor, baseHeight * scaleFactor
        thumbnail = item.pixmap().scaled(thumbnailWidth, thumbnailHeight, Qt.KeepAspectRatio)
        hotSpot = QPoint(thumbnailWidth / 2, thumbnailHeight / 2)
        
        mimeData = QMimeData()
        mimeData.setData('application/x-lotrlcg', 'iDontCare')
        
        drag = QDrag(self)
        drag.setPixmap(thumbnail)
        drag.setHotSpot(hotSpot)
        drag.setMimeData(mimeData)
        self.setCursor(Qt.DragMoveCursor)
        
        item.setOpacity(0.5)
        if self.name == 'Token Bank':
            self.draggingItem = Token(item.type_())
        else:
            self.draggingItem = item  # for transfering item instance between Areas
        drag.exec_()
        item.setOpacity(1)
        self.draggingItem = None
        
    def dragMoveEvent(self, event):
        '''implement highlight effect'''
        if event.mimeData().hasFormat('application/x-lotrlcg'):
            self.setCursor(Qt.DragMoveCursor)
            # this shit must be reinitialized every time
            try:
                if self.highlightEffect:
                    self.highlightEffect.setEnabled(False)
            except RuntimeError:  # Underlying C/C++ object has been deleted. No idea.
                pass
            self.highlightEffect = QGraphicsColorizeEffect()
            
            if self.name == 'Hand Area':
                self.setGraphicsEffect(self.highlightEffect)
                return
                
            item = self.itemAt(event.pos())
            if item:
                while item.parentItem():
                    item = item.parentItem()
                item.setGraphicsEffect(self.highlightEffect)
            else:
                self.setGraphicsEffect(self.highlightEffect)
            self.update()
            
    def dragLeaveEvent(self, event):
        if self.highlightEffect:
            self.highlightEffect.setEnabled(False)
            # some area will still be highlighted here. No idea. Let's force it unhighlight again...
            self.highlightEffect = QGraphicsColorizeEffect()
            self.setGraphicsEffect(self.highlightEffect)
            self.highlightEffect.setEnabled(False)
            self.update()
            
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-lotrlcg'):
            if self.highlightEffect:
                self.highlightEffect.setEnabled(False)
            
            source = event.source()
            draggingItem = event.source().draggingItem
            targetItem = self.itemAt(event.pos())
            if targetItem:
                while targetItem.parentItem():
                    targetItem = targetItem.parentItem()
                    
            if not self.dndHandler(draggingItem, source, targetItem):
                event.setDropAction(Qt.IgnoreAction)
            self.update()
            source.update()
            self.setCursor(Qt.OpenHandCursor)
        
    def dndHandler(self, draggingItem, source, targetItem):
        '''drag draggingItem from sourceArea, to selfArea's targetItem. Return True on valid operation'''
        if draggingItem is targetItem:
            return False
            
        if targetItem:  # intend to attach something
            if isinstance(draggingItem, Card):
                if isinstance(targetItem, Card):  # Card -> Card
                    if self.name in ('Engaged Area', 'Hero Area', 'Staging Area'):
                        source.removeCard(draggingItem)
                        purify(draggingItem)
                        targetItem.attach(draggingItem)
                        return True
                    else:  # Card -> Deck or HandArea
                        source.removeCard(draggingItem)
                        purify(draggingItem)
                        self.addCard(draggingItem)
                        return True
            elif isinstance(draggingItem, Token):
                if isinstance(targetItem, Card):  # Token -> Card
                    purify(draggingItem)
                    targetItem.attach(draggingItem)
                    return True
        else:
            if isinstance(draggingItem, Card):  # Card -> Area
                source.removeCard(draggingItem)
                purify(draggingItem)
                self.addCard(draggingItem)
                return True
        return False
        
    def resizeEvent(self, event):
        self.update()
        
    def update(self):
        '''this is totally crappy holy shit. DON'T DO THIS AT HOME'''
        if not self.cardList:
            return
        for (i, card) in enumerate(self.cardList):
            card.setZValue(i)
            
        if self.orientation == Qt.Horizontal:
            x = 0
            if self.name == 'Hand Area':  # partially stackable
                ratio = float(CARD_WIDTH * len(self.cardList)) / CARD_HEIGHT
                limitedRatio = float(self.width()) / self.height()
                if ratio > limitedRatio and len(self.cardList) > 1:  # do compact listing
                    # since limitedRatio == (avgAvailableWidth * (N - 1) + cardWidth) / cardHeight
                    avgAvailableWidth = (limitedRatio * CARD_HEIGHT - CARD_WIDTH) / (len(self.cardList) - 1)
                    for card in self.cardList:
                        card.setPos(x, 0)
                        x += avgAvailableWidth
                else:  # space is sufficient
                    for card in self.cardList:
                        card.setPos(x, 0)
                        x += CARD_WIDTH
            else:
                # N cards in a row
                N = 6
                row = 0
                y = 0
                for (i, card) in enumerate(self.cardList):
                    if i >= N and i % N == 0:
                        row += 1
                        height = CARD_HEIGHT
                        for card_ in self.cardList[(row - 1) * N : row * N]:
                            size = card_.fullSize()
                            if card_.exhausted():
                                height = max(height, size[0])
                            else:
                                height = max(height, size[1])
                        y += height + PADDING
                        x = 0
                        
                    offset = 0
                    if card.exhausted():
                        card.setRotation(90)
                        offset = OFFSET + card.fullSize()[1] - CARD_HEIGHT
                    else:
                        card.setRotation(0)
                        if card.fullSize()[0] == CARD_HEIGHT:  # readied card with exhausted attachment
                            offset = OFFSET
                            
                    card.setPos(x + offset, y)
                    
                    if card.exhausted():
                        x += card.fullSize()[1]
                    else:
                        x += card.fullSize()[0]
                    x += PADDING * 2
                    
                    for attachedItem in card.childItems():
                        if isinstance(attachedItem, Token):
                            continue
                            
                        if attachedItem.exhausted():
                            if attachedItem.rotation() == 0:
                                attachedItem.moveBy(0, OFFSET)
                            attachedItem.setRotation(90)
                        else:
                            if attachedItem.rotation() == 90:
                                attachedItem.moveBy(0, -OFFSET)
                            attachedItem.setRotation(0)
                    
        else:  # self.orientation == Qt.Vertical:
            y = 0
            for card in self.cardList:
                y += len(card.attachedItems.shadows) * CARD_HEIGHT / 4
                card.setPos(0, y)
                y += CARD_HEIGHT + len(card.attachedItems.equipments) * CARD_HEIGHT / 4 + PADDING * 2
                
        sceneRect = self.scene.itemsBoundingRect()
        self.scene.setSceneRect(sceneRect)
        sceneRect.adjust(-PADDING, -PADDING, PADDING, PADDING)
        self.fitInView(sceneRect, Qt.KeepAspectRatio)
        
    def __str__(self):
        return self.name


# sorry for recursive dependencies...
from Deck import Deck
from DeckManipulator import DeckManipulator