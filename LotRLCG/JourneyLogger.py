import re
from common import *


class JourneyLogger(QDialog):
    def __init__(self, parent=None):
        super(JourneyLogger, self).__init__(parent)
        self.sphereColor = {
            'neutral': '969696',
            'leadership': '9d489b',
            'tactics': 'b71f25',
            'spirit': '00b6e3',
            'lore': '00a651',
        }
        cardStringPattern = r'\[.*?\]'
        self.cardPattern = re.compile('{0}|<font.*?>{0}</font>'.format(cardStringPattern))
        self.areaPattern = re.compile('{.*?}')
        
        self.createUI()
        self.lastMessage = ''  # last line of appended log
        
    def append(self, message):
        message = self.parseMessage(message)
        if not message:
            return
        if self.canBeCombinedWithLastLog(message):
            message = self.combineWithLastLog(message)
            
        self.lastMessage = message
        self.textEdit.append(message)
        scrollBar = self.textEdit.verticalScrollBar()
        scrollBar.setValue(scrollBar.maximum())  # scroll to bottom
        
        # handle questing status
        if message.startswith('Completed quest'):
            questCards = self.parentWidget().questDeck.getList()
            if questCards:
                self.append('Questing {0}'.format(repr(questCards[-1])))
            else:
                self.append('Journey done!')
                
    def convertCardsRepresentation(self, message):
        '''replace Card representation such as [('core', 1)] in message into [Aragorn], with font color'''
        while '[(' in message:
            cardStartIndex = message.index('[(')
            cardEndIndex = message.index(')]') + 2
            card = message[cardStartIndex : cardEndIndex]
            card = card[2:-2]
            (set_, id) = card.split(',')
            id = int(id)
            title = '[{0}]'.format(cardsInfo[set_][id]['title'])
            color = self.sphereColor.get(cardsInfo[set_][id]['icon'], '804000')  # Encounter cards' default color
            message = '{0}<font color="#{1}">{2}</font>{3}'.format(message[:cardStartIndex], color, title, message[cardEndIndex:])
        return message
        
    def parseMessage(self, message):
        message = self.convertCardsRepresentation(message)
        # WARNING: message examples listed later do not show <font color> tag
        
        if message.startswith(('damage', 'resource', 'progress')):  # Token attach/detach
            '''message examples:
            attach 1 resource token to Aragorn who already has 2 resource tokens: 'resource->[Aragorn](3)'
            remove 1 progress token from Rhosgobel which originally has 3 progress tokens: 'progress<-[Rhosgobel](2)'
            '''
            damage = '<font color="#b22726">damage</font>'
            resource = '<font color="#80899b">resource</font>'
            progress = '<font color="#097b44">Progress</font>'
            
            splitter = '->' if '->' in message else '<-'
            (tokenType, surplus) = message.split(splitter)
            (card, surplus) = surplus.split('(', 1)
            count = int(surplus[:-1])
            
            if splitter == '->':  # adding token
                if tokenType == 'damage':
                    return '{0} suffered 1 {1} ({2}->{3})'.format(card, damage, count - 1, count)
                elif tokenType == 'resource':
                    return '{0} gained 1 {1} ({2}->{3})'.format(card, resource, count - 1, count)
                elif tokenType == 'progress':
                    return '{0} made at {1} ({2}->{3})'.format(progress, card, count - 1, count)
                    
            elif splitter == '<-':  # removing token
                if tokenType == 'damage':
                    return '{0} healed 1 {1} ({2}->{3})'.format(card, damage, count + 1, count)
                elif tokenType == 'resource':
                    return '{0} spent 1 {1} ({2}->{3})'.format(card, resource, count + 1, count)
                elif tokenType == 'progress':
                    return '{0} removed from {1} ({2}->{3})'.format(progress, card, count + 1, count)
            # TODO: attached card may get resource
            
        elif message.endswith(('exhausted', 'readied')):  # Card exhaust/ready
            '''message examples:
            ready Aragorn: '[NONE]->[Aragorn] readied'
            exhaust "Born Aloft", which is attached to Beorn: '[Beorn]->[Born Aloft] exhausted'
            by auto proceeding Refresh Phase: 'All card readied'
            '''
            if message.startswith('All'):
                return message
            (parent, msg) = message.split('->')
            if parent != '[NONE]':
                msg = "{0}'s {1}".format(parent, msg)
            return msg
            
        elif message.endswith(('revealed', 'covered')):  # Card flip
            '''message construction:
            {area}[parent card][card] action
            
            flipping a shadow card: '{Engaged Area}[Forest Spider][Eyes of the Forest] revealed'
            normal flip: '{Hero Area}[NONE][Aragorn] covered'
            '''
            area = re.search(self.areaPattern, message).group(0)
            (parentCard, card) = re.findall(self.cardPattern, message)
            
            if area == '{Engaged Area}' and message.endswith('revealed') and parentCard != '[NONE]':
                return "{0}'s shadow {1} revealed".format(parentCard, card)
            elif area == '{Quest Deck}':
                return ''
            else:
                message = message.replace('[NONE]', '')
                message = message.replace(' Area}', '}')
                message = message.replace('}', "}'s ")
                return message
                
        elif '->' in message: # Card movements
            '''message construction:
            {source area}[card]->{destination area}[destination card]
            
            message examples:
            attach to a card: '{Hand Area}[Celebrian's Stone]->{Hero Area}[Theodred]'
            basic movement: '{Staging Area}[Forest Spider]->{Engaged Area}[NONE]'
            yet another example: '{Hero Area}[Faramir]->{Player Discard Pile}[NONE]'
            '''
            (card, destinationCard) = re.findall(self.cardPattern, message)
            (sourceArea, destinationArea) = re.findall(self.areaPattern, message)
            
            if destinationCard != '[NONE]':  # attaching card
                if sourceArea == '{Encounter Deck}':
                    if destinationArea == '{Engaged Area}':
                        return 'Deal shadow {0} to {1}'.format(card, destinationCard)
                    elif destinationArea == '{Staging Area}':
                        return '{0} is now guarding {1}'.format(card, destinationCard)
                return 'Attach {0} to {1}'.format(card, destinationCard)
                
            if destinationArea == '{Hand Area}':
                return 'Draw {0}'.format(card)
            elif destinationArea == '{Hero Area}' and sourceArea == '{Hand Area}':
                return 'Play {0}'.format(card)
            elif destinationArea == '{Engaged Area}':
                return 'Engaged with {0}'.format(card)
            if destinationArea == '{Active Location}':
                return 'Travel to {0}'.format(card)
            elif destinationArea == '{Staging Area}':
                return 'Draw {0} to {{Staging}}'.format(card)
            elif destinationArea == '{Encounter Discard Pile}':
                if sourceArea == '{Active Location}':
                    return 'Explored {0}'.format(card)
                elif sourceArea == '{Quest Deck}':
                    return 'Completed quest {0}'.format(card)
                else:
                    return 'Discard {0}'.format(card)
            elif destinationArea == '{Removed From Play}':
                if sourceArea == '{Quest Deck}':
                    return 'Completed quest {0}'.format(card)
            elif destinationArea == '{Player Discard Pile}':
                return 'Discard {0}'.format(card)
                
            message = message.replace('[NONE]', '')
            message = message.replace(' Area}', '}')
            message = message.replace('}', "}'s ", 1)
            message = message.replace('->', ' moved to ')
            return message
            
        else:
            return message
            
    def canBeCombinedWithLastLog(self, currentMessage):
        # message is constructed like this: 'blahblahblah 1 blahblahblah (1->2)' or 'blahblahblah (1->2)'
        # we have to know if BLAH parts are the same
        
        lastMessage = self.lastMessage
        if currentMessage.endswith(')'):
            if lastMessage.endswith(')'):
                lastMessage = str(lastMessage)
                # remove all numbers, then compare two trimmed messages
                message1 = lastMessage
                message2 = currentMessage
                for pattern in ('<font.*?>', '</font>', r'\d+', ' +'):
                    message1 = re.sub(pattern, '', message1)
                    message2 = re.sub(pattern, '', message2)
                if message1 == message2:
                    return True
        else:
            for keyword in ('Threat', 'Victory'):
                pattern = '<font.*?>' + keyword
                if re.match(pattern, currentMessage) and re.match(pattern, lastMessage):
                    return True
        return False
        
    def combineWithLastLog(self, currentMessage):
        # message is constructed like this: 'blahblahblah 1 blahblahblah (1->2)' or 'blahblahblah (1->2)'
        #                                      (part1)        (part2)                  (part1)
        # we want to change its numbers and keep BLAH parts
        
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)  # select last line
        cursor.removeSelectedText()  # remove last line
        cursor.deletePreviousChar()  # remove last newline
        
        for keyword in ('Threat', 'Victory'):
            pattern = '<font.*?>' + keyword
            if re.match(pattern, currentMessage):
                return currentMessage
                
        lastMessage = self.lastMessage
        suffix = lastMessage[lastMessage.rindex('(') + 1 : -1]
        (startingValue, finalValue) = suffix.split('->')
        startingValue = int(startingValue)
        finalValue = int(finalValue)
        if startingValue < finalValue:
            finalValue += 1
        else:
            finalValue -= 1
        difference = abs(finalValue - startingValue)
        
        message = ''
        if re.match('(<font.*?>)?Progress', lastMessage):
            part1 = lastMessage[:lastMessage.rindex(' ')]
            message = '{0} ({1}->{2})'.format(part1, startingValue, finalValue)
        else:
            m = re.search(r' \d+ ', lastMessage)
            numberPos = lastMessage.index(m.group(0)) + 1
            part1 = lastMessage[:numberPos]
            part2 = lastMessage[numberPos + 1 : lastMessage.rindex('(')]
            message = '{0}{1}{2}({3}->{4})'.format(part1, difference, part2, startingValue, finalValue)
        return message
        
    def setStateLabel(self, text):
        self.stateLabel.setText(text)
        QTimer.singleShot(3000, lambda: self.stateLabel.setText(''))  # clear it later
        
    def copyPlainText(self):
        QApplication.clipboard().setText(self.textEdit.toPlainText())
        self.setStateLabel(self.tr('Copied to clipboard!'))
        
    def saveHtmlFile(self):
        filePath = QFileDialog.getSaveFileName(self, self.tr('Save HTML'), 'JourneyLog.html', 'HTML (*.html)')
        if filePath:
            if saveFile(filePath, self.textEdit.toHtml()):
                self.setStateLabel(self.tr('Saved to "%1"'.arg(QFileInfo(filePath).fileName())))
            else:
                QMessageBox.critical(self, self.tr("Can't save HTML"), self.tr('Failed to write file!'))
                
    def showEvent(self, event):
        if hasattr(self, 'lastGeometry'):
            self.setGeometry(self.lastGeometry)
            
    def closeEvent(self, event):
        self.lastGeometry = self.geometry()
        event.accept()
        
    def createUI(self):
        self.textEdit = QTextEdit()
        clearButton = QPushButton(self.tr('Clear'))
        clearButton.clicked.connect(self.textEdit.clear)
        copyPlainTextButton = QPushButton(self.tr('Copy as Plain Text'))
        copyPlainTextButton.clicked.connect(self.copyPlainText)
        saveHtmlButton = QPushButton(self.tr('&Save as HTML'))
        saveHtmlButton.clicked.connect(self.saveHtmlFile)
        self.stateLabel = QLabel()
        closeButton = QPushButton(QCoreApplication.translate('QObject', '&Close'))
        closeButton.clicked.connect(self.close)
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(clearButton)
        buttonsLayout.addWidget(copyPlainTextButton)
        buttonsLayout.addWidget(saveHtmlButton)
        buttonsLayout.addWidget(self.stateLabel)
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(buttonsLayout)
        self.setLayout(layout)
        
        self.resize(500, 300)
        self.setWindowIcon(QIcon(':/images/tokens/progress.png'))
        self.setWindowTitle(self.tr('Journey Logger'))