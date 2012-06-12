import collections
import glob
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


VERSION = '2012.06.13'


SETS = ('core', 'mirkwood', 'osgiliath', 'khazaddum', 'dwarrowdelf')  # EXPANSION

CARD_WIDTH = 358
CARD_HEIGHT = 500
TOKEN_WIDTH = 65
TOKEN_HEIGHT = 65

Z_INDEX_TOP = 1023  # QGraphicsItem with this Z value will be shown above all other things
PADDING = 10
OFFSET = (CARD_HEIGHT - CARD_WIDTH) / 2


def getCardPixmap(imageResourcePath):
    pixmap = None
    if QFile(imageResourcePath).exists():
        pixmap = QPixmap(imageResourcePath)
    else:
        pixmap = QPixmap(':/images/error.png')
        print('File not exists: {0}'.format(imageResourcePath))
    return pixmap


def _convertJson():
    def evalJsonObject(filePath):
        '''replace some JavaScript keywords to Python keywords then eval'''
        with open(filePath) as f:
            content = f.read()
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
                print('{0} dumped.'.format(newFilePath))

#_convertJson()


def _parseInfo(filePath):
    with open(filePath) as f:
        return json.loads(f.read())

cardsInfo = {}
for set_ in SETS:
    cardsInfo[set_] = _parseInfo('./resource/introspection/cards_{0}.json'.format(set_))

scenariosInfo = _parseInfo('./resource/introspection/scenarios.json')


# copy default decks if not exists
_DECKS = './decks.json'
_FALLBACK = './resource/decks_fallback.json'
if not os.path.exists(_DECKS):
    shutil.copyfile(_FALLBACK, _DECKS)


# check if decks are corrupted
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


def warnIfDecksCorrupted(parentWidget):
    if DECKS_CORRUPTED:
        msgBox = QMessageBox(QMessageBox.Critical, QCoreApplication.translate('QObject', 'Decks Corrupted'), QString('%1<br>%2').arg(QCoreApplication.translate('QObject', 'Decks file "decks.json" corrupted!')).arg(QCoreApplication.translate('QObject', 'Loading default decks...')), QMessageBox.Ok, parentWidget)
        msgBox.exec_()


def saveFile(filePath, contentText):
    file = QFile(filePath)
    file.open(QIODevice.WriteOnly | QIODevice.Text)
    result = file.writeData(contentText)
    file.close()
    if result == -1:  # write file failed
        return False
    return True