#---------- SUMMIT LOADING WINDOW ----------#

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)

from PySide2.QtWidgets import *

class Ui_summitLoading(object):

    def setupUi(self, summitLoading):

        #---------- MAIN WINDOW ----------#

        # MAIN WINDOW - Declaration
        summitLoading.setObjectName("summitLoading")
        summitLoading.resize(1920, 1080)
        self.centralwidget = QWidget(summitLoading)
        self.centralwidget.setObjectName("centralwidget")

        # MAIN WINDOW - Vertical Layout
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # MAIN WINDOW - Drop Shadow Frame
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame#dropShadowFrame{    \n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.477508, y1:0, x2:0.493, y2:0.994, stop:0 rgba(97, 37, 101, 255), stop:1 rgba(204, 181, 213, 255));\n"
                                           "    color: rgb(220, 220, 220);\n"
                                           "    border-radius: 10px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")

        # MAIN WINDOW - Progress Bar
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QRect(820, 973, 241, 20))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    \n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "    border-style: none;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: rgb(157, 117, 163)\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        # MAIN WINDOW - SUMMIT Label
        self.label = QLabel(self.dropShadowFrame)
        self.label.setGeometry(QRect(0, 390, 1901, 231))
        font = QFont()
        font.setFamily("Circular Std Black")
        font.setPointSize(110)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        # MAIN WINDOW - Summarize It! Label
        self.label_2 = QLabel(self.dropShadowFrame)
        self.label_2.setGeometry(QRect(0, 490, 1901, 231))
        font = QFont()
        font.setFamily("Circular Std Bold Italic")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(208, 181, 213);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # MAIN WINDOW - Icon
        self.label_3 = QLabel(self.dropShadowFrame)
        self.label_3.setGeometry(QRect(0, 290, 1901, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QPixmap("SUMMIT Logo.png"))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        summitLoading.setCentralWidget(self.centralwidget)

        self.retranslateUi(summitLoading)
        QMetaObject.connectSlotsByName(summitLoading)
    
    #---------- FUNCTIONS ----------#

    # FUNCTION FOR RETRANSLATE UI (SETTING-UP)
    def retranslateUi(self, summitLoading):
        _translate = QCoreApplication.translate
        summitLoading.setWindowTitle(_translate("summitLoading", "MainWindow"))
        self.label.setText(_translate("summitLoading", "SUMMIT"))
        self.label_2.setText(_translate("summitLoading", "Summarize It!"))

