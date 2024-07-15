#---------- SUMMIT HELP WINDOW ----------#

# UI LIBRARIES
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class Ui_HelpWindow(object):

    def setupUi(self, HelpWindow):

        #---------- HELP WINDOW ----------#

        # HELP WINDOW - Declaration
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(800, 531)
        HelpWindow.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)

        # MAIN WINDOW - Icon Title Bar
        help_icon = QIcon()
        help_icon.addPixmap(QPixmap("help.ico"), QIcon.Normal, QIcon.Off)
        HelpWindow.setWindowIcon(help_icon)
        HelpWindow.setAnimated(True)
        self.centralwidget = QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")

        # HELP WINDOW - Background
        HelpWindow.setAutoFillBackground(False)
        HelpWindow.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")

        # LABEL - Upload the Case Document
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # LABEL 2 - Click the INPUT DOCUMENT 
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # PUSHBUTTON - Input Document Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(119, 62, 124);\n"
                                      "border-radius: 15px;\n"
                                      "font:rgb(255, 255, 255);\n"
                                      "color:white;")
        self.pushButton.setObjectName("pushButton")

        # LABEL 3 - button to import your case document
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 90, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # LABEL 4 - Summarize the Case Document
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # LABEL 5 - Click the
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 220, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # PUSHBUTTON 2 - SUMMIT Button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(119, 62, 124);\n"
                                        "border-radius: 15px;\n"
                                        "font:rgb(255, 255, 255);\n"
                                        "color:white;")
        self.pushButton_2.setObjectName("pushButton_2")


        # LABEL 6 - button to begin the summarization
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 220, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        # LABEL 7 - Save the Summarized Version
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 300, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        # LABEL 8 - Click the
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 360, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        # PUSHBUTTON 3 - SUMMIT Button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(119, 62, 124);\n"
                                        "border-radius: 15px;\n"
                                        "font:rgb(255, 255, 255);\n"
                                        "color:white;")
        self.pushButton_3.setObjectName("pushButton_3")

        # LABEL 9 - button to export the final output in .txt format
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 360, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        # LABEL 10 - Note
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 440, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book Italic")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(156, 156, 156)")
        self.label_10.setObjectName("label_10")
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Help"))
        self.label.setText(_translate("HelpWindow", "Upload the Case Document"))
        self.label_2.setText(_translate("HelpWindow", "Click the"))
        self.pushButton.setText(_translate("HelpWindow", "INPUT DOCUMENT"))
        self.label_3.setText(_translate("HelpWindow", "button to import your case document."))
        self.label_4.setText(_translate("HelpWindow", "Summarize the Case Document"))
        self.label_5.setText(_translate("HelpWindow", "Click the"))
        self.pushButton_2.setText(_translate("HelpWindow", "SUMMIT"))
        self.label_6.setText(_translate("HelpWindow", "button to begin the summarization."))
        self.label_7.setText(_translate("HelpWindow", "Save the Summarized Version"))
        self.label_8.setText(_translate("HelpWindow", "Click the "))
        self.label_9.setText(_translate("HelpWindow", "button to export the final output in .txt format."))
        self.pushButton_3.setText(_translate("HelpWindow", "EXPORT"))
        self.label_10.setText(_translate("HelpWindow", "Note: SUMMIT will only accept TXT input documents."))

     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())
