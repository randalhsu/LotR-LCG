from common import *


class ThreatDial(QGraphicsView):
    def __init__(self, parent=None):
        super(ThreatDial, self).__init__(parent)
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setBackgroundBrush(QBrush(QColor.fromRgb(165, 165, 165)))
        self.setMouseTracking(True)
        self.setCursor(Qt.PointingHandCursor)
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.threatPixmap = QPixmap('./resource/image/threatdial.png')
        self.threatItem = None
        
        gradient = QLinearGradient()
        gradient.setColorAt(0, QColor.fromRgb(255, 246, 200))
        gradient.setColorAt(1, QColor.fromRgb(240, 66, 44))
        brush = QBrush(gradient)
        
        self.tensDigit = QGraphicsSimpleTextItem('0')
        self.tensDigit.setFont(QFont('Times', 16, QFont.Bold))
        self.tensDigit.setBrush(brush)
        self.tensDigit.setPos(145, 78)
        self.tensDigit.setZValue(Z_INDEX_TOP)
        self.scene.addItem(self.tensDigit)
        
        self.unitsDigit = QGraphicsSimpleTextItem('0')
        self.unitsDigit.setFont(QFont('Times', 16, QFont.Bold))
        self.unitsDigit.setBrush(brush)
        self.unitsDigit.setPos(202, 78)
        self.unitsDigit.setZValue(Z_INDEX_TOP)
        self.scene.addItem(self.unitsDigit)
        
        brush = QBrush(QColor.fromRgb(255, 255, 255))
        self.plusItem = QGraphicsSimpleTextItem('+')
        self.plusItem.setFont(QFont('Times', 100, QFont.Bold))
        self.plusItem.setBrush(brush)
        self.plusItem.setPos(250, 11)  # '+' font is a little above '-'
        self.plusItem.setZValue(Z_INDEX_TOP)
        self.plusItem.shape = lambda: QPainterPath()
        self.plusItem.hide()
        self.scene.addItem(self.plusItem)
        
        self.minusItem = QGraphicsSimpleTextItem('-')
        self.minusItem.setFont(QFont('Times', 100, QFont.Bold))
        self.minusItem.setBrush(brush)
        self.minusItem.setPos(25, 0)
        self.minusItem.setZValue(Z_INDEX_TOP)
        self.minusItem.shape = lambda: QPainterPath()
        self.minusItem.hide()
        self.scene.addItem(self.minusItem)
        
        self.value = 20  # current threat level
        self.scaleRatio = 1
        
    def setValue(self, value):
        self.value = value
        self.tensDigit.setText(str(value / 10))
        self.unitsDigit.setText(str(value % 10))
        
    def increaseValue(self):
        self.setValue(self.value + 1)
        
    def decreaseValue(self):
        self.setValue(self.value - 1)
        
    def leaveEvent(self, event):
        self.plusItem.hide()
        self.minusItem.hide()
        
    def mouseMoveEvent(self, event):
        x = event.pos().x()
        if x > self.width() / 2:
            self.plusItem.show()
            self.minusItem.hide()
        else:
            self.plusItem.hide()
            self.minusItem.show()
            
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressEvent(event)
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            if x > self.width() / 2:
                self.increaseValue()
            else:
                self.decreaseValue()
        elif event.button() == Qt.RightButton:
            (value, valid) = QInputDialog.getInt(self, 'Threat Dial', 'Set threat value to:', self.value, 0, 99)
            if valid:
                self.setValue(value)
            
    def resizeEvent(self, event):
        if self.width() != 0 and self.height() != 0:
            widthRatio = self.threatPixmap.width() / self.width()
            heightRatio = self.threatPixmap.height() / self.height()
            self.scaleRatio = min(widthRatio, heightRatio)
        self.update()
        
    def update(self):
        pixmapWidth = self.threatPixmap.width() * self.scaleRatio
        pixmapHeight = self.threatPixmap.height() * self.scaleRatio
        self.threatPixmap = self.threatPixmap.scaled(pixmapWidth, pixmapHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        if self.threatItem:
            self.scene.removeItem(self.threatItem)
        self.threatItem = QGraphicsPixmapItem(self.threatPixmap)
        self.scene.addItem(self.threatItem)
        
        sceneRect = self.scene.itemsBoundingRect()
        self.scene.setSceneRect(sceneRect)
        self.fitInView(sceneRect, Qt.KeepAspectRatio)