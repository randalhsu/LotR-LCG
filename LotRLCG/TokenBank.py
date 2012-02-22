from Area import *
from Draggable import *


class TokenBank(Area):
    def __init__(self, parent=None):
        super(TokenBank, self).__init__(parent)
        self.name = 'Token Bank'
        self.resourceToken = Token('resource')
        self.damageToken = Token('damage')
        self.progressToken = Token('progress')
        
        self.addCard(self.resourceToken)
        self.addCard(self.damageToken)
        self.addCard(self.progressToken)
        
    def update(self):
        self.resourceToken.setPos(0, 0)
        self.damageToken.setPos(self.width() / 3, 0)
        self.progressToken.setPos(self.width() * 2 / 3, 0)
        
        sceneRect = self.scene.itemsBoundingRect()
        self.scene.setSceneRect(sceneRect)
        sceneRect.adjust(-PADDING, -PADDING, PADDING, PADDING)
        self.fitInView(sceneRect, Qt.KeepAspectRatio)