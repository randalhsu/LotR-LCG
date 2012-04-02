from Area import *


class Deck(Area):
    def __init__(self, name, visualName, orientation=Qt.Vertical, parent=None):
        super(Deck, self).__init__(name, parent=parent)
        self.orientation = orientation
        
        self.emptyItem = QGraphicsPixmapItem(scaledCardPixmap('./resource/image/empty.png'))
        self.emptyItem.setPos(0, 0)
        self.emptyItem.setZValue(-1)
        self.scene.addItem(self.emptyItem)
        
        self.nameTextItem = QGraphicsTextItem()
        self.nameTextItem.setPos(PADDING * 2, 0)
        self.nameTextItem.setFont(QFont('Times', 50, QFont.Bold))
        self.nameTextItem.setDefaultTextColor(QColor(Qt.white))
        self.nameTextItem.shape = lambda: QPainterPath()  # disable its mouse click event
        self.nameTextItem.setZValue(Z_INDEX_TOP)  # will be shown above any other things
        self.nameTextItem.hide()
        self.nameTextItem.setHtml(visualName)
        self.scene.addItem(self.nameTextItem)
        
        self.sizeTextItem = QGraphicsSimpleTextItem('0')
        self.sizeTextItem.setFont(QFont('Times', 75, QFont.Bold))
        self.sizeTextItem.setBrush(QBrush(Qt.white))
        self.sizeTextItem.shape = lambda: QPainterPath()
        self.sizeTextItem.setZValue(Z_INDEX_TOP)
        self.scene.addItem(self.sizeTextItem)
        
        if self.orientation == Qt.Horizontal:
            self.nameTextItem.setRotation(-90)
            self.nameTextItem.setPos(0, CARD_HEIGHT - PADDING * 2)
            self.sizeTextItem.setRotation(-90)
            self.rotate(90)
            
        if self.name == 'Active Location':
            self.sizeTextItem.setOpacity(0)
        
    def enterEvent(self, event):
        self.nameTextItem.show()
        
    def leaveEvent(self, event):
        self.nameTextItem.hide()
        
    def sizeHint(self):
        return QSize(CARD_WIDTH + PADDING, CARD_HEIGHT + PADDING)
        
    def update(self):
        for (i, card) in enumerate(self.cardList):
            card.setPos(0, 0)
            card.setZValue(i)
            
        self.sizeTextItem.setText(str(len(self.cardList)))
        textRect = self.sizeTextItem.sceneBoundingRect()
        if self.orientation == Qt.Vertical:
            self.sizeTextItem.setPos(CARD_WIDTH - (textRect.width() + PADDING * 2), CARD_HEIGHT - textRect.height())
        else:
            self.sizeTextItem.setPos(CARD_WIDTH - textRect.width(), textRect.height() + PADDING * 2)
        
        sceneRect = self.scene.itemsBoundingRect()
        self.scene.setSceneRect(sceneRect)
        sceneRect.adjust(-PADDING, -PADDING, PADDING, PADDING)
        self.fitInView(sceneRect, Qt.KeepAspectRatio)