#---------- SUMMIT TOOL EVALUATION - LSA AND PART SEGMENTATION ----------#

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
        ROUGE_UI.setStyleSheet("background-color: white;")


        # ROUGE UI WINDOW - Icon Title Bar
        icon = QIcon()
        icon.addPixmap(QPixmap("logo.ico"), QIcon.Normal, QIcon.Off)
        ROUGE_UI.setWindowIcon(icon)
        ROUGE_UI.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(ROUGE_UI)
        self.centralwidget.setObjectName("centralwidget")


        # ROUGE UI WINDOW - SUMMIT Panel
        self.summitPanelBorder = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelBorder.setGeometry(QtCore.QRect(100, 112, 600, 730))
        self.summitPanelBorder.setStyleSheet("border: 8px solid #773E7C;\n" "border-radius: 30px;\n" "")
        self.summitPanelBorder.setText("")
        self.summitPanelBorder.setObjectName("summitPanelBorder")

        self.summitPanelHeaderSolid = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelHeaderSolid.setGeometry(QtCore.QRect(100, 157, 600, 45))
        self.summitPanelHeaderSolid.setStyleSheet("\n" "\n" "background: #773E7C;\n" "")
        self.summitPanelHeaderSolid.setText("")
        self.summitPanelHeaderSolid.setObjectName("summitPanelHeaderSolid")

        self.summitPanelHeaderRounded = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelHeaderRounded.setGeometry(QtCore.QRect(100, 112, 600, 85))
        self.summitPanelHeaderRounded.setStyleSheet("background: #773E7C;\n" "border-radius: 32px;\n" "")
        self.summitPanelHeaderRounded.setText("")
        self.summitPanelHeaderRounded.setObjectName("summitPanelHeaderRounded")

        self.summitPanelLabel = QtWidgets.QLabel(self.centralwidget)
        self.summitPanelLabel.setGeometry(QtCore.QRect(232, 112, 336, 90))
        self.summitPanelLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n"
                                            "font-size: 40px;\n" "color: #FFFFFF;\n" "background: #773E7C;\n" "")
        self.summitPanelLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.summitPanelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.summitPanelLabel.setObjectName("summitPanelLabel")

        self.summitFactsLabel = QtWidgets.QLabel(self.centralwidget)
        self.summitFactsLabel.setGeometry(QtCore.QRect(140, 235, 85, 25))
        self.summitFactsLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n" "\n" "")
        self.summitFactsLabel.setObjectName("summitFactsLabel")
        
        self.summitFacts = QtWidgets.QTextEdit(self.centralwidget)
        self.summitFacts.setGeometry(QtCore.QRect(141, 269, 521, 130))
        self.summitFacts.setStyleSheet("background: #FFFFFF;\n" "border: 2px solid #773E7C;\n" "font-family: Circular Std;\n" "font-size: 18px;\n" "\n" "")
        self.summitFacts.setObjectName("summitFacts")

        self.summitIssuesLabel = QtWidgets.QLabel(self.centralwidget)
        self.summitIssuesLabel.setGeometry(QtCore.QRect(140, 424, 85, 25))
        self.summitIssuesLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n" "\n" "")
        self.summitIssuesLabel.setObjectName("summitIssuesLabel")

        self.summitIssues = QtWidgets.QTextEdit(self.centralwidget)
        self.summitIssues.setGeometry(QtCore.QRect(141, 462, 521, 130))
        self.summitIssues.setStyleSheet("background: #FFFFFF;\n" "border: 2px solid #773E7C;\n" "font-family: Circular Std;\n" "font-size: 18px;\n" "\n" "")
        self.summitIssues.setObjectName("summitIssues")

        self.summitRulingLabel = QtWidgets.QLabel(self.centralwidget)
        self.summitRulingLabel.setGeometry(QtCore.QRect(140, 617, 91, 25))
        self.summitRulingLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n" "\n" "")
        self.summitRulingLabel.setObjectName("summitRulingLabel")

        self.summitRuling = QtWidgets.QTextEdit(self.centralwidget)
        self.summitRuling.setGeometry(QtCore.QRect(141, 655, 521, 130))
        self.summitRuling.setStyleSheet("background: #FFFFFF;\n" "border: 2px solid #773E7C;\n" "font-family: Circular Std;\n" "font-size: 18px;\n" "\n" "")
        self.summitRuling.setObjectName("summitRuling")

       
        # ROUGE UI WINDOW - Reference Panel
        self.referencePanelBorder = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelBorder.setGeometry(QtCore.QRect(1220, 112, 600, 730))
        self.referencePanelBorder.setStyleSheet("border: 8px solid #773E7C;\n" "border-radius: 30px;\n" "")
        self.referencePanelBorder.setText("")
        self.referencePanelBorder.setObjectName("referencePanelBorder")

        self.referencePanelLabel = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelLabel.setGeometry(QtCore.QRect(1220, 161, 600, 41))
        self.referencePanelLabel.setStyleSheet("background: #773E7C;\n" "font-family: Circular Std;\n" "font-style: normal;\n" 
                                               "font-weight: 900;\n" "font-size: 40px;\n" "color: #FFFFFF;\n" "\n" "")
        self.referencePanelLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.referencePanelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.referencePanelLabel.setObjectName("referencePanelLabel")

        self.referencePanelLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelLabel_2.setGeometry(QtCore.QRect(1229, 131, 581, 51))
        self.referencePanelLabel_2.setStyleSheet("background: #773E7C;\n" "font-family: Circular Std;\n" "font-style: normal;\n" 
                                                 "font-weight: 900;\n" "font-size: 40px;\n" "color: #FFFFFF;\n" "\n" "")
        self.referencePanelLabel_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.referencePanelLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.referencePanelLabel_2.setObjectName("referencePanelLabel_2")

        self.referencePanelHeaderRounded = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelHeaderRounded.setGeometry(QtCore.QRect(1220, 112, 600, 90))
        self.referencePanelHeaderRounded.setStyleSheet("background: #773E7C;\n" "border-radius: 32px;\n" "")
        self.referencePanelHeaderRounded.setText("")
        self.referencePanelHeaderRounded.setObjectName("referencePanelHeaderRounded")

        self.referencePanelHeaderSolid = QtWidgets.QLabel(self.centralwidget)
        self.referencePanelHeaderSolid.setGeometry(QtCore.QRect(1220, 157, 600, 45))
        self.referencePanelHeaderSolid.setStyleSheet("\n" "\n" "background: #773E7C;\n" "")
        self.referencePanelHeaderSolid.setText("")
        self.referencePanelHeaderSolid.setObjectName("referencePanelHeaderSolid")

        self.referenceFactsLabel = QtWidgets.QLabel(self.centralwidget)
        self.referenceFactsLabel.setGeometry(QtCore.QRect(1260, 235, 85, 25))
        self.referenceFactsLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n" "\n" "")
        self.referenceFactsLabel.setObjectName("referenceFactsLabel")

        self.referenceFacts = QtWidgets.QTextEdit(self.centralwidget)
        self.referenceFacts.setGeometry(QtCore.QRect(1261, 269, 521, 130))
        self.referenceFacts.setStyleSheet("background: #FFFFFF;\n" "border: 2px solid #773E7C;\n" "font-family: Circular Std;\n" "font-size: 18px;\n" "\n" "")
        self.referenceFacts.setObjectName("referenceFacts")

        self.referenceIssuesLabel = QtWidgets.QLabel(self.centralwidget)
        self.referenceIssuesLabel.setGeometry(QtCore.QRect(1260, 424, 85, 25))
        self.referenceIssuesLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n""font-weight: bold;\n" "font-size: 24px;\n" "\n" "")
        self.referenceIssuesLabel.setObjectName("referenceIssuesLabel")

        self.referenceIssues = QtWidgets.QTextEdit(self.centralwidget)
        self.referenceIssues.setGeometry(QtCore.QRect(1261, 462, 521, 130))
        self.referenceIssues.setStyleSheet("background: #FFFFFF;\n" "border: 2px solid #773E7C;\n" "font-family: Circular Std;\n" "font-size: 18px;\n" "\n" "")
        self.referenceIssues.setObjectName("referenceIssues")

        self.referenceRulingLabel = QtWidgets.QLabel(self.centralwidget)
        self.referenceRulingLabel.setGeometry(QtCore.QRect(1260, 617, 91, 25))
        self.referenceRulingLabel.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 24px;\n" "\n" "")
        self.referenceRulingLabel.setObjectName("referenceRulingLabel")

        self.referenceRuling = QtWidgets.QTextEdit(self.centralwidget)
        self.referenceRuling.setGeometry(QtCore.QRect(1261, 655, 521, 130))
        self.referenceRuling.setStyleSheet("background: #FFFFFF;\n" "border: 2px solid #773E7C;\n" "font-family: Circular Std;\n" "font-size: 18px;\n" "\n" "")
        self.referenceRuling.setObjectName("referenceRuling")


        # ROUGE UI WINDOW - Rouge Panel
        self.rougePanelBorder = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelBorder.setGeometry(QtCore.QRect(760, 112, 400, 730))
        self.rougePanelBorder.setStyleSheet("border: 8px solid #773E7C;\n" "border-radius: 30px;\n""")
        self.rougePanelBorder.setText("")
        self.rougePanelBorder.setObjectName("rougePanelBorder")

        self.rougePanelHeaderRounded = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelHeaderRounded.setGeometry(QtCore.QRect(760, 112, 391, 85))
        self.rougePanelHeaderRounded.setStyleSheet("background: #773E7C;\n" "border-radius: 20px;\n""")
        self.rougePanelHeaderRounded.setText("")
        self.rougePanelHeaderRounded.setObjectName("rougePanelHeaderRounded")

        self.rougePanelHeaderSolid = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelHeaderSolid.setGeometry(QtCore.QRect(763, 131, 392, 71))
        self.rougePanelHeaderSolid.setStyleSheet("\n" "\n" "background: #773E7C;\n""")
        self.rougePanelHeaderSolid.setText("")
        self.rougePanelHeaderSolid.setObjectName("rougePanelHeaderSolid")

        self.rougePanelLabel = QtWidgets.QLabel(self.centralwidget)
        self.rougePanelLabel.setGeometry(QtCore.QRect(770, 121, 381, 71))
        self.rougePanelLabel.setStyleSheet("background: #773E7C;\n" "font-family: Circular Std;\n" "font-style: normal;\n"
                                           "font-weight: 900;\n" "font-size: 30px;\n" "color: #FFFFFF;\n" "\n" "")
        self.rougePanelLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.rougePanelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rougePanelLabel.setObjectName("rougePanelLabel")


        # ROUGE UI WINDOW - ROUGE Overall
        self.rougeOverallLabel = QtWidgets.QLabel(self.centralwidget)
        self.rougeOverallLabel.setGeometry(QtCore.QRect(768, 202, 384, 44))
        self.rougeOverallLabel.setStyleSheet("background: #E5CE83;\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n" "font-size: 24px;\n"
                                             "color: #000000;\n" "\n" "/* SUMMIT */\n" "\n" "position: absolute;\n" "width: 499.97px;\n" "height: 138.93px;\n" "\n" "\n" "")
        self.rougeOverallLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rougeOverallLabel.setObjectName("rougeOverallLabel")

        self.rougeFactsLabel = QtWidgets.QLabel(self.centralwidget)
        self.rougeFactsLabel.setGeometry(QtCore.QRect(768, 360, 384, 44))
        self.rougeFactsLabel.setStyleSheet("background: #E5CE83;\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" 
                                           "font-size: 24px;\n" "color: #FFFFFF;\n" "\n" "")
        self.rougeFactsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rougeFactsLabel.setObjectName("rougeFactsLabel")

        self.rougeIssuesLabel = QtWidgets.QLabel(self.centralwidget)
        self.rougeIssuesLabel.setGeometry(QtCore.QRect(768, 518, 384, 44))
        self.rougeIssuesLabel.setStyleSheet("background: #E5CE83;\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n"
                                            "font-size: 24px;\n" "color: #FFFFFF;\n" "\n" "")
        self.rougeIssuesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rougeIssuesLabel.setObjectName("rougeIssuesLabel")

        self.rougeRulingLabel = QtWidgets.QLabel(self.centralwidget)
        self.rougeRulingLabel.setGeometry(QtCore.QRect(768, 676, 384, 44))
        self.rougeRulingLabel.setStyleSheet("background: #E5CE83;\n" "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n"
                                            "font-size: 24px;\n" "color: #FFFFFF;\n" "\n" "")
        self.rougeRulingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rougeRulingLabel.setObjectName("rougeRulingLabel")


        # ROUGE UI WINDOW - ROUGE Overall Metrics
        self.rougeOverallMetrics = QtWidgets.QLabel(self.centralwidget)
        self.rougeOverallMetrics.setGeometry(QtCore.QRect(793, 246, 148, 114))
        self.rougeOverallMetrics.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 24px;\n"
                                               "color: #000000;\n" "\n""")
        self.rougeOverallMetrics.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rougeOverallMetrics.setObjectName("rougeOverallMetrics")

        self.overallPrecision = QtWidgets.QTextEdit(self.centralwidget)
        self.overallPrecision.setEnabled(False)
        self.overallPrecision.setGeometry(QtCore.QRect(1052, 246, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.overallPrecision.setFont(font)
        self.overallPrecision.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                            "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.overallPrecision.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.overallPrecision.setObjectName("overallPrecision")

        self.overallRecall = QtWidgets.QTextEdit(self.centralwidget)
        self.overallRecall.setEnabled(False)
        self.overallRecall.setGeometry(QtCore.QRect(1052, 282, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.overallRecall.setFont(font)
        self.overallRecall.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                         "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.overallRecall.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.overallRecall.setObjectName("overallRecall")

        self.overallFMeasure = QtWidgets.QTextEdit(self.centralwidget)
        self.overallFMeasure.setEnabled(False)
        self.overallFMeasure.setGeometry(QtCore.QRect(1052, 316, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.overallFMeasure.setFont(font)
        self.overallFMeasure.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                           "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.overallFMeasure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.overallFMeasure.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.overallFMeasure.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.overallFMeasure.setObjectName("overallFMeasure")


        # ROUGE UI WINDOW - ROUGE Facts Metrics
        self.rougeFactsMetrics = QtWidgets.QLabel(self.centralwidget)
        self.rougeFactsMetrics.setGeometry(QtCore.QRect(793, 404, 148, 114))
        self.rougeFactsMetrics.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 24px;\n"
                                             "color: #000000;\n" "\n""")
        self.rougeFactsMetrics.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rougeFactsMetrics.setObjectName("rougeFactsMetrics")

        self.factsPrecision = QtWidgets.QTextEdit(self.centralwidget)
        self.factsPrecision.setEnabled(False)
        self.factsPrecision.setGeometry(QtCore.QRect(1052, 404, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.factsPrecision.setFont(font)
        self.factsPrecision.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                          "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.factsPrecision.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.factsPrecision.setObjectName("factsPrecision")

        self.factsRecall = QtWidgets.QTextEdit(self.centralwidget)
        self.factsRecall.setEnabled(False)
        self.factsRecall.setGeometry(QtCore.QRect(1052, 440, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.factsRecall.setFont(font)
        self.factsRecall.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                       "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.factsRecall.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.factsRecall.setObjectName("factsRecall")

        self.factsFMeasure = QtWidgets.QTextEdit(self.centralwidget)
        self.factsFMeasure.setEnabled(False)
        self.factsFMeasure.setGeometry(QtCore.QRect(1052, 474, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.factsFMeasure.setFont(font)
        self.factsFMeasure.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n" 
                                         "color: #ffffff;\n" "background: #D0B5D5;\n" "\n"  "\n" "")
        self.factsFMeasure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.factsFMeasure.setObjectName("factsFMeasure")


        # ROUGE UI WINDOW - ROUGE Issues Metrics
        self.rougeIssuesMetrics = QtWidgets.QLabel(self.centralwidget)
        self.rougeIssuesMetrics.setGeometry(QtCore.QRect(793, 562, 148, 114))
        self.rougeIssuesMetrics.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 24px;\n"
                                              "color: #000000;\n" "\n" "")
        self.rougeIssuesMetrics.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rougeIssuesMetrics.setObjectName("rougeIssuesMetrics")

        self.issuesRecall = QtWidgets.QTextEdit(self.centralwidget)
        self.issuesRecall.setEnabled(False)
        self.issuesRecall.setGeometry(QtCore.QRect(1052, 598, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.issuesRecall.setFont(font)
        self.issuesRecall.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                        "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.issuesRecall.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.issuesRecall.setObjectName("issuesRecall")

        self.issuesPrecision = QtWidgets.QTextEdit(self.centralwidget)
        self.issuesPrecision.setEnabled(False)
        self.issuesPrecision.setGeometry(QtCore.QRect(1052, 562, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.issuesPrecision.setFont(font)
        self.issuesPrecision.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                           "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.issuesPrecision.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.issuesPrecision.setObjectName("issuesPrecision")

        self.issuesFMeasure = QtWidgets.QTextEdit(self.centralwidget)
        self.issuesFMeasure.setEnabled(False)
        self.issuesFMeasure.setGeometry(QtCore.QRect(1052, 632, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.issuesFMeasure.setFont(font)
        self.issuesFMeasure.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                          "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.issuesFMeasure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.issuesFMeasure.setObjectName("issuesFMeasure")


        # ROUGE UI WINDOW - ROUGE Ruling Metrics
        self.rougeRulingMetrics = QtWidgets.QLabel(self.centralwidget)
        self.rougeRulingMetrics.setGeometry(QtCore.QRect(793, 720, 148, 114))
        self.rougeRulingMetrics.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 450;\n" "font-size: 24px;\n"
                                              "color: #000000;\n" "\n" "")
        self.rougeRulingMetrics.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rougeRulingMetrics.setObjectName("rougeRulingMetrics")

        self.rulingRecall = QtWidgets.QTextEdit(self.centralwidget)
        self.rulingRecall.setEnabled(False)
        self.rulingRecall.setGeometry(QtCore.QRect(1052, 756, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rulingRecall.setFont(font)
        self.rulingRecall.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                        "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.rulingRecall.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rulingRecall.setObjectName("rulingRecall")

        self.rulingPrecision = QtWidgets.QTextEdit(self.centralwidget)
        self.rulingPrecision.setEnabled(False)
        self.rulingPrecision.setGeometry(QtCore.QRect(1052, 720, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rulingPrecision.setFont(font)
        self.rulingPrecision.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n" 
                                           "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "")
        self.rulingPrecision.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rulingPrecision.setObjectName("rulingPrecision")

        self.rulingFMeasure = QtWidgets.QTextEdit(self.centralwidget)
        self.rulingFMeasure.setEnabled(False)
        self.rulingFMeasure.setGeometry(QtCore.QRect(1062, 790, 81, 38))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rulingFMeasure.setFont(font)
        self.rulingFMeasure.setStyleSheet("font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: bold;\n" "font-size: 15px;\n"
                                          "color: #ffffff;\n" "background: #D0B5D5;\n" "\n" "\n" "\n" "")
        self.rulingFMeasure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rulingFMeasure.setObjectName("rulingFMeasure")
        

        # ROUGE UI WINDOW - ROUGE Overall Metrics Background
        self.rougeMetricsBg = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg.setGeometry(QtCore.QRect(1052, 246, 100, 114))
        self.rougeMetricsBg.setStyleSheet("background: #D0B5D5;\n" "\n""")
        self.rougeMetricsBg.setText("")
        self.rougeMetricsBg.setObjectName("rougeMetricsBg")

        self.rougeMetricsBg_2 = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg_2.setGeometry(QtCore.QRect(1052, 404, 100, 114))
        self.rougeMetricsBg_2.setStyleSheet("\n" "\n" "background: #D0B5D5;\n" "\n" "")
        self.rougeMetricsBg_2.setText("")
        self.rougeMetricsBg_2.setObjectName("rougeMetricsBg_2")

        self.rougeMetricsBg_3 = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg_3.setGeometry(QtCore.QRect(1052, 562, 100, 114))
        self.rougeMetricsBg_3.setStyleSheet("\n" "\n" "background: #D0B5D5;\n" "\n" "")
        self.rougeMetricsBg_3.setText("")
        self.rougeMetricsBg_3.setObjectName("rougeMetricsBg_3")

        self.rougeMetricsBg_4 = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg_4.setGeometry(QtCore.QRect(1052, 720, 100, 86))
        self.rougeMetricsBg_4.setStyleSheet("\n" "\n" "background: #D0B5D5;\n" "\n" "")
        self.rougeMetricsBg_4.setText("")
        self.rougeMetricsBg_4.setObjectName("rougeMetricsBg_4")

        self.rougeMetricsBg_5 = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg_5.setGeometry(QtCore.QRect(1052, 720, 71, 115))
        self.rougeMetricsBg_5.setStyleSheet("\n" "\n" "background: #D0B5D5;\n" "\n" "")
        self.rougeMetricsBg_5.setText("")
        self.rougeMetricsBg_5.setObjectName("rougeMetricsBg_5")

        self.rougeMetricsBg_6 = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg_6.setGeometry(QtCore.QRect(1052, 720, 100, 114))
        self.rougeMetricsBg_6.setStyleSheet("background: #D0B5D5;\n" "border-radius: 20px;\n" "")
        self.rougeMetricsBg_6.setText("")
        self.rougeMetricsBg_6.setObjectName("rougeMetricsBg_6")

        self.rougeMetricsBg_7 = QtWidgets.QLabel(self.centralwidget)
        self.rougeMetricsBg_7.setGeometry(QtCore.QRect(1052, 720, 61, 114))
        self.rougeMetricsBg_7.setStyleSheet("background: #D0B5D5;\n" "\n" "")
        self.rougeMetricsBg_7.setText("")
        self.rougeMetricsBg_7.setObjectName("rougeMetricsBg_7")


        # ROUGE UI WINDOW - BUTTONS
        # ROUGE UI WINDOW - Compute Button
        self.computeButton = QtWidgets.QPushButton(self.centralwidget)
        self.computeButton.setGeometry(QtCore.QRect(730, 882, 200, 60))
        self.computeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.computeButton.setStyleSheet("QPushButton{\n" "background-color: rgb(208, 181, 213);\n" "background-color: rgb(119, 62, 124);\n" "border-radius: 30px;\n"
                                         "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n" "font-size: 24px;\n" "line-height: 30px;\n" "color: #FFFFFF;\n" "}\n"
                                         "\n" "QPushButton:hover{background: #D0B5D5;\n" ";}\n" "\n" "\n" "")
        self.computeButton.setObjectName("computeButton")
        compute = self.computeButton.clicked.connect(self._compute_rouge)

        # ROUGE UI WINDOW - Clear Button
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(990, 882, 200, 60))
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setStyleSheet("QPushButton{\n" "background-color: rgb(208, 181, 213);\n" "background-color: rgb(119, 62, 124);\n" "border-radius: 30px;\n"
                                       "font-family: Circular Std;\n" "font-style: normal;\n" "font-weight: 900;\n" "font-size: 24px;\n" "line-height: 30px;\n" "color: #FFFFFF;\n" "}\n"
                                       "\n" "QPushButton:hover{background: #D0B5D5;\n" ";}\n" "\n" "\n" "")
        self.clearButton.setObjectName("clearButton")
        clear = self.clearButton.clicked.connect(self._clear)



        self.summitPanelBorder.raise_()
        self.summitPanelHeaderSolid.raise_()
        self.summitPanelHeaderRounded.raise_()
        self.summitPanelLabel.raise_()
        self.summitFactsLabel.raise_()
        self.summitIssuesLabel.raise_()
        self.summitRulingLabel.raise_()
        self.summitFacts.raise_()
        self.summitIssues.raise_()
        self.summitRuling.raise_()
        
        self.referencePanelHeaderSolid.raise_()
        self.referencePanelBorder.raise_()
        self.referencePanelHeaderRounded.raise_()
        self.referencePanelLabel.raise_()
        self.referencePanelLabel_2.raise_()
        self.referenceFactsLabel.raise_()
        self.referenceIssuesLabel.raise_()
        self.referenceRulingLabel.raise_()
        self.referenceFacts.raise_()
        self.referenceIssues.raise_()
        self.referenceRuling.raise_()
        
        self.rougePanelBorder.raise_()
        self.rougePanelHeaderRounded.raise_()
        self.rougePanelHeaderSolid.raise_()
        self.rougePanelLabel.raise_()
        self.rougeOverallLabel.raise_()
        self.rougeFactsLabel.raise_()
        self.rougeIssuesLabel.raise_()
        self.rougeRulingLabel.raise_()
        self.rougeOverallMetrics.raise_()
        self.rougeFactsMetrics.raise_()
        self.rougeIssuesMetrics.raise_()
        self.rougeRulingMetrics.raise_()
        self.rougeMetricsBg.raise_()
        self.rougeMetricsBg_2.raise_()
        self.rougeMetricsBg_3.raise_()
        self.rougeMetricsBg_4.raise_()
        self.rougeMetricsBg_5.raise_()
        self.rougeMetricsBg_6.raise_()
        self.rougeMetricsBg_7.raise_()
        
        self.overallRecall.raise_()
        self.overallPrecision.raise_()
        self.overallFMeasure.raise_()
        self.factsRecall.raise_()
        self.factsPrecision.raise_()
        self.factsFMeasure.raise_()
        self.issuesRecall.raise_()
        self.issuesPrecision.raise_()
        self.issuesFMeasure.raise_()
        self.rulingRecall.raise_()
        self.rulingPrecision.raise_()
        self.rulingFMeasure.raise_()
        self.computeButton.raise_()
        self.clearButton.raise_()
       
        ROUGE_UI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ROUGE_UI)
        self.statusbar.setObjectName("statusbar")
        ROUGE_UI.setStatusBar(self.statusbar)

        self.retranslateUi(ROUGE_UI)
        QtCore.QMetaObject.connectSlotsByName(ROUGE_UI)

    def retranslateUi(self, ROUGE_UI):
        _translate = QtCore.QCoreApplication.translate
        ROUGE_UI.setWindowTitle(_translate("ROUGE_UI", "ROUGE Metrics"))
        self.summitPanelLabel.setText(_translate("ROUGE_UI", "SUMMIT"))
        self.rougePanelLabel.setText(_translate("ROUGE_UI", "ROUGE METRICS"))
        self.computeButton.setText(_translate("ROUGE_UI", "COMPUTE"))
        self.rougeOverallLabel.setText(_translate("ROUGE_UI", "OVERALL"))
        self.rougeFactsLabel.setText(_translate("ROUGE_UI", "FACTS"))
        self.rougeIssuesLabel.setText(_translate("ROUGE_UI", "ISSUES"))
        self.rougeRulingLabel.setText(_translate("ROUGE_UI", "RULING"))
        self.rougeOverallMetrics.setText(_translate("ROUGE_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">PRECISION</span></p><p><span style=\" font-size:14pt;\">RECALL</span></p><p><span style=\" font-size:14pt;\">F-MEASURE</span></p></body></html>"))
        self.rougeFactsMetrics.setText(_translate("ROUGE_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">PRECISION</span></p><p><span style=\" font-size:14pt;\">RECALL</span></p><p><span style=\" font-size:14pt;\">F-MEASURE</span></p></body></html>"))
        self.rougeIssuesMetrics.setText(_translate("ROUGE_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">PRECISION</span></p><p><span style=\" font-size:14pt;\">RECALL</span></p><p><span style=\" font-size:14pt;\">F-MEASURE</span></p></body></html>"))
        self.rougeRulingMetrics.setText(_translate("ROUGE_UI", "<html><head/><body><p><span style=\" font-size:14pt;\">PRECISION</span></p><p><span style=\" font-size:14pt;\">RECALL</span></p><p><span style=\" font-size:14pt;\">F-MEASURE</span></p></body></html>"))
        self.overallPrecision.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n" 
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.overallPrecision.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.overallRecall.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.overallRecall.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.overallFMeasure.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.overallFMeasure.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.factsPrecision.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.factsPrecision.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.factsRecall.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.factsRecall.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.factsFMeasure.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.factsFMeasure.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.issuesPrecision.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.issuesPrecision.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.issuesRecall.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.issuesRecall.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.issuesFMeasure.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.issuesFMeasure.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.rulingPrecision.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.rulingPrecision.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.rulingRecall.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.rulingRecall.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.rulingFMeasure.setHtml(_translate("ROUGE_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Circular Std\'; font-size:15px; font-weight:600; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:448;\">-</span></p></body></html>"))
        self.rulingFMeasure.setPlaceholderText(_translate("ROUGE_UI", "-"))
        self.summitFactsLabel.setText(_translate("ROUGE_UI", "FACTS"))
        self.summitIssuesLabel.setText(_translate("ROUGE_UI", "ISSUES"))
        self.referenceFactsLabel.setText(_translate("ROUGE_UI", "FACTS"))
        self.summitRulingLabel.setText(_translate("ROUGE_UI", "RULING"))
        self.referenceIssuesLabel.setText(_translate("ROUGE_UI", "ISSUES"))
        self.referenceRulingLabel.setText(_translate("ROUGE_UI", "RULING"))
        self.clearButton.setText(_translate("ROUGE_UI", "CLEAR"))
        self.referencePanelLabel_2.setText(_translate("ROUGE_UI", "REFERENCE SUMMARY"))


    #---------- BUTTONS FUNCTIONS ----------#

    # COMPUTE BUTTON
    def _compute_rouge(self):
        r = Rouge()

        # GET TEXT FROM TEXTFIELDS
        summit_facts = self.summitFacts.toPlainText()
        reference_facts = self.referenceFacts.toPlainText()
        summit_issues = self.summitIssues.toPlainText()
        reference_issues = self.referenceIssues.toPlainText()
        summit_ruling = self.summitRuling.toPlainText()
        reference_ruling = self.referenceRuling.toPlainText()

        # REMOVE NEW LINES FROM DOCUMENTS
        summit_facts = summit_facts.replace("\n","")
        reference_facts = reference_facts.replace("\n","")
        summit_issues = summit_issues.replace("\n","")
        reference_issues = reference_issues.replace("\n","")
        summit_ruling = summit_ruling.replace("\n","")
        reference_ruling = reference_ruling.replace("\n","")
       
        # REMOVE EXTRA DOUBLE QUOTATIONS FROM DOCUMENTS
        summit_facts = summit_facts.replace('"',"")
        reference_facts = reference_facts.replace('"',"")
        summit_issues = summit_issues.replace('"',"")
        reference_issues = reference_issues.replace('"',"")
        summit_ruling = summit_ruling.replace('"',"")
        reference_ruling = reference_ruling.replace('"',"")

        # COMPUTE FOR ROUGE
        [facts_precision, facts_recall, facts_f_score] = r.rouge_l([summit_facts], [reference_facts])
        [issues_precision, issues_recall, issues_f_score] = r.rouge_l([summit_issues], [reference_issues])
        [ruling_precision, ruling_recall, ruling_f_score] = r.rouge_l([summit_ruling], [reference_ruling])
        
        overall_precision = (facts_precision + issues_precision + ruling_precision)/3
        overall_recall = (facts_recall + issues_recall + ruling_recall)/3
        overall_f_score = (facts_f_score + issues_f_score + ruling_f_score)/3

        self.overallPrecision.setText("  " + str(round(overall_precision,5)))
        self.overallRecall.setText("  " + str(round(overall_recall,5)))
        self.overallFMeasure.setText("  " + str(round(overall_f_score,5)))
        self.factsPrecision.setText("  " + str(round(facts_precision,5)))                
        self.factsRecall.setText("  " + str(round(facts_recall,5)))  
        self.factsFMeasure.setText("  " + str(round(facts_f_score,5)))  
        self.issuesPrecision.setText("  " + str(round(issues_precision,5)))                    
        self.issuesRecall.setText("  " + str(round(issues_recall,5)))   
        self.issuesFMeasure.setText("  " + str(round(issues_f_score,5)))
        self.rulingPrecision.setText("  " + str(round(ruling_precision,5)))                
        self.rulingRecall.setText("  " + str(round(ruling_recall,5)))
        self.rulingFMeasure.setText(str(round(ruling_f_score,5))) 

    # CLEAR BUTTON
    def _clear(self):
        self.summitFacts.setText("")
        self.summitIssues.setText("")
        self.summitRuling.setText("")
        self.referenceFacts.setText("")
        self.referenceIssues.setText("")
        self.referenceRuling.setText("")
        self.overallPrecision.setText("  -")
        self.overallRecall.setText("  -")
        self.overallFMeasure.setText("  -")
        self.factsPrecision.setText("  -")                
        self.factsRecall.setText("  -")  
        self.factsFMeasure.setText("  -")  
        self.issuesPrecision.setText("  -")                    
        self.issuesRecall.setText("  -")   
        self.issuesFMeasure.setText("  -")
        self.rulingPrecision.setText("  -")                
        self.rulingRecall.setText("  -")
        self.rulingFMeasure.setText("-")  



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ROUGE_UI = QtWidgets.QMainWindow()
    ui = Ui_ROUGE_UI()
    ui.setupUi(ROUGE_UI)
    ROUGE_UI.show()
    sys.exit(app.exec_())