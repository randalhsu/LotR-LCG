from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from common import *


DEBUG = False

def DPRINT(s):
    if DEBUG:
        print(s)


class Client(QTcpSocket):
    def __init__(self, nickname, serverIP, serverPort, parentWidget):
        super(Client, self).__init__(parent=None)
        self.nickname = nickname
        self.setParent(parentWidget)
        
        self.connectToHost(serverIP, int(serverPort))
        self.connected.connect(self.socketConnected)
        self.readyRead.connect(self.dataIncoming)
        
    def setParent(self, parentWidget):
        self.parent = parentWidget
        
    def appendMessage(self, message):
        self.parent.appendMessage(message)
        
    def appendSystemMessage(self, message):
        self.parent.appendSystemMessage(message)
        
    def sendSystemMessage(self, message):
        data = 'CHAT:__SYSTEM__:{0}\n'.format(message)
        self.sendData(data)
        
    def sendChatMessage(self, message):
        assert(isinstance(message, QByteArray))
        data = 'CHAT:{0}:{1}\n'.format(self.nickname, message)
        self.sendData(data)
        
    def sendData(self, data):
        assert(data.endswith('\n'))
        
        if self.state() != QAbstractSocket.ConnectedState:
            QMessageBox.critical(self.parent, self.tr('Networking Failed'), self.tr('Connection error'))
            
        self.write(QByteArray(data))
        
    def handleChatData(self, data):
        (type_, nickname, message) = data.split(':', 2)
        if message.endswith('\n'):
            message = message[:-1]
            
        if nickname == '__SYSTEM__':
            self.parent.appendSystemMessage(message)
        else:
            chatMessage = nickname + '> ' + QString.fromUtf8(message)
            self.parent.appendMessage(chatMessage)
            
    def handleData(self, data):
        if ':' not in data:
            return False
        (type_, content) = data.split(':', 1)
        
        if type_ == 'STATE':
            content = content[:-1]  # trim '\n'
            self.parent.handleStateChange(content)
            
        elif type_ == 'CHAT':  # example data: 'CHAT:amulet:Cave-Troll, WTF!?\n'
            self.handleChatData(data)
            
        elif type_ == 'SERVER':
            content = content.rstrip()
            if content.startswith('VERSION'):
                version = content.split(':')[1]
                if version != VERSION:
                    QMessageBox.warning(self.parent, self.tr('Different Version'), self.tr('Server\'s program version is "{0}".\nAnything could happen.'.format(version)))
                
            elif content == 'CLOSE':  # data == 'SERVER:CLOSE\n'
                QMessageBox.critical(self.parent, self.tr('Disconnected'), self.tr('SERVER CLOSED!'))
                
            elif content == 'INITIALIZE_MAINWINDOW':  # data == 'SERVER:INITIALIZE_MAINWINDOW\n'
                self.parent.initializeMainWindow()
                
            elif content == 'START_NEW_GAME':  # data == 'SERVER:START_NEW_GAME\n'
                self.parent.startNewGame()
                
            elif content.startswith('ADDRESSES'):  # example data: 'SERVER:ADDRESSES:127.0.0.1:1234,140.116.40.40:1235,210.23.32.1:57649\n'
                self.parent.recordPlayerAddresses(content.split(':', 1)[1])
                
            elif content.startswith('NICKNAMES'):  # example data: 'SERVER:NICKNAMES:amulet,nick,name\n'
                self.parent.recordPlayerNicknames(content.split(':', 1)[1])
                
            elif content.startswith('SETUP'):  # example data: 'SERVER:SETUP:1\n'
                scenarioId = int(content.split(':')[1])
                self.parent.scenarioId = scenarioId
                self.parent.restartGame()
                
    def dataIncoming(self):
        while self.canReadLine():
            data = str(self.readLine())
            self.handleData(data)
        
    def socketConnected(self):
        #DPRINT(str(self.localAddress().toString()) + ':' + str(self.localPort()))
        #DPRINT(str(self.peerAddress().toString()) + ':' + str(self.peerPort()))
        data = 'JOIN:{0}\n'.format(self.nickname)
        self.sendData(data)
        self.parent.clientSocketConnected()


class Server(QTcpServer):
    def __init__(self, parentWidget):
        super(Server, self).__init__()
        self.newConnection.connect(self.playerJoined)
        
        self.setParent(parentWidget)
        self.subscribers = []  # all connected clients' sockets, one of them is from localhost
        # TODO: add chatting colors
        #self.chatColors = (QColor(Qt.darkRed), QColor(Qt.darkGreen), QColor(Qt.darkBlue), QColor(Qt.darkCyan), QColor(Qt.darkMagenta))
        
    def setParent(self, parentWidget):
        self.parent = parentWidget
        
    def hostGame(self):
        '''return PORT that is hosting game, or -1 if failed'''
        if not self.listen():
            return -1
        return self.serverPort()
        
    def writeDataToSocket(self, socket, data):
        if not data.endswith('\n'):
            data += '\n'
        socket.write(QByteArray(data))
        
    def broadcast(self, data):
        for socket in self.subscribers:
            self.writeDataToSocket(socket, data)
            
    def handleData(self, data, sourceSocket=None):
        
        def allPlayerAddresses():
            addresses = ['{0}:{1}'.format(socket.peerAddress().toString(), socket.peerPort()) for socket in self.subscribers]
            data = 'SERVER:ADDRESSES:{0}\n'.format(','.join(addresses))
            return data
            
        def allPlayerNicknames():
            nicknames = [socket.nickname for socket in self.subscribers]
            data = 'SERVER:NICKNAMES:{0}\n'.format(','.join(nicknames))
            return data
            
        def inGamePlayers():
            message = 'Players in game: ' + ', '.join([socket.nickname for socket in self.subscribers if hasattr(socket, 'nickname')])
            data = 'CHAT:__SYSTEM__:{0}.\n'.format(message)
            return data
            
        DPRINT('handleData: ' + repr(data))
        
        if ':' not in data:
            return False
            
        (type_, content) = data.split(':', 1)
        
        if type_ == 'CHAT':  # example data: 'CHAT:amulet:Cave-Troll, WTF!?\n'
            self.broadcast(data)
                
        elif type_ == 'JOIN':  # example data: 'JOIN:amulet\n'
            nickname = content.rstrip()
            # bind nickname with socket
            (address, port) = (sourceSocket.peerAddress(), sourceSocket.peerPort())
            for socket in self.subscribers:
                if (address, port) == (socket.peerAddress(), socket.peerPort()):
                    socket.nickname = nickname
                    break
                    
            data = 'CHAT:__SYSTEM__:{0} has joined the game!\n'.format(nickname)
            self.broadcast(data)
            data = inGamePlayers()
            self.broadcast(data)
            
        elif type_ == 'QUIT':  # example data: 'QUIT:amulet\n'
            nickname = content.rstrip()
            data = 'CHAT:__SYSTEM__:{0} has left the game...\n'.format(nickname)
            self.broadcast(data)
            data = inGamePlayers()
            self.broadcast(data)
            
        elif type_ == 'CLIENT':
            content = content.rstrip()
            if content == 'READY':  # data == 'CLIENT:READY\n', client had selected deck to play
                for socket in self.subscribers:
                    if socket == sourceSocket:
                        socket.readied = True
                        break
                        
                # check if all Clients are readied
                allReadied = True
                for socket in self.subscribers:
                    if socket.readied == False:
                        allReadied = False
                        break
                if allReadied:
                    data = allPlayerAddresses()
                    self.broadcast(data)
                    data = allPlayerNicknames()
                    self.broadcast(data)
                    self.setup()
                    
        elif type_ == 'STATE':  # game state change
            # broadcast except source
            for socket in self.subscribers:
                if socket != sourceSocket:
                    self.writeDataToSocket(socket, data)
            
    def playerJoined(self):
        
        def dataIncoming(socket):
            def dataIncoming_():
                while socket.canReadLine():
                    data = str(socket.readLine())
                    self.handleData(data, socket)
            return dataIncoming_
            
        def playerLeft(socket):
            def playerLeft_():
                for socket_ in self.subscribers:
                    if socket == socket_:
                        self.subscribers.remove(socket)
                        data = 'QUIT:{0}\n'.format(socket.nickname)
                        self.handleData(data)
                        break
            return playerLeft_
            
        socket = self.nextPendingConnection()
        socket.disconnected.connect(playerLeft(socket))
        socket.readyRead.connect(dataIncoming(socket))
        self.subscribers.append(socket)
        DPRINT(str(socket.peerAddress().toString()) + ':' + str(socket.peerPort()) + ' connected!')
        self.sendVersionInfo(socket)
        
    def sendVersionInfo(self, socket):
        data = 'SERVER:VERSION:{0}\n'.format(VERSION)
        self.writeDataToSocket(socket, data)
        
    def setup(self):
        data = 'SERVER:SETUP:{0}\n'.format(self.parent.scenarioId)
        self.broadcast(data)
        
    def startNewGame(self):
        self.reset()
        data = 'SERVER:START_NEW_GAME\n'
        self.broadcast(data)
        
    def reset(self):
        '''for starting new game'''
        for socket in self.subscribers:
            socket.readied = False
            
    def startGame(self):
        '''bring MultiplayerMainWindow up from xxxxGameDialog'''
        self.close()  # stop listening incoming connections
        self.reset()
        data = 'SERVER:INITIALIZE_MAINWINDOW\n'
        self.broadcast(data)
        
    def farewell(self):
        data = 'CHAT:__SYSTEM__:SERVER CLOSED!\n'
        self.broadcast(data)
        data = 'SERVER:CLOSE\n'
        self.broadcast(data)
        
        for socket in self.subscribers:
            socket.setSocketState(QAbstractSocket.UnconnectedState)
        self.subscribers = []