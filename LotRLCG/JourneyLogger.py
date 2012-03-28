import re
from common import *


class JourneyLogger(QDialog):
    def __init__(self, parent=None):
        super(JourneyLogger, self).__init__(parent)
        self.sphereColor = {
            'leadership': '9d489b',
            'tactics': 'b71f25',
            'spirit': '00b6e3',
            'lore': '00a651',
        }
        self.createUI()
        self.lastMessage = ''  # last line of appended log
        
    def append(self, message):
        message = self.parseMessage(message)
        if self.canBeCombinedWithLastLog(message):
            self.combineWithLastLog(message)
        else:
            self.lastMessage = message
            self.textEdit.append(message)
            
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
            color = self.sphereColor.get(cardsInfo[set_][id]['icon'], '000000')
            message = '{0}<font color="#{1}">{2}</font>{3}'.format(message[:cardStartIndex], color, title, message[cardEndIndex:])
        return message
        
    def parseMessage(self, message):
        message = self.convertCardsRepresentation(message)
        # message examples listed later do not show <font color> tag
        
        if message.startswith(('damage', 'resource', 'progress')):  # Token attach/detach
            '''message examples:
            attach 1 resource token to Aragorn who already has 2 resource tokens: 'resource->[Aragorn](3)'
            remove 1 progress token from Rhosgobel which originally has 3 progress tokens: 'progress<-[Rhosgobel](2)'
            '''
            splitter = '->' if '->' in message else '<-'
            (tokenType, surplus) = message.split(splitter)
            (card, surplus) = surplus.split('(', 1)
            count = int(surplus[:-1])
            
            if splitter == '->':  # adding token
                if tokenType == 'damage':
                    return '{0} suffered 1 damage ({1}->{2})'.format(card, count - 1, count)
                elif tokenType == 'resource':
                    return '{0} gained 1 resource ({1}->{2})'.format(card, count - 1, count)
                elif tokenType == 'progress':
                    return 'Progress made at {0} ({1}->{2})'.format(card, count - 1, count)
                    
            elif splitter == '<-':  # removing token
                if tokenType == 'damage':
                    return '{0} healed 1 damage ({1}->{2})'.format(card, count + 1, count)
                elif tokenType == 'resource':
                    return '{0} removed 1 resource ({1}->{2})'.format(card, count + 1, count)
                elif tokenType == 'progress':
                    return 'Progress removed from {0} ({1}->{2})'.format(card, count + 1, count)
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
            parentCard = message[message.find('[') : message.find(']') + 1]
            if message.startswith('{Engaged Area}') and message.endswith('revealed') and parentCard != '[NONE]':
                card = message[message.rfind('[') : message.rfind(']') + 1]
                return "{0}'s shadow {1} revealed".format(parentCard, card)
            else:
                return message[message.index(']') + 1:]
                
        elif '->' in message: # Card movements
            '''message construction:
            {source area}[card]->{destination area}[destination card]
            
            message examples:
            attach to a card: '{Hand Area}[Celebrian's Stone]->{Hero Area}[Theodred]'
            basic movement: '{Staging Area}[Forest Spider]->{Engaged Area}[NONE]'
            yet another example: '{Hero Area}[Faramir]->{Player Discard Pile}[NONE]'
            '''
            cardPattern = r'\[.*?\]'
            cards = re.findall(cardPattern, message)
            card = cards[0]
            destinationCard = cards[1]
            
            areaPattern = '{.*?}'
            areas = re.findall(areaPattern, message)
            sourceArea = areas[0]
            destinationArea = areas[1]
            
            if destinationArea == '{Active Location}':
                return 'Travel to {0}'.format(card)
            elif destinationArea == '{Engaged Area}':
                if destinationCard == '[NONE]':
                    return 'Engaged with {0}'.format(card)
                else:
                    if sourceArea == '{Encounter Deck}':
                        return 'Deal shadow {0} to {1}'.format(card, destinationCard)
            elif destinationArea == '{Staging Area}' and destinationCard == '[NONE]':
                return 'Draw {0} to staging'.format(card)
            elif destinationArea == '{Encounter Discard Pile}':
                if sourceArea == '{Active Location}':
                    return 'Explored {0}'.format(card)
                elif sourceArea == '{Quest Deck}':
                    return 'Defeated {0}'.format(card)
            return message
            
        else:
            return message
            
    def canBeCombinedWithLastLog(self, currentMessage):
        # message is constructed like this: 'blahblahblah 1 blahblahblah (1->2)' or 'blahblahblah (1->2)'
        # we have to know if BLAH parts are the same
        
        if currentMessage.endswith(')'):
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
            lastMessage = cursor.selectedText()
            if lastMessage.endsWith(')'):  # isinstance(lastMessage, QString) , so use QString's method
                lastMessage = str(lastMessage)
                # remove all numbers, then compare two trimmed messages
                message1 = lastMessage
                message2 = currentMessage
                for pattern in ('<font.*">', '</font>', r'\d+', ' +'):
                    message1 = re.sub(pattern, '', message1)
                    message2 = re.sub(pattern, '', message2)
                if message1 == message2:
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
        if lastMessage.startswith('Progress'):
            part1 = lastMessage[:lastMessage.rindex(' ')]
            message = '{0} ({1}->{2})'.format(part1, startingValue, finalValue)
        else:
            m = re.search(r' \d+ ', lastMessage)
            numberPos = lastMessage.index(m.group(0)) + 1
            part1 = lastMessage[:numberPos]
            part2 = lastMessage[numberPos + 1 : lastMessage.rindex('(')]
            message = '{0}{1}{2}({3}->{4})'.format(part1, difference, part2, startingValue, finalValue)
            
        self.lastMessage = message
        self.textEdit.append(message)
        
    def createUI(self):
        self.textEdit = QTextEdit()
        clearButton = QPushButton(self.tr('Clear'))
        clearButton.clicked.connect(self.textEdit.clear)
        closeButton = QPushButton(self.tr('&Close'))
        closeButton.clicked.connect(self.close)
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(clearButton)
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(buttonsLayout)
        self.setLayout(layout)
        
        self.setMinimumWidth(500)
        self.setWindowIcon(QIcon('./resource/image/token/progress.png'))
        self.setWindowTitle(self.tr('Journey Logger'))