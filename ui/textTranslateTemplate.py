# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\textTranslateTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1510, 688)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textToTranslateInput = QtWidgets.QPlainTextEdit(Form)
        self.textToTranslateInput.setDocumentTitle("")
        self.textToTranslateInput.setObjectName("textToTranslateInput")
        self.gridLayout.addWidget(self.textToTranslateInput, 0, 0, 1, 1)
        self.translatedTextInput = QtWidgets.QPlainTextEdit(Form)
        self.translatedTextInput.setDocumentTitle("")
        self.translatedTextInput.setObjectName("translatedTextInput")
        self.gridLayout.addWidget(self.translatedTextInput, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(Form)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.previousSentenceButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousSentenceButton.sizePolicy().hasHeightForWidth())
        self.previousSentenceButton.setSizePolicy(sizePolicy)
        self.previousSentenceButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.previousSentenceButton.setObjectName("previousSentenceButton")
        self.horizontalLayout.addWidget(self.previousSentenceButton)
        self.previousWordButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousWordButton.sizePolicy().hasHeightForWidth())
        self.previousWordButton.setSizePolicy(sizePolicy)
        self.previousWordButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.previousWordButton.setObjectName("previousWordButton")
        self.horizontalLayout.addWidget(self.previousWordButton)
        self.nextWordButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextWordButton.sizePolicy().hasHeightForWidth())
        self.nextWordButton.setSizePolicy(sizePolicy)
        self.nextWordButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.nextWordButton.setObjectName("nextWordButton")
        self.horizontalLayout.addWidget(self.nextWordButton)
        self.nextSentenceButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextSentenceButton.sizePolicy().hasHeightForWidth())
        self.nextSentenceButton.setSizePolicy(sizePolicy)
        self.nextSentenceButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.nextSentenceButton.setObjectName("nextSentenceButton")
        self.horizontalLayout.addWidget(self.nextSentenceButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.translateAllButton = QtWidgets.QPushButton(Form)
        self.translateAllButton.setObjectName("translateAllButton")
        self.horizontalLayout_2.addWidget(self.translateAllButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.retranslateUi(Form)
        self.resetButton.clicked.connect(self.textToTranslateInput.clear)
        self.resetButton.clicked.connect(self.translatedTextInput.clear)
        self.translateAllButton.clicked.connect(Form.translateAll)
        self.startButton.clicked.connect(Form.startTranslation)
        self.pauseButton.clicked.connect(Form.pauseTranslation)
        self.stopButton.clicked.connect(Form.stopTranslation)
        self.nextSentenceButton.clicked.connect(Form.translateNextSentence)
        self.nextWordButton.clicked.connect(Form.translateNextWord)
        self.previousWordButton.clicked.connect(Form.translatePreviousWord)
        self.previousSentenceButton.clicked.connect(Form.translatePreviousSentence)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textToTranslateInput.setPlaceholderText(_translate("Form", "Text to translate"))
        self.translatedTextInput.setPlaceholderText(_translate("Form", "Translated text"))
        self.startButton.setText(_translate("Form", "Start"))
        self.pauseButton.setText(_translate("Form", "Pause"))
        self.stopButton.setText(_translate("Form", "Stop"))
        self.previousSentenceButton.setText(_translate("Form", "<<"))
        self.previousWordButton.setText(_translate("Form", "<"))
        self.nextWordButton.setText(_translate("Form", ">"))
        self.nextSentenceButton.setText(_translate("Form", ">>"))
        self.resetButton.setText(_translate("Form", "Reset"))
        self.translateAllButton.setText(_translate("Form", "Trnaslate all"))
