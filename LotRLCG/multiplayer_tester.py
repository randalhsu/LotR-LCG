import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtTest import *
from JoinGameDialog import *
from HostGameDialog import *


hostGameDialog = None
joinGameDialog = None


def startServer():
    global hostGameDialog
    hostGameDialog.move(0, -100)
    hostGameDialog.show()
    hostGameDialog.hostButton.click()
    QTest.keyPress(hostGameDialog.hostingLineEdit, Qt.Key_C, Qt.ControlModifier)
    QTest.keyRelease(hostGameDialog.hostingLineEdit, Qt.Key_C, Qt.ControlModifier)


def startClient():
    global joinGameDialog
    joinGameDialog.move(joinGameDialog.width(), 0)
    joinGameDialog.show()
    QTest.keyPress(joinGameDialog.addressLineEdit, Qt.Key_V, Qt.ControlModifier)
    QTest.keyRelease(joinGameDialog.addressLineEdit, Qt.Key_V, Qt.ControlModifier)
    joinGameDialog.joinButton.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hostGameDialog = HostGameDialog()
    joinGameDialog = JoinGameDialog()
    startServer()
    QTimer.singleShot(500, startClient)
    sys.exit(app.exec_())