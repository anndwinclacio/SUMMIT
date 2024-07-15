#---------- SUMMIT APPLICATION ----------#

# UI LIBRARIES
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

#---------- SUMMIT SPLASH SCREEN ----------#
from uipkg.SUMMIT_Splash import Ui_summitLoading

#---------- SUMMIT MAIN WINDOW ----------#
from uipkg.SUMMIT_Main import Ui_MainWindow

## ==> GLOBALS
counter = 0

#---------- SUMMIT MAIN WINDOW ----------#
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#---------- SUMMIT SPLASH SCREEN ----------#
class summitLoading(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_summitLoading()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # QTIMER --> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        
        # TIMER IN MILLISECONDS
        self.timer.start(50)

        # SHOW --> MAIN WINDOW
        self.show()

    #---------- FUNCTIONS ----------#

    # PROGRESS FUNCTION
    def progress(self):
        
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1
        
#---------- MAIN FUNCTION OF SYSTEM ----------#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = summitLoading()
    sys.exit(app.exec_())
