from LotRLCG import *


mainWindow = None
hostGameDialog = None
joinGameDialog = None
deckBuilder = None


class Launcher(QDialog):
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)
        self.createUI()
        
    def startSoloGame(self):
        self.close()
        global mainWindow  # use global variable so it won't be cleaned up immediately after this method ends
        mainWindow = MainWindow()
        mainWindow.show()
        
    def startHostingGame(self):
        self.close()
        global hostGameDialog
        hostGameDialog = HostGameDialog()
        hostGameDialog.show()
        
    def startJoiningGame(self):
        self.close()
        global joinGameDialog
        joinGameDialog = JoinGameDialog()
        joinGameDialog.show()
        
    def startDeckBuilder(self):
        self.close()
        global deckBuilder
        deckBuilder = DeckBuilder()
        deckBuilder.show()
        
    def createUI(self):
        icon = QIcon('./resource/image/LotRLCG.ico')
        
        soloButton = QPushButton(icon, self.tr('     &Solo Game     '))
        soloButton.clicked.connect(self.startSoloGame)
        soloButton.setDefault(True)
        
        multiplayerMenu = QMenu()
        multiplayerMenu.addAction(self.tr('&Host Game'), self.startHostingGame)
        multiplayerMenu.addAction(self.tr('&Join Game'), self.startJoiningGame)
        
        multiplayerButton = QPushButton(QIcon('./resource/image/LotRLCG_MP.ico'), self.tr('&Multiplayer Game'))
        multiplayerButton.setMenu(multiplayerMenu)
        
        deckBuilderButton = QPushButton(QIcon('./resource/image/DeckBuilder.ico'), self.tr('    &Deck Builder    '))
        deckBuilderButton.clicked.connect(self.startDeckBuilder)
        
        quitButton = QPushButton(QIcon('./resource/image/exit.ico'), self.tr('           &Quit           '))
        quitButton.clicked.connect(self.close)
        
        layout = QVBoxLayout()
        
        buttons = (soloButton, multiplayerButton, deckBuilderButton, quitButton)
        for button in buttons:
            button.setMinimumSize(QSize(200, 50))
            button.setIconSize(QSize(24, 24))
            layout.addWidget(button)
            
        self.setLayout(layout)
        
        self.adjustSize()
        self.resize(300, self.height())
        self.setWindowIcon(icon)
        self.setWindowTitle(self.tr('LotR: LCG Launcher'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec_())