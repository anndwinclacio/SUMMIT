#---------- SUMMIT MAIN WINDOW ----------#

# FILE EXTRACTION LIBRARIES
from ctypes import alignment
import fitz
from uipkg.SUMMIT_HelpWindow import Ui_HelpWindow
from uipkg.SUMMIT_PromptWindow import Ui_InputPrompt

# NLP AND LSA PACKAGE
from lsapkg import lsa_summarizer, part_segmentation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import re
import os

from os import path
from tkinter import *
from tkinter import filedialog
import math

# UI LIBRARIES
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):

    #---------- HELP WINDOW ----------#

    def _help_window (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    #---------- PROMPT WINDOW ----------#

    def _prompt_window (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InputPrompt()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):

        #---------- MAIN WINDOW ----------#

        # MAIN WINDOW - Declaration
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.showMaximized()

        # MAIN WINDOW - Background Color
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        
        # MAIN WINDOW - Icon Title Bar
        icon = QIcon()
        icon.addPixmap(QPixmap("logo.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #---------- COURT CASE DOCUMENT ----------#

        # COURT CASE DOCUMENT FRAME - Declaration
        self.CCD_border = QLabel(self.centralwidget)
        self.CCD_border.setEnabled(True)
        self.CCD_border.setGeometry(QRect(110, 40, 621, 871))
        self.CCD_border.setAcceptDrops(False)
        self.CCD_border.setStyleSheet("border-radius:40px;\n"
                                      "border-color: rgb(119, 62, 124);\n"
                                      "border: 10px solid #773E7C;\n")
        self.CCD_border.setFrameShape(QFrame.Box)
        self.CCD_border.setFrameShadow(QFrame.Plain)
        self.CCD_border.setLineWidth(2)
        self.CCD_border.setMidLineWidth(9)
        self.CCD_border.setText("")
        self.CCD_border.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.CCD_border.setObjectName("CCD_border")

        # COURT CASE DOCUMENT FRAME - Background
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.CCD_border.setPalette(palette)

        # COURT CASE DOCUMENT - Frame Label and Color Filler
        self.label_CCD = QLabel(self.centralwidget)
        self.label_CCD.setGeometry(QRect(110, 40, 621, 61))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_CCD.setFont(font)
        self.label_CCD.setStyleSheet("color:rgb(255, 255, 255);background-color: rgb(119, 62, 124);border-radius:20px;")
        self.label_CCD.setAlignment(Qt.AlignCenter)
        self.label_CCD.setObjectName("label_CCD")
        self.colorFillerCCD = QLabel(self.centralwidget)
        self.colorFillerCCD.setGeometry(QRect(110, 60, 621, 41))
        self.colorFillerCCD.setStyleSheet("color:rgb(255, 255, 255);background-color: rgb(119, 62, 124);")
        self.colorFillerCCD.setText("")
        self.colorFillerCCD.setAlignment(Qt.AlignCenter)
        self.colorFillerCCD.setObjectName("colorFillerCCD")

        # COURT CASE DOCUMENT FRAME - Text Area 
        self.CD_display = QTextEdit(self.centralwidget)
        self.CD_display.setEnabled(False)
        self.CD_display.setGeometry(QRect(130, 110, 581, 781))

        # COURT CASE DOCUMENT FRAME - Text Area Background and Font 
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.CD_display.setPalette(palette)

        self.CD_display.setStyleSheet("font: 57 14pt \"Circular Std\";background-color: rgb(255, 255, 255)")
        self.CD_display.setInputMethodHints(Qt.ImhNone)
        self.CD_display.setFrameShape(QFrame.NoFrame)
        self.CD_display.setObjectName("CD_display")
        
        #---------- SUMMIT FRAME ----------#

        #  - Declaration
        self.SUMMIT_border = QLabel(self.centralwidget)
        self.SUMMIT_border.setEnabled(False)
        self.SUMMIT_border.setGeometry(QRect(790, 190, 341, 531))
        self.SUMMIT_border.setStyleSheet("border-radius:30px;\n"
                                         "border-color: rgb(119, 62, 124);\n"
                                         "background-color: rgb(255, 255, 255);border: 10px solid #773E7C;")
        self.SUMMIT_border.setFrameShape(QFrame.Box)
        self.SUMMIT_border.setFrameShadow(QFrame.Plain)
        self.SUMMIT_border.setLineWidth(2)
        self.SUMMIT_border.setMidLineWidth(9)
        self.SUMMIT_border.setText("")
        self.SUMMIT_border.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.SUMMIT_border.setObjectName("SUMMIT_border")

        # SUMMIT FRAME - Background
        palette = QPalette()
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        self.SUMMIT_border.setPalette(palette)

        # SUMMIT FRAME - Frame Label and Color Filler
        self.label_SUMMIT = QLabel(self.centralwidget)
        self.label_SUMMIT.setGeometry(QRect(790, 190, 341, 51))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_SUMMIT.setFont(font)
        self.label_SUMMIT.setStyleSheet("color:rgb(255, 255, 255);background-color: rgb(119, 62, 124);border-radius:20px;")
        self.label_SUMMIT.setAlignment(Qt.AlignCenter)
        self.label_SUMMIT.setObjectName("label_SUMMIT")

        self.colorFiller_SUMMIT = QLabel(self.centralwidget)
        self.colorFiller_SUMMIT.setGeometry(QRect(790, 220, 341, 21))
        self.colorFiller_SUMMIT.setStyleSheet("color:rgb(255, 255, 255);background-color: rgb(119, 62, 124);border-radius:20px;")
        self.colorFiller_SUMMIT.setText("")
        self.colorFiller_SUMMIT.setAlignment(Qt.AlignCenter)
        self.colorFiller_SUMMIT.setObjectName("colorFiller_SUMMIT")

        # SUMMIT FRAME - Court Case Document Section
        self.CD_description = QLabel(self.centralwidget)
        self.CD_description.setGeometry(QRect(790, 240, 341, 61))
        font = QFont()
        font.setFamily("Circular Std")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.CD_description.setFont(font)
        self.CD_description.setAlignment(Qt.AlignCenter)
        self.CD_description.setObjectName("CD_description")
    
        # SUMMIT FRAME - Court Case Document Section - Word Count
        self.CD_wordDescription = QLabel(self.centralwidget)
        self.CD_wordDescription.setGeometry(QRect(790, 300, 341, 31))
        font = QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CD_wordDescription.setFont(font)
        self.CD_wordDescription.setAlignment(Qt.AlignCenter)
        self.CD_wordDescription.setObjectName("CD_wordDescription")

        self.CD__word_display = QTextEdit(self.centralwidget)
        self.CD__word_display.setEnabled(False)
        self.CD__word_display.setGeometry(QRect(923, 330, 161, 51))
        self.CD__word_display.setStyleSheet("font: 57 20pt \"Circular Std Bold\";background-color: rgb(255, 255, 255);color: rgb(212, 175, 55);")
        self.CD__word_display.setInputMethodHints(Qt.ImhNone)
        self.CD__word_display.setFrameShape(QFrame.NoFrame)
        self.CD__word_display.setObjectName("CD__word_display")
        
        # SUMMIT FRAME - Court Case Document Section - Word Count Background
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.CD__word_display.setPalette(palette)
 
        # SUMMIT FRAME - Court Case Document Section - Sentence Count
        self.CD_sentenceDescription = QLabel(self.centralwidget)
        self.CD_sentenceDescription.setGeometry(QRect(790, 380, 341, 31))
        font = QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CD_sentenceDescription.setFont(font)
        self.CD_sentenceDescription.setAlignment(Qt.AlignCenter)
        self.CD_sentenceDescription.setObjectName("CD_sentenceDescription")

        self.CD__sentence_display = QTextEdit(self.centralwidget)
        self.CD__sentence_display.setEnabled(False)
        self.CD__sentence_display.setGeometry(QRect(930, 410, 161, 51))
        self.CD__sentence_display.setStyleSheet("font: 57 20pt \"Circular Std Bold\";background-color: rgb(255, 255, 255);color: rgb(212, 175, 55);")
        self.CD__sentence_display.setInputMethodHints(Qt.ImhNone)
        self.CD__sentence_display.setFrameShape(QFrame.NoFrame)
        self.CD__sentence_display.setObjectName("CD__sentence_display")

        # SUMMIT FRAME - Court Case Document Section - Sentence Count Background
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(120, 120, 120, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(120, 120, 120, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.CD__sentence_display.setPalette(palette)
  
        # SUMMIT FRAME - Line
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(790, 460, 341, 28))
        self.line.setStyleSheet("color: rgb(119, 62, 124);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        # SUMMIT FRAME - Summary Section
        self.SUM_description = QLabel(self.centralwidget)
        self.SUM_description.setGeometry(QRect(790, 480, 341, 61))
        font = QFont()
        font.setFamily("Circular Std")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.SUM_description.setFont(font)
        self.SUM_description.setAlignment(Qt.AlignCenter)
        self.SUM_description.setObjectName("SUM_description")

        # SUMMIT FRAME - Summary Section - Word Count
        self.SUM_wordDescription = QLabel(self.centralwidget)
        self.SUM_wordDescription.setGeometry(QRect(790, 540, 341, 31))
        font = QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SUM_wordDescription.setFont(font)
        self.SUM_wordDescription.setAlignment(Qt.AlignCenter)
        self.SUM_wordDescription.setObjectName("SUM_wordDescription")

        self.SUM__word_display = QTextEdit(self.centralwidget)
        self.SUM__word_display.setEnabled(False)
        self.SUM__word_display.setGeometry(QRect(930, 570, 161, 51))
        self.SUM__word_display.setStyleSheet("font: 57 20pt \"Circular Std Bold\";background-color: rgb(255, 255, 255);color: rgb(212, 175, 55);")
        self.SUM__word_display.setInputMethodHints(Qt.ImhNone)
        self.SUM__word_display.setFrameShape(QFrame.NoFrame)
        self.SUM__word_display.setObjectName("SUM__word_display")

        # SUMMIT FRAME - Summary Section - Word Count Background
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(120, 120, 120, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(120, 120, 120, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.SUM__word_display.setPalette(palette)

        # SUMMIT FRAME - Summary Section - Sentence Count
        self.SUM_sentenceDescription = QLabel(self.centralwidget)
        self.SUM_sentenceDescription.setGeometry(QRect(790, 620, 341, 31))
        font = QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SUM_sentenceDescription.setFont(font)
        self.SUM_sentenceDescription.setAlignment(Qt.AlignCenter)
        self.SUM_sentenceDescription.setObjectName("SUM_sentenceDescription")

        self.SUM__sentence_display = QTextEdit(self.centralwidget)
        self.SUM__sentence_display.setEnabled(False)
        self.SUM__sentence_display.setGeometry(QRect(935, 650, 161, 51))
        self.SUM__sentence_display.setStyleSheet("font: 57 20pt \"Circular Std Bold\";background-color: rgb(255, 255, 255);color: rgb(212, 175, 55);")
        self.SUM__sentence_display.setInputMethodHints(Qt.ImhNone)
        self.SUM__sentence_display.setFrameShape(QFrame.NoFrame)
        self.SUM__sentence_display.setObjectName("SUM__sentence_display")

        # SUMMIT FRAME - Summary Section - Sentence Count Background
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(120, 120, 120, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(119, 62, 124))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(120, 120, 120, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.SUM__sentence_display.setPalette(palette)

        #---------- SUMMARIZED VERSION FRAME ----------#

        # SUMMARIZED VERSION FRAME  - Declaration
        self.SV_border = QLabel(self.centralwidget)
        self.SV_border.setEnabled(True)
        self.SV_border.setGeometry(QRect(1190, 40, 621, 871))
        self.SV_border.setAcceptDrops(False)
        self.SV_border.setStyleSheet("border-radius:40px;\n"
                                     "border-color: rgb(119, 62, 124);\n"
                                     "border: 10px solid #773E7C;\n")
        self.SV_border.setFrameShape(QFrame.Box)
        self.SV_border.setFrameShadow(QFrame.Plain)
        self.SV_border.setLineWidth(2)
        self.SV_border.setMidLineWidth(9)
        self.SV_border.setText("")
        self.SV_border.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.SV_border.setObjectName("SV_border")

        # SUMMARIZED VERSION FRAME - Background
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.SV_border.setPalette(palette)
       
        # SUMMARIZED VERSION FRAME - Frame Label and Color Filler
        self.label_SV = QLabel(self.centralwidget)
        self.label_SV.setGeometry(QRect(1190, 40, 621, 61))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_SV.setFont(font)
        self.label_SV.setStyleSheet("color:rgb(255, 255, 255);background-color: rgb(119, 62, 124);border-radius:20px;")
        self.label_SV.setAlignment(Qt.AlignCenter)
        self.label_SV.setObjectName("label_SV")

        self.colorFillerSV = QLabel(self.centralwidget)
        self.colorFillerSV.setGeometry(QRect(1190, 80, 621, 21))
        self.colorFillerSV.setFont(font)
        self.colorFillerSV.setStyleSheet("color:rgb(255, 255, 255);background-color: rgb(119, 62, 124);")
        self.colorFillerSV.setText("")
        self.colorFillerSV.setAlignment(Qt.AlignCenter)
        self.colorFillerSV.setObjectName("colorFillerSV")
       
        # SUMMARIZED VERSION FRAME - Text Area 
        self.SV_display = QTextEdit(self.centralwidget)
        self.SV_display.setEnabled(False)
        self.SV_display.setGeometry(QRect(1210, 110, 581, 781))

        # SUMMARIZED VERSION FRAME - Text Area Background and Font
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.SV_display.setPalette(palette)

        self.SV_display.setFont(font)
        self.SV_display.setStyleSheet("font: 57 14pt \"Circular Std\";background-color: rgb(255, 255, 255)")
        self.SV_display.setInputMethodHints(Qt.ImhNone)
        self.SV_display.setFrameShape(QFrame.NoFrame)
        self.SV_display.setObjectName("SV_display")

        #---------- BUTTONS ----------#

        # INPUT DOCUMENT BUTTON
        self.button_input = QPushButton(self.centralwidget)
        self.button_input.setGeometry(QRect(260, 930, 321, 51))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_input.setToolTip('Open Case Document')
        self.button_input.setFont(font)
        self.button_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_input.setStyleSheet("QPushButton:hover{background-color: rgb(208, 181, 213);\n"
                                        "border-radius: 25px;\n"
                                        "font:rgb(255, 255, 255);\n"
                                        "color:white;}\n"
                                        "\n"
                                        "QPushButton{background-color: rgb(208, 181, 213);\n"
                                        "    background-color: rgb(119, 62, 124);\n"
                                        "border-radius: 25px;\n"
                                        "font:rgb(255, 255, 255);\n"
                                        "color:white;}")                                
        self.button_input.setObjectName("button_input")
        self.button_input.clicked.connect(self._input_document)

        # SUMMIT! BUTTON
        self.button_summit = QPushButton(self.centralwidget)
        self.button_summit.setGeometry(QRect(840, 930, 231, 61))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_summit.setToolTip('Summarize the Document')
        self.button_summit.setFont(font)
        self.button_summit.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_summit.setStyleSheet("QPushButton:hover{background-color: rgb(208, 181, 213);\n"
                                         "border-radius: 30px;\n"
                                         "font:rgb(255, 255, 255);\n"
                                         "color:white;}\n"
                                         "\n"
                                         "QPushButton{background-color: rgb(208, 181, 213);\n"
                                         "    background-color: rgb(119, 62, 124);\n"
                                         "border-radius: 30px;\n"
                                         "font:rgb(255, 255, 255);\n"
                                         "color:white;}")
        self.button_summit.setObjectName("button_summit")
        self.button_summit.clicked.connect(self._summit_button)

        # EXPORT BUTTON
        self.button_export = QPushButton(self.centralwidget)
        self.button_export.setGeometry(QRect(1340, 930, 321, 51))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_export.setToolTip('Save the Summarized Version in a Text File')
        self.button_export.setFont(font)
        self.button_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_export.setStyleSheet("QPushButton:hover{background-color: rgb(208, 181, 213);\n"
                                         "border-radius: 25px;\n"
                                         "font:rgb(255, 255, 255);\n"
                                         "color:white;}\n"
                                         "\n"
                                         "QPushButton{background-color: rgb(208, 181, 213);\n"
                                         "    background-color: rgb(119, 62, 124);\n"
                                         "border-radius: 25px;\n"
                                         "font:rgb(255, 255, 255);\n"
                                         "color:white;}")
        self.button_export.setObjectName("button_export")
        self.button_export.clicked.connect(self._export_file)

        # HELP BUTTON
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(20, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.help_button.setFont(font)
        self.help_button.setStyleSheet("QPushButton:hover{background-color: rgb(208, 181, 213);\n"
                                         "border-radius: 20px;\n"
                                         "font:rgb(255, 255, 255);\n"
                                         "color:white;}\n"
                                         "\n"
                                      "QPushButton{background-color: rgb(119, 62, 124);\n"
                                      "border-radius: 20px;\n"
                                      "font:rgb(255, 255, 255);\n"
                                      "color:white;}")
        self.help_button.setObjectName("help_button")

        self.help_button.clicked.connect(self._help_window)

        #MainWindow.setCentralWidget(self.centralwidget)

        #---------- DECLARED OBJECTS ----------#

        # CALLING THE DECLARED OBJECTS
        self.SV_border.raise_()
        self.CCD_border.raise_()
        self.colorFillerCCD.raise_()
        self.SUMMIT_border.raise_()
        self.CD_description.raise_()
        self.CD_wordDescription.raise_()
        self.label_CCD.raise_()
        self.button_input.raise_()
        self.button_summit.raise_()
        self.button_export.raise_()
        self.help_button.raise_()
        self.colorFillerSV.raise_()
        self.label_SV.raise_()
        self.CD_display.raise_()
        self.SV_display.raise_()
        self.colorFiller_SUMMIT.raise_()
        self.label_SUMMIT.raise_()
        self.line.raise_()
        self.CD_sentenceDescription.raise_()
        self.SUM_description.raise_()
        self.SUM_wordDescription.raise_()
        self.SUM_sentenceDescription.raise_()
        self.CD__word_display.raise_()
        self.CD__sentence_display.raise_()
        self.SUM__word_display.raise_()
        self.SUM__sentence_display.raise_()

        # IMPLEMENTATION OF THE DECLARED WINDOW
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #---------- FUNCTIONS ----------#

    # FUNCTION FOR RETRANSLATE UI (SETTING-UP)
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SUMMIT"))
        self.CD_description.setText(_translate("MainWindow", "CASE DOCUMENT"))
        self.CD_wordDescription.setText(_translate("MainWindow", "TOTAL NUMBER OF WORDS:"))
        self.label_CCD.setText(_translate("MainWindow", "COURT CASE DOCUMENT"))
        self.label_SUMMIT.setText(_translate("MainWindow", "SUMMIT"))
        self.label_SV.setText(_translate("MainWindow", "SUMMARIZED VERSION"))
        self.button_input.setText(_translate("MainWindow", "INPUT DOCUMENT"))
        self.button_summit.setText(_translate("MainWindow", "SUMMIT!"))
        self.button_export.setText(_translate("MainWindow", "EXPORT"))
        self.help_button.setText(_translate("MainWindow", "?"))
        self.CD_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Circular Std\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SV_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Circular Std\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CD_sentenceDescription.setText(_translate("MainWindow", "TOTAL NUMBER OF SENTENCES:"))
        self.SUM_description.setText(_translate("MainWindow", "SUMMARY"))
        self.SUM_wordDescription.setText(_translate("MainWindow", "TOTAL NUMBER OF WORDS:"))
        self.SUM_sentenceDescription.setText(_translate("MainWindow", "TOTAL NUMBER OF SENTENCES:"))
        self.CD__word_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Circular Std\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CD__sentence_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Circular Std\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SUM__word_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Circular Std\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SUM__sentence_display.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'Circular Std\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

    #---------- BUTTON FUNCTIONS ----------#

    # INPUT DOCUMENT BUTTON
    def _input_document(self):
        root = Tk()
        root.withdraw()
        
        self.CD_display.setText("")
        self.SV_display.setText("")
        self.SV_display.setText("")
        self.CD__word_display.setText("")
        self.CD__sentence_display.setText("")
        self.SUM__word_display.setText("")
        self.SUM__sentence_display.setText("")

        text = "" 
        
        tf = filedialog.askopenfilename(initialdir="C:/Users/MainFrame/Desktop/", 
                                        title="Open Case Document",
                                        defaultextension=".txt",
                                        filetypes=(("Text Document", "*.txt"),("All Files", "*.*")))

        print(tf)
        if not tf:
            return ()

        file_name, file_extension = os.path.splitext(tf)
        
        if file_extension != ".txt":
            self._prompt_window()
        else: 
            global paragraphs
            with open(tf, encoding='utf-8') as f:
                paragraphs = f.readlines()


            for line in paragraphs:
                text += line
            
            self.CD_display.setText(text)
            self.CD_display.setEnabled(True)
            self.CD_display.setReadOnly(True)


    # SUMMIT BUTTON
    def _summit_button(self):

        self.SV_display.setText("")
        self.CD__word_display.setText("")
        self.CD__sentence_display.setText("")
        self.SUM__word_display.setText("")
        self.SUM__sentence_display.setText("")

        # CD_text = self.CD_display.toPlainText()

        # if not CD_text:
        #     return ()
        

        # CLEANING OF PARAGRAPHS
        cleaned_paragraphs = []
        for sentence in paragraphs:
            sentence = sentence.replace("\n", "")
            sentence = sentence.replace("’","'")
            cleaned_paragraphs.append(sentence)

        print("\n\n---COURT CASE DOCUMENT----\n")  
        print(cleaned_paragraphs)

        word_tokenizer = lsa_summarizer.LSA_Summarizer()._words_tokenize
        sentence_splitter = lsa_summarizer.LSA_Summarizer()._sentence_splitter

        sentences_count_cd = len(sentence_splitter(cleaned_paragraphs))
        words_count_cd = len(word_tokenizer(cleaned_paragraphs))
        

        # PART SEGMENTATION
        part_segment = part_segmentation.Part_Segmentation()

        title_sentences, noc_sentences, facts_sentences, facts_count, issues_sentences, issues_count, ruling_sentences, ruling_fsentences, ruling_count = part_segment(cleaned_paragraphs)


        # LSA 
        summarize = lsa_summarizer.LSA_Summarizer()

        summary_facts = summarize(facts_sentences, facts_count)
        summary_issues = summarize(issues_sentences,issues_count)
        summary_ruling = summarize(ruling_sentences, ruling_count)


        # CLEANING OF SUMMARY
        cleaning_summary = part_segmentation.Part_Segmentation()._cleaning_of_summary

        title, noc, facts, issues, ruling = cleaning_summary(title_sentences, noc_sentences, summary_facts, summary_issues, summary_ruling, ruling_fsentences)

        summary = "TITLE\n\n" + title + "\n\n\nNATURE OF THE CASE\n\n" + noc + "\n\n\nFACTS\n\n" + facts + "\n\n\nISSUES\n\n" + issues + "\n\n\nRULING\n\n" + ruling

        self.SV_display.setText(summary)
        self.SV_display.setEnabled(True)
        self.SV_display.setReadOnly(True)

        SV_content = self.SV_display.toPlainText()

        # Sentence Tokenize
        list_abbrev_law = ['ca-g.r', 'ca-gr', 'g.r', 'cr-h.c', 'no', 'nos', 'r.a', 'col', 'u.s', 'a.m', 'p.m', 'st', 'brgy', 'inc', 'a.k.a', 'atty', 'dr', 'mr', 'ms', 'mrs.', 'insp', 'asst', 'pros', 'nos', 'sec']
        punkt_param = PunktParameters()
        punkt_param.abbrev_types = set(list_abbrev_law)
        sentence_splitter = PunktSentenceTokenizer(punkt_param)
        sentences_summary = sentence_splitter.tokenize(SV_content)

        sentences_count_sv = len(sentences_summary)
        words_count_sv = len(word_tokenizer(sentences_summary))
        

        # Word Count - Case Document
        self.CD__word_display.setText(str(words_count_cd))
        self.CD__word_display.setEnabled(True)
        self.CD__word_display.setReadOnly(True)

        # Sentence Count - Case Document
        self.CD__sentence_display.setText(str(sentences_count_cd))
        self.CD__sentence_display.setEnabled(True)
        self.CD__sentence_display.setReadOnly(True)

        # Word Count - Summary
        self.SUM__word_display.setText(str(words_count_sv))
        self.SUM__word_display.setEnabled(True)
        self.SUM__word_display.setReadOnly(True)

        # Sentence Count - Summary
        self.SUM__sentence_display.setText(str(sentences_count_sv))
        self.SUM__sentence_display.setEnabled(True)
        self.SUM__sentence_display.setReadOnly(True)


    # EXPORT BUTTON
    def _export_file(self):
        root= Tk()
        root.withdraw()

        SV_text = self.SV_display.toPlainText()
        if not SV_text:
            return ()   
        
        tf = filedialog.asksaveasfile(mode='w',
                                      title ="Save file",
                                      defaultextension=".txt",
                                      filetypes=(("Text file", "*.txt"),("All Files", "*.*")))
        
        if not tf:
            return ()                              
        
        tf.write(SV_text)
        tf.close()
