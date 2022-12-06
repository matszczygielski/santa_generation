# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXvwure.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1069, 882)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"    background-color: rgb(106, 22, 22);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topbarContainer = QWidget(self.centralwidget)
        self.topbarContainer.setObjectName(u"topbarContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.topbarContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.statusSubContainer = QWidget(self.topbarContainer)
        self.statusSubContainer.setObjectName(u"statusSubContainer")
        self.verticalLayout_5 = QVBoxLayout(self.statusSubContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.statusSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"* {\n"
"    border: none;\n"
"    background-color: rgb(156, 22, 22);\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 14pt \"Chilanka\";\n"
"    color: rgb(222, 221, 218); \n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.statusMsgLbl = QLabel(self.frame_2)
        self.statusMsgLbl.setObjectName(u"statusMsgLbl")
        self.statusMsgLbl.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.statusMsgLbl)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_5.addWidget(self.statusSubContainer)

        self.settingsSubContainer = QWidget(self.topbarContainer)
        self.settingsSubContainer.setObjectName(u"settingsSubContainer")
        self.settingsSubContainer.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.settingsSubContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.utils = QFrame(self.settingsSubContainer)
        self.utils.setObjectName(u"utils")
        self.utils.setStyleSheet(u"*{\n"
"    border: none;\n"
"    background-color: rgb(156, 22, 22);\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    border-bottom: 2px solid rgb(106, 22, 22);\n"
"}")
        self.utils.setFrameShape(QFrame.StyledPanel)
        self.utils.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.utils)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, -1, 15, -1)
        self.undoBtn = QPushButton(self.utils)
        self.undoBtn.setObjectName(u"undoBtn")
        icon = QIcon()
        icon.addFile(u"resources/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.undoBtn.setIcon(icon)
        self.undoBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.undoBtn, 0, Qt.AlignLeft)

        self.keyBtn = QPushButton(self.utils)
        self.keyBtn.setObjectName(u"keyBtn")
        self.keyBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"resources/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.keyBtn.setIcon(icon1)
        self.keyBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.keyBtn, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.utils, 0, Qt.AlignRight)

        self.languages = QFrame(self.settingsSubContainer)
        self.languages.setObjectName(u"languages")
        self.languages.setStyleSheet(u"* {\n"
"    border: none;\n"
"    background-color: rgb(156, 22, 22);\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    border-bottom: 2px solid rgb(106, 22, 22);\n"
"}")
        self.languages.setFrameShape(QFrame.StyledPanel)
        self.languages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.languages)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plBtn = QPushButton(self.languages)
        self.plBtn.setObjectName(u"plBtn")
        self.plBtn.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(36)
        self.plBtn.setFont(font)
        self.plBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"resources/PL.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.plBtn.setIcon(icon2)
        self.plBtn.setIconSize(QSize(24, 24))
        self.plBtn.setCheckable(False)
        self.plBtn.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.plBtn)

        self.engBtn = QPushButton(self.languages)
        self.engBtn.setObjectName(u"engBtn")
        self.engBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"resources/UK.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.engBtn.setIcon(icon3)
        self.engBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.engBtn)


        self.horizontalLayout_3.addWidget(self.languages, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.settingsSubContainer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.topbarContainer, 0, Qt.AlignTop)

        self.titleContainer = QWidget(self.centralwidget)
        self.titleContainer.setObjectName(u"titleContainer")
        self.titleContainer.setMaximumSize(QSize(782, 466))
        font1 = QFont()
        font1.setFamily(u"Chilanka")
        font1.setPointSize(50)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.titleContainer.setFont(font1)
        self.titleContainer.setStyleSheet(u"*{\n"
"    font: 75 50pt \"Chilanka\";\n"
"    color: rgb(222, 221, 218);\n"
"    border: none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.titleContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(self.titleContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(533, 123))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.titleLbl = QLabel(self.frame)
        self.titleLbl.setObjectName(u"titleLbl")
        self.titleLbl.setFont(font1)
        self.titleLbl.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.titleLbl, 0, Qt.AlignLeft)

        self.titleIconLbl = QLabel(self.frame)
        self.titleIconLbl.setObjectName(u"titleIconLbl")
        self.titleIconLbl.setMaximumSize(QSize(100, 100))
        self.titleIconLbl.setFont(font1)
        self.titleIconLbl.setTextFormat(Qt.AutoText)
        self.titleIconLbl.setPixmap(QPixmap(u"resources/santa.svg"))
        self.titleIconLbl.setScaledContents(True)
        self.titleIconLbl.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.titleIconLbl)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.titleContainer, 0, Qt.AlignHCenter)

        self.inputContainer = QWidget(self.centralwidget)
        self.inputContainer.setObjectName(u"inputContainer")
        self.inputContainer.setStyleSheet(u"QLabel {\n"
"    font: 20pt \"Chilanka\";\n"
"    color: rgb(222, 221, 218); \n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(244, 76, 76);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(222, 221, 218); \n"
"    font: 18pt \"Chilanka\";\n"
"    min-width: 150px;\n"
"    padding: 6px;\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 221, 218); \n"
"    border-color: rgb(244, 76, 76);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(192, 191, 188);\n"
" }\n"
"\n"
"QComboBox {\n"
"    font: 18pt \"Chilanka\";\n"
"    selection-background-color: rgb(244, 76, 76);\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    font: 18pt \"Chilanka\";\n"
"    max-height: 40px;\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.inputContainer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget = QWidget(self.inputContainer)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"    border: none;\n"
"    background-color: rgb(156, 22, 22);\n"
"    border-radius: 20;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.widget_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.AddSantaLbl = QLabel(self.frame_4)
        self.AddSantaLbl.setObjectName(u"AddSantaLbl")

        self.verticalLayout_9.addWidget(self.AddSantaLbl)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_5 = QFrame(self.widget_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.AddSantaInput = QTextEdit(self.frame_5)
        self.AddSantaInput.setObjectName(u"AddSantaInput")
        self.AddSantaInput.setMaximumSize(QSize(16777215, 48))
        self.AddSantaInput.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.AddSantaInput)

        self.AddSantaBtn = QPushButton(self.frame_5)
        self.AddSantaBtn.setObjectName(u"AddSantaBtn")
        self.AddSantaBtn.setStyleSheet(u"QPushButton {\n"
"    max-width: 200px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.AddSantaBtn, 0, Qt.AlignRight)


        self.horizontalLayout_9.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.widget_6, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"#widget_4{\n"
"    border: none;\n"
"    background-color: rgb(156, 22, 22);\n"
"    border-radius: 20;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.constrainsLbl = QLabel(self.frame_6)
        self.constrainsLbl.setObjectName(u"constrainsLbl")

        self.verticalLayout_11.addWidget(self.constrainsLbl)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QComboBox{\n"
"    border-style: outset;\n"
"    border-width: 4px;\n"
"    border-radius: 10px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.noDrawLeftBox = QComboBox(self.frame_7)
        self.noDrawLeftBox.addItem("")
        self.noDrawLeftBox.addItem("")
        self.noDrawLeftBox.setObjectName(u"noDrawLeftBox")

        self.horizontalLayout_11.addWidget(self.noDrawLeftBox)

        self.NoDrawLbl = QLabel(self.frame_7)
        self.NoDrawLbl.setObjectName(u"NoDrawLbl")
        self.NoDrawLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.NoDrawLbl)

        self.noDrawRightBox = QComboBox(self.frame_7)
        self.noDrawRightBox.addItem("")
        self.noDrawRightBox.addItem("")
        self.noDrawRightBox.setObjectName(u"noDrawRightBox")

        self.horizontalLayout_11.addWidget(self.noDrawRightBox)

        self.NoDrawBtn = QPushButton(self.frame_7)
        self.NoDrawBtn.setObjectName(u"NoDrawBtn")

        self.horizontalLayout_11.addWidget(self.NoDrawBtn, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_7)


        self.verticalLayout_4.addWidget(self.widget_4)


        self.horizontalLayout_7.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.inputContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3 {\n"
"    border: none;\n"
"    background-color: rgb(156, 22, 22);\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton {\n"
"     min-height: 100px;\n"
" }\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.generateLbl = QLabel(self.frame_3)
        self.generateLbl.setObjectName(u"generateLbl")

        self.verticalLayout_7.addWidget(self.generateLbl, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.generateBtn = QPushButton(self.frame_3)
        self.generateBtn.setObjectName(u"generateBtn")

        self.verticalLayout_7.addWidget(self.generateBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.frame_3)


        self.horizontalLayout_7.addWidget(self.widget_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.inputContainer, 0, Qt.AlignHCenter)

        self.tableContainer = QWidget(self.centralwidget)
        self.tableContainer.setObjectName(u"tableContainer")
        self.verticalLayout_8 = QVBoxLayout(self.tableContainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.summaryTable = QTableWidget(self.tableContainer)
        if (self.summaryTable.columnCount() < 3):
            self.summaryTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.summaryTable.setObjectName(u"summaryTable")
        self.summaryTable.setStyleSheet(u"font: 20pt \"Chilanka\";\n"
"background-color: rgb(255, 227, 226);")

        self.verticalLayout_8.addWidget(self.summaryTable)


        self.verticalLayout.addWidget(self.tableContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.statusMsgLbl.setText(QCoreApplication.translate("MainWindow", u"Hello World", None))
        self.undoBtn.setText("")
        self.keyBtn.setText("")
        self.plBtn.setText("")
        self.engBtn.setText("")
        self.titleLbl.setText(QCoreApplication.translate("MainWindow", u"Santa Generator", None))
        self.titleIconLbl.setText("")
        self.AddSantaLbl.setText(QCoreApplication.translate("MainWindow", u"1. Add Santa", None))
        self.AddSantaBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.constrainsLbl.setText(QCoreApplication.translate("MainWindow", u"2. Add constrains", None))
        self.noDrawLeftBox.setItemText(0, QCoreApplication.translate("MainWindow", u"test1", None))
        self.noDrawLeftBox.setItemText(1, QCoreApplication.translate("MainWindow", u"test2", None))

        self.NoDrawLbl.setText(QCoreApplication.translate("MainWindow", u"doesn't draw", None))
        self.noDrawRightBox.setItemText(0, QCoreApplication.translate("MainWindow", u"test3", None))
        self.noDrawRightBox.setItemText(1, QCoreApplication.translate("MainWindow", u"test4", None))

        self.NoDrawBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.generateLbl.setText(QCoreApplication.translate("MainWindow", u"3. Generate Santas", None))
        self.generateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        ___qtablewidgetitem = self.summaryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Santa", None));
        ___qtablewidgetitem1 = self.summaryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Doesn't draw", None));
        ___qtablewidgetitem2 = self.summaryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Secret URL", None));
    # retranslateUi

