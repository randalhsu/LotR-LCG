from common import *


class _AttachedItems:
    '''Each Card instance has one AttachedItems instance, bookkeeping every Card/Token instances attached to that Card'''
    def __init__(self, parent):
        self.parent = parent
        
        self.counter = {
            'damage': 0,
            'progress': 0,
            'resource': 0,
        }
        self.tokens = []  # Token instances
        self.equipments = []  # attachment or objective Card instances
        self.shadows = []  # shadow or guarder Card instances
        
    def calcTokenPos(self, type_, i):
        column = int(i / 5)
        if i % 5 == 0:
            column -= 1
        x = PADDING + TOKEN_WIDTH * column * 0.7
        
        if type_ in ('resource', 'progress'):
            return QPointF(x, CARD_HEIGHT - 30 - TOKEN_HEIGHT * (i - column * 5) * 0.7)
        elif type_ == 'damage':
            return QPointF(x, PADDING + TOKEN_HEIGHT * (i - 1 - column * 5) * 0.7)
        
    def calcCardPos(self, type_, i, exhausted=False):
        if type_ == 'attachment':
            offset = OFFSET if exhausted else 0
            return QPointF(0, i * CARD_HEIGHT / 4 + offset)
        else:
            return QPointF(0, -i * CARD_HEIGHT / 4)
        
    def updateCardPos(self):
        for (i, card) in enumerate(self.equipments):
            card.setPos(self.calcCardPos('attachment', i + 1, card.exhausted()))
            card.setZValue(Z_INDEX_TOP - i)
            
        for (i, card) in enumerate(self.shadows):
            card.setPos(self.calcCardPos('shadow', i + 1))
            card.setZValue(Z_INDEX_TOP - len(self.shadows) + i)
        
    def attach(self, item):
        item.setParentItem(self.parent)
        if isinstance(item, Card):
            self.attachCard(item)
        elif isinstance(item, Token):
            self.attachToken(item)
            
        self.updateParent()
        
    def attachToken(self, token):
        self.tokens.append(token)
        tokenType = token.type_()
        self.counter[tokenType] += 1
        token.setPos(self.calcTokenPos(tokenType, self.counter[tokenType]))
        
    def attachCard(self, card):
        def attachable(child, parent):
            if child.info['type'] in ('attachment', 'objective'):
                if child.revealed():
                    return True
            if parent.info['type'] in ('hero', 'ally'):
                return True
            return False
            
        if attachable(card, self.parent):
            card.setFlag(QGraphicsItem.ItemStacksBehindParent)
            self.equipments.append(card)
        else:  # shadow card or objective card's guarder
            self.shadows.append(card)
        self.updateCardPos()
        
    def detach(self, item):
        if item.scene():
            item.scene().removeItem(item)
        if isinstance(item, Card):
            self.detachCard(item)
        else:
            self.detachToken(item)
            
        self.updateParent()
        
    def detachCard(self, card):
        if card in self.equipments:
            self.equipments.remove(card)
        elif card in self.shadows:
            self.shadows.remove(card)
        self.updateCardPos()
        
    def detachToken(self, token):
        if token in self.tokens:
            tokenType = token.type_()
            self.counter[tokenType] -= 1
            self.tokens.remove(token)
            # update tokens' pos of same type
            i = 1
            for token in self.tokens:
                if token.type_() == tokenType:
                    token.setPos(self.calcTokenPos(tokenType, i))
                    i += 1
                    
    def removeAllTokens(self):
        while self.tokens:
            self.detach(self.tokens[-1])
            
    def updateParent(self):
        scene = self.parent.scene()
        if scene:
            views = scene.views()
            if views:
                for view in views:
                    view.update()
                    
    def __str__(self):
        equipmentCards = '['
        for card in self.equipments:
            equipmentCards += str(card)
        equipmentCards += ']'
        
        shadowCards = '['
        for card in self.shadows:
            shadowCards += str(card)
        shadowCards += ']'
        return 'r{0}d{1}p{2}E{3}S{4}'.format(self.counter['resource'], self.counter['damage'], self.counter['progress'], equipmentCards, shadowCards)
        
    def getState(self):
        '''dict representation, for syncing program states between clients'''
        state = {}
        
        if self.counter['damage'] > 0:
            state['D'] = self.counter['damage']
        if self.counter['progress'] > 0:
            state['P'] = self.counter['progress']
        if self.counter['resource'] > 0:
            state['R'] = self.counter['resource']
        
        if self.equipments:
            cards = []
            for card in self.equipments:
                cards.append(card.getState())
            state['E'] = cards
        
        if self.shadows:
            cards = []
            for card in self.shadows:
                cards.append(card.getState())
            state['S'] = cards
        
        return state


class Token(QGraphicsPixmapItem):
    def __init__(self, tokenType, parent=None):
        assert(tokenType in ('damage', 'progress', 'resource'))
        super(Token, self).__init__(QPixmap('./resource/image/token/{0}.png'.format(tokenType)), parent)
        self.setFlag(QGraphicsItem.ItemIgnoresParentOpacity)
        self._type = tokenType
        
    def type_(self):
        return self._type
        
    def __str__(self):
        return self.type_().title()


class Card(QGraphicsPixmapItem):
    imageDict = {}  # this will cache all created  (set_, id): QPixmap  instances
    
    def __init__(self, info, revealed=False):
        super(Card, self).__init__()
        
        # workaround for Error "QPixmap: Must construct a QApplication before a QPaintDevice"
        if not hasattr(Card, 'PLAYER_CARD_BACK_IMAGE'):
            Card.PLAYER_CARD_BACK_IMAGE = scaledCardPixmap('./resource/image/player_card_back.jpg')
        if not hasattr(Card, 'ENCOUNTER_CARD_BACK_IMAGE'):
            Card.ENCOUNTER_CARD_BACK_IMAGE = scaledCardPixmap('./resource/image/encounter_card_back.jpg')
        if not hasattr(Card, 'IMAGE_PATH_DICT'):
            Card.IMAGE_PATH_DICT = self.parseCardImagePathDict()
        
        self.setTransformOriginPoint(CARD_WIDTH / 2, CARD_HEIGHT / 2)
        self.setTransformationMode(Qt.SmoothTransformation)
        
        self.info = info  # card info dict from ./resource/introspection/cards_*.json
        self._revealed = revealed
        self._exhausted = False
        
        self.attachedItems = _AttachedItems(self)
        
        type_ = self.info['type']
        (set_, id) = (self.info['set'], self.info['id'])
        
        if (set_, id) in Card.imageDict and type_ != 'quest':  # QPixmap already cached
            self.frontImage = Card.imageDict[(set_, id)]
        else:
            imagePath = Card.IMAGE_PATH_DICT[(self.info['set'], self.info['id'])]
            if type_ == 'quest':
                self.frontImage = scaledCardPixmap(imagePath[:-4] + '-A.jpg')
                self.backImage = scaledCardPixmap(imagePath[:-4] + '-B.jpg')
            else:
                pixmap = scaledCardPixmap(imagePath)
                self.frontImage = pixmap
                Card.imageDict[(set_, id)] = pixmap  # cache it
                
        if type_ in ('hero', 'ally', 'event', 'attachment'):
            self.backImage = Card.PLAYER_CARD_BACK_IMAGE
        elif type_ in ('enemy', 'treachery', 'location', 'objective'):
            self.backImage = Card.ENCOUNTER_CARD_BACK_IMAGE
            
        self.updateImage()
        
    def revealed(self):
        return self._revealed
        
    def flip(self):
        self._revealed = not self._revealed
        self.updateImage()
        
        if self.info['type'] != 'quest':
            for child in self.childItems():
                child.setVisible(self.revealed())
        
    def exhausted(self):
        return self._exhausted
        
    def exhaust(self):
        self._exhausted = True
        
    def ready(self):
        self._exhausted = False
        
    def updateImage(self):
        self.setPixmap(self.currentImage())
        
    def currentImage(self):
        if self.revealed():
            return self.frontImage
        else:
            return self.backImage
            
    def attach(self, item):
        self.attachedItems.attach(item)
        
    def detach(self, item):
        self.attachedItems.detach(item)
        
    def fullSize(self):
        '''occupied tuple(width, height), including all its children (attached cards)'''
        rect = self.boundingRect() | self.childrenBoundingRect()
        return (rect.width(), rect.height())
        
    def parseCardImagePathDict(self):
        pathDict = {}
        for set_ in cardsInfo:
            with open('./resource/card_image_path_{0}.txt'.format(set_)) as f:
                lines = f.readlines()
                for (id, fileName) in enumerate(lines):
                    fileName = fileName.strip()
                    if fileName:
                        pathDict[(set_, id + 1)] = './resource/image/{0}/{1}'.format(set_, fileName)
        return pathDict
        
    def __str__(self):
        return '[{0}]'.format(self.info['title'])
        
    def __repr__(self):
        return '[({0},{1})]'.format(self.info['set'], self.info['id'])
        
    def getState(self):
        '''dict representation, for syncing program states between clients'''
        state = self.attachedItems.getState()
        state['s'] = self.info['set']
        state['i'] = self.info['id']
        if not self.revealed():
            state['c'] = 1
        if self.exhausted():
            state['e'] = 1
        return state
        '''
        keys of state:
        s -> card set (str)
        i -> card id  (int)
        c -> covered   (1 if covered)
        e -> exhausted (1 if exhausted)
        D ->   damage token (int)
        P -> progress token (int)
        R -> resource token (int)
        E -> attached cards as equipment (list of card states)
        S -> attached cards as shadow    (list of card states)
        '''