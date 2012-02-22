from LotRLCG import *


mainWindow = None
deckBuilder = None


class Launcher(QDialog):
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)
        
        size = QSize(250, 50)
        soloButton = QPushButton(QIcon('./resource/image/LotRLCG.ico'), self.tr('&Solo Game'))
        soloButton.setMinimumSize(size)
        soloButton.clicked.connect(self.startSoloGame)
        soloButton.setDefault(True)
        deckBuilderButton = QPushButton(QIcon('./resource/image/DeckBuilder.ico'), self.tr('&Deck Builder'))
        deckBuilderButton.setMinimumSize(size)
        deckBuilderButton.clicked.connect(self.startDeckBuilder)
        quitButton = QPushButton(self.tr('&Quit'))
        quitButton.setMinimumSize(size)
        quitButton.clicked.connect(self.close)
        
        layout = QVBoxLayout()
        layout.addWidget(soloButton)
        layout.addWidget(deckBuilderButton)
        layout.addWidget(quitButton)
        self.setLayout(layout)
        self.setMinimumWidth(300)
        self.setWindowTitle(self.tr('LotR: LCG Launcher'))
        
    def startSoloGame(self):
        self.close()
        global mainWindow  # use global variable so it won't be cleaned up immediately after this method ends
        mainWindow = MainWindow()
        mainWindow.show()
        
    def startDeckBuilder(self):
        self.close()
        global deckBuilder
        deckBuilder = DeckBuilder()
        deckBuilder.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec_())
    