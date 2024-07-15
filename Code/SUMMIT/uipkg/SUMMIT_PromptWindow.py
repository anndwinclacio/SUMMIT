#---------- SUMMIT PROMPT WINDOW ----------#

# UI LIBRARIES
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_InputPrompt(object):
    def setupUi(self, InputPrompt):

        #---------- PROMPT WINDOW ----------#

        # PROMPT WINDOW - Declaration
        InputPrompt.setObjectName("InputPrompt")
        InputPrompt.resize(385, 180)
        InputPrompt.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)

        # PROMPT WINDOW - Icon Title Bar
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("prompt_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InputPrompt.setWindowIcon(icon)

        # PROMPT WINDOW - Background
        InputPrompt.setStyleSheet("background-color:rgb(255, 255, 255);\n""")
        InputPrompt.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(InputPrompt)
        self.centralwidget.setObjectName("centralwidget")

        # LABEL - SUMMIT only accepts input
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # LABEL - documents in .txt format.
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 70, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")

        # LABEL - Please select a different file.
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 100, 251, 60))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # LABEL - .txt
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(203, 65, 31, 31))
        self.label_6.setStyleSheet("color: rgb(119, 62, 124)")
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(14)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        InputPrompt.setCentralWidget(self.centralwidget)

        self.retranslateUi(InputPrompt)
        QtCore.QMetaObject.connectSlotsByName(InputPrompt)

    def retranslateUi(self, InputPrompt):
        _translate = QtCore.QCoreApplication.translate
        InputPrompt.setWindowTitle(_translate("InputPrompt", "ERROR!"))
        self.label_3.setText(_translate("InputPrompt", "SUMMIT only accepts input"))
        self.label_4.setText(_translate("InputPrompt", "documents in .txt format."))
        self.label_5.setText(_translate("InputPrompt", "Please select a different file."))
        self.label_6.setText(_translate("InputPrompt", ".txt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputPrompt = QtWidgets.QMainWindow()
    ui = Ui_InputPrompt()
    ui.setupUi(InputPrompt)
    InputPrompt.show()
    sys.exit(app.exec_())
