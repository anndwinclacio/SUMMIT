#---------- SUMMIT TOOL EVALUATION - LSA ----------#

from PyRouge.pyrouge import Rouge
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_ROUGE_UI(object):

    def setupUi(self, ROUGE_UI):

        #---------- ROUGE UI WINDOW ----------#

        ROUGE_UI.setObjectName("ROUGE_UI")
        # ROUGE_UI.resize(1920, 1080)
        ROUGE_UI.showMaximized()
        # ROUGE_UI.setStyleSheet("background-color: white;")

        # ROUGE UI WINDOW - Icon Title Bar
        icon = QIcon()
        icon.addPixmap(QPixmap("logo.ico"), QIcon.Normal, QIcon.Off)
        ROUGE_UI.setWindowIcon(icon)
        ROUGE_UI.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(ROUGE_UI)
        self.centralwidget.setObjectName("centralwidget")

        # ROUGE UI WINDOW - SUMMIT Panel
        self.summitPanelBorder = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelBorder.setGeometry(QtCore.QRect(100, 50, 600, 872))
        self.summitPanelBorder.setStyleSheet("border: 8px solid #773E7C;\n" "border-radius: 30px;\n" "")
        self.summitPanelBorder.setText("")
        self.summitPanelBorder.setObjectName("summitPanelBorder")

        self.summitPanelHeaderSolid = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelHeaderSolid.setGeometry(QtCore.QRect(100, 90, 600, 45))
        self.summitPanelHeaderSolid.setStyleSheet("\n" "\n" "background: #773E7C;\n" "")
        self.summitPanelHeaderSolid.setText("")
        self.summitPanelHeaderSolid.setObjectName("summitPanelHeaderSolid")

        self.summitPanelHeaderRounded = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelHeaderRounded.setGeometry(QtCore.QRect(100, 50, 600, 85))
        self.summitPanelHeaderRounded.setStyleSheet("background: #773E7C;\n" "border-radius: 32px;\n" "")
        self.summitPanelHeaderRounded.setText("")
        self.summitPanelHeaderRounded.setObjectName("summitPanelHeaderRounded")

        self.summitPanelTextArea = QtWidgets.QTextEdit(self.centralwidget)
        self.summitPanelTextArea.setEnabled(True)
        self.summitPanelTextArea.setGeometry(QtCore.QRect(120, 150, 561, 751))
        self.summitPanelTextArea.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 18px;\n" "color: #000000;\n" "\n" "")
        self.summitPanelTextArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.summitPanelTextArea.setObjectName("summitPanelTextArea")

        self.summitPanelLabel = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelLabel.setGeometry(QtCore.QRect(232, 50, 336, 90))
        self.summitPanelLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n" "font-size: 40px;\n" "color: #FFFFFF;\n" "\n" "")
        self.summitPanelLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.summitPanelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.summitPanelLabel.setObjectName("summitPanelLabel")


        # ROUGE UI WINDOW - Reference Panel
        self.referencePanelBorder = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelBorder.setGeometry(QtCore.QRect(1220, 50, 600, 872))
        self.referencePanelBorder.setStyleSheet("border: 8px solid #773E7C;\n" "border-radius: 30px;\n" "")
        self.referencePanelBorder.setText("")
        self.referencePanelBorder.setObjectName("referencePanelBorder")

        self.referencePanelLabel = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelLabel.setGeometry(QtCore.QRect(1220, 50, 600, 90))
        self.referencePanelLabel.setStyleSheet("\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n" "font-size: 40px;\n" "color: #FFFFFF;\n" "\n" "")
        self.referencePanelLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.referencePanelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.referencePanelLabel.setObjectName("referencePanelLabel")

        self.referencePanelHeaderRounded = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelHeaderRounded.setGeometry(QtCore.QRect(1220, 50, 600, 85))
        self.referencePanelHeaderRounded.setStyleSheet("background: #773E7C;\n" "border-radius: 32px;\n" "")
        self.referencePanelHeaderRounded.setText("")
        self.referencePanelHeaderRounded.setObjectName("referencePanelHeaderRounded")

        self.referencePanelHeaderSolid = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelHeaderSolid.setGeometry(QtCore.QRect(1220, 90, 600, 45))
        self.referencePanelHeaderSolid.setStyleSheet("\n" "\n" "background: #773E7C;\n" "")
        self.referencePanelHeaderSolid.setText("")
        self.referencePanelHeaderSolid.setObjectName("referencePanelHeaderSolid")

        self.referencePanelTextArea = QtWidgets.QTextEdit(self.centralwidget)
        self.referencePanelTextArea.setEnabled(True)
        self.referencePanelTextArea.setGeometry(QtCore.QRect(1240, 150, 561, 751))
        self.referencePanelTextArea.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 18px;\n" "color: #000000;\n" "\n" "")
        self.referencePanelTextArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.referencePanelTextArea.setObjectName("referencePanelTextArea")


        # ROUGE UI WINDOW - BUTTONS
        # ROUGE UI WINDOW - Compute Button
        self.computeButton = QtWidgets.QPushButton(self.centralwidget)
        self.computeButton.setGeometry(QtCore.QRect(710, 920, 191, 60))
        self.computeButton.setStyleSheet("background: #773E7C;\n" "border-radius: 30px;\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n"
                                         "font-size: 24px;\n" "line-height: 30px;\n" "color: #FFFFFF;\n" "\n" "\n" "\n" "")
        self.computeButton.setObjectName("computeButton")
        compute = self.computeButton.clicked.connect(self._compute_rouge)


        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(1010, 920, 191, 60))
        self.clearButton.setStyleSheet("background: #773E7C;\n" "border-radius: 30px;\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n"
                                       "font-size: 24px;\n" "line-height: 30px;\n" "color: #FFFFFF;\n" "\n" "\n" "\n" "")
        self.clearButton.setObjectName("clearButton")
        clear = self.clearButton.clicked.connect(self._clear)



        # ROUGE UI WINDOW - Rouge Panel
        self.rougePanelBorder = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelBorder.setGeometry(QtCore.QRect(760, 220, 400, 539))
        self.rougePanelBorder.setStyleSheet("border: 8px solid #773E7C;\n" "border-radius: 30px;\n" "")
        self.rougePanelBorder.setText("")
        self.rougePanelBorder.setObjectName("rougePanelBorder")

        self.rougePanelHeaderRounded = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelHeaderRounded.setGeometry(QtCore.QRect(760, 226, 392, 51))
        self.rougePanelHeaderRounded.setStyleSheet("background: #773E7C;\n" "border-radius: 20px;\n" "")
        self.rougePanelHeaderRounded.setText("")
        self.rougePanelHeaderRounded.setObjectName("rougePanelHeaderRounded")

        self.rougePanelHeaderSolid = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelHeaderSolid.setGeometry(QtCore.QRect(761, 238, 391, 44))
        self.rougePanelHeaderSolid.setStyleSheet("\n" "\n" "background: #773E7C;\n" "")
        self.rougePanelHeaderSolid.setText("")
        self.rougePanelHeaderSolid.setObjectName("rougePanelHeaderSolid")

        self.rougePanelLabel = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelLabel.setGeometry(QtCore.QRect(760, 218, 400, 66))
        self.rougePanelLabel.setStyleSheet("\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n" "font-size: 30px;\n" "color: #FFFFFF;\n" "\n" "")
        self.rougePanelLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.rougePanelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rougePanelLabel.setObjectName("rougePanelLabel")

        self.precision = QtWidgets.QLabel(self.centralwidget)
        self.precision.setGeometry(QtCore.QRect(767, 360, 384, 41))
        self.precision.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 30px;\n"
                                     "line-height: 38px;\n" "text-align: center;\n" "color: #000000;\n" "\n" "")
        self.precision.setTextFormat(QtCore.Qt.MarkdownText)
        self.precision.setAlignment(QtCore.Qt.AlignCenter)
        self.precision.setObjectName("precision")

        self.precisionLabel = QtWidgets.QLabel(self.centralwidget)
        self.precisionLabel.setGeometry(QtCore.QRect(763, 300, 391, 32))
        self.precisionLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n" 
                                          "line-height: 30px;\n" "text-align: center;\n" "\n" "color: #000000;\n" "\n" "")
        self.precisionLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.precisionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.precisionLabel.setObjectName("precisionLabel")


        self.recall = QtWidgets.QLabel(self.centralwidget)
        self.recall.setGeometry(QtCore.QRect(767, 520, 384, 41))
        self.recall.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 30px;\n"
                                  "line-height: 38px;\n" "text-align: center;\n" "color: #000000;\n" "\n" "")
        self.recall.setTextFormat(QtCore.Qt.MarkdownText)
        self.recall.setAlignment(QtCore.Qt.AlignCenter)
        self.recall.setObjectName("recall")

        self.recallLabel = QtWidgets.QLabel(self.centralwidget)
        self.recallLabel.setGeometry(QtCore.QRect(761, 460, 401, 32))
        self.recallLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n"
                                       "line-height: 30px;\n" "text-align: center;\n" "\n" "color: #000000;\n" "\n" "")
        self.recallLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.recallLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recallLabel.setObjectName("recallLabel")


        self.fmeasure = QtWidgets.QLabel(self.centralwidget)
        self.fmeasure.setGeometry(QtCore.QRect(767, 680, 384, 41))
        self.fmeasure.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 30px;\n"
                                    "line-height: 38px;\n" "text-align: center;\n" "color: #000000;\n" "\n" "")
        self.fmeasure.setTextFormat(QtCore.Qt.MarkdownText)
        self.fmeasure.setAlignment(QtCore.Qt.AlignCenter)
        self.fmeasure.setObjectName("fmeasure")

        self.fmeasureLabel = QtWidgets.QLabel(self.centralwidget)
        self.fmeasureLabel.setGeometry(QtCore.QRect(851, 620, 218, 32))
        self.fmeasureLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n"
                                         "line-height: 30px;\n" "text-align: center;\n" "\n" "color: #000000;\n" "\n" "")
        self.fmeasureLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.fmeasureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fmeasureLabel.setObjectName("fmeasureLabel")

       
        
       
        self.referencePanelHeaderSolid.raise_()
        self.summitPanelBorder.raise_()
        self.summitPanelHeaderSolid.raise_()
        self.summitPanelHeaderRounded.raise_()
        self.summitPanelTextArea.raise_()
        self.summitPanelLabel.raise_()
        self.computeButton.raise_()
        self.referencePanelBorder.raise_()
        self.referencePanelHeaderRounded.raise_()
        self.referencePanelLabel.raise_()
        self.referencePanelTextArea.raise_()
        self.clearButton.raise_()
        self.rougePanelBorder.raise_()
        self.rougePanelHeaderRounded.raise_()
        self.rougePanelHeaderSolid.raise_()
        self.rougePanelLabel.raise_()
        self.precisionLabel.raise_()
        self.recallLabel.raise_()
        self.fmeasureLabel.raise_()
        self.precision.raise_()
        self.recall.raise_()
        self.fmeasure.raise_()
        ROUGE_UI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ROUGE_UI)
        self.statusbar.setObjectName("statusbar")
        ROUGE_UI.setStatusBar(self.statusbar)

        self.retranslateUi(ROUGE_UI)
        QtCore.QMetaObject.connectSlotsByName(ROUGE_UI)

    def retranslateUi(self, ROUGE_UI):
        _translate = QtCore.QCoreApplication.translate
        ROUGE_UI.setWindowTitle(_translate("ROUGE_UI", "ROUGE Metrics"))
        self.summitPanelTextArea.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Circular Std\'; font-size:18px; font-weight:448; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.summitPanelLabel.setText(_translate("ROUGE_UI", "SUMMIT"))
        self.computeButton.setText(_translate("ROUGE_UI", "COMPUTE"))
        self.referencePanelLabel.setText(_translate("ROUGE_UI", "REFERENCE SUMMARY"))
        self.clearButton.setText(_translate("ROUGE_UI", "CLEAR"))
        self.rougePanelLabel.setText(_translate("ROUGE_UI", "ROUGE METRICS"))
        self.precisionLabel.setText(_translate("ROUGE_UI", "PRECISION"))
        self.recallLabel.setText(_translate("ROUGE_UI", "RECALL"))
        self.fmeasureLabel.setText(_translate("ROUGE_UI", "F-MEASURE"))
        self.precision.setText(_translate("ROUGE_UI", "-"))
        self.recall.setText(_translate("ROUGE_UI", "-"))
        self.fmeasure.setText(_translate("ROUGE_UI", "-"))

    # COMPUTE BUTTON
    def _compute_rouge(self):
        r = Rouge()

        # GET TEXT FROM TEXTFIELDS
        summit = self.summitPanelTextArea.toPlainText()
        reference = self.referencePanelTextArea.toPlainText()

        # REMOVE NEW LINES FROM DOCUMENTS
        summit = summit.replace("\n","")
        reference = reference.replace("\n","")

        # REMOVE EXTRA DOUBLE QUOTATIONS FROM DOCUMENTS
        summit = summit.replace('"',"")
        reference = reference.replace('"',"")

        # COMPUTE FOR ROUGE
        [precisionValue, recallValue, fmeasureValue] = r.rouge_l([summit], [reference])

        self.precision.setText("  " + str(round(precisionValue,5)))
        self.recall.setText("  " + str(round(recallValue,5)))
        self.fmeasure.setText("  " + str(round(fmeasureValue,5)))

    # CLEAR BUTTON
    def _clear(self):
        self.summitPanelTextArea.setText("")
        self.precision.setText("-")
        self.recall.setText("")
        self.fmeasure.setText("")
        self.referencePanelTextArea.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ROUGE_UI = QtWidgets.QMainWindow()
    ui = Ui_ROUGE_UI()
    ui.setupUi(ROUGE_UI)
    ROUGE_UI.show()
    sys.exit(app.exec_())
