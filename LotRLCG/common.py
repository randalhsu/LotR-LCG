import collections
import glob
import hashlib
import json
import os
import shutil
import sys
try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except ImportError:
    print('ImportError: PyQt4 is required to run this program.')
    sys.exit(1)


VERSION = '2012.02.24'


SETS = ('core', 'mirkwood', 'osgiliath', 'khazaddum')  # EXPANSION

CARD_WIDTH = 358
CARD_HEIGHT = 500
TOKEN_WIDTH = 65
TOKEN_HEIGHT = 65

Z_INDEX_TOP = 1023  # QGraphicsItem with this Z value will be shown above all other things
PADDING = 10
OFFSET = (CARD_HEIGHT - CARD_WIDTH) / 2


def scaledCardPixmap(pixmap):
    return pixmap.scaled(CARD_WIDTH, CARD_HEIGHT, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)


def _convertJson():
    def evalJsonObject(filePath):
        '''replace some JavaScript keywords to Python keywords then eval'''
        with open(filePath) as f:
            content = f.read()
            content = content.replace(': null,', ': None,')
            content = content.replace(': true,', ': True,')
            content = content.replace(': false,', ': False,')
            return eval(content)
            
    fileList = glob.glob('./resource/introspection/*_original.js')
    for filePath in fileList:
        filePath = filePath.replace('\\', '/')
        newFilePath = filePath.replace('_original.js', '.json')
        if not os.path.exists(newFilePath):
            object = evalJsonObject(filePath)
            with open(newFilePath, 'w') as f:
                json.dump(object, f, separators=(',', ':'))
                print(newFilePath + ' dumped.')

_convertJson()


def _parseInfo(filePath):
    with open(filePath) as f:
        return json.loads(f.read())

cardsInfo = {}
for set_ in SETS:
    cardsInfo[set_] = _parseInfo('./resource/introspection/cards_{0}.json'.format(set_))

scenariosInfo = _parseInfo('./resource/introspection/scenarios.json')


# a recipe...
_SPICE1 = hashlib.md5('Fantasy Flight Games ').hexdigest()
_SPICE2 = hashlib.md5('The Lord of the Rings: The Card GamE').hexdigest()
_SAUCE1 = sum([int(c) for c in _SPICE1 if c.isdigit()])
_SAUCE2 = sum([int(c) for c in _SPICE2 if c.isdigit()])
_DRESSING = int(_SPICE1[(int(_SPICE1[2]) + int(_SPICE1[3])) / 2])
_MIXED_SAUCE = (_SAUCE1 + _SAUCE2) / _DRESSING

BAD = eval(cardsInfo[eval(scenariosInfo[_DRESSING]['name'].split()[-1].lower().join(("'",) * 2))][_MIXED_SAUCE]['title'].split()[0])
CARD_TASTE = not BAD  # yummy!


_DECKS = './decks.json'
_FALLBACK = './resource/decks_fallback.json'
if not os.path.exists(_DECKS):
    shutil.copyfile(_FALLBACK, _DECKS)

DECKS_CORRUPTED = False
try:
    playerDecksInfo = _parseInfo(_DECKS)
except ValueError:
    playerDecksInfo = _parseInfo(_FALLBACK)
    DECKS_CORRUPTED = True


def isPlayerCard(set_, id):
    if cardsInfo[set_][id]['type'] in ('hero', 'ally', 'event', 'attachment'):
        return True
    return False


def isEncounterCard(set_, id):
    if cardsInfo[set_][id]['type'] in ('enemy', 'location', 'treachery', 'objective', 'quest'):
        return True
    return False


def isHeroCard(set_, id):
    return cardsInfo[set_][id]['type'] == 'hero'


def warnIfDecksCorrupted():
    if DECKS_CORRUPTED:
        msgBox = QMessageBox(QMessageBox.Critical, self.tr('Decks Corrupted'), self.tr('Decks file "decks.json" corrupted. Loading default decks...'), QMessageBox.Ok, self)
        msgBox.exec_()