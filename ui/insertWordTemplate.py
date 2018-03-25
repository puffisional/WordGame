# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\insertWordTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1131, 173)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.wordInput = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordInput.sizePolicy().hasHeightForWidth())
        self.wordInput.setSizePolicy(sizePolicy)
        self.wordInput.setPlaceholderText("")
        self.wordInput.setClearButtonEnabled(False)
        self.wordInput.setObjectName("wordInput")
        self.gridLayout.addWidget(self.wordInput, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dictionaryLabel = QtWidgets.QLabel(Form)
        self.dictionaryLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dictionaryLabel.setObjectName("dictionaryLabel")
        self.gridLayout.addWidget(self.dictionaryLabel, 1, 0, 1, 1)
        self.playWordButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playWordButton.sizePolicy().hasHeightForWidth())
        self.playWordButton.setSizePolicy(sizePolicy)
        self.playWordButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playWordButton.setIcon(icon)
        self.playWordButton.setIconSize(QtCore.QSize(20, 20))
        self.playWordButton.setObjectName("playWordButton")
        self.gridLayout.addWidget(self.playWordButton, 0, 2, 1, 1)
        self.dictionarySelect = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionarySelect.sizePolicy().hasHeightForWidth())
        self.dictionarySelect.setSizePolicy(sizePolicy)
        self.dictionarySelect.setObjectName("dictionarySelect")
        self.gridLayout.addWidget(self.dictionarySelect, 1, 1, 1, 1)
        self.dictionaryAddButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionaryAddButton.sizePolicy().hasHeightForWidth())
        self.dictionaryAddButton.setSizePolicy(sizePolicy)
        self.dictionaryAddButton.setMinimumSize(QtCore.QSize(0, 0))
        self.dictionaryAddButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dictionaryAddButton.setObjectName("dictionaryAddButton")
        self.gridLayout.addWidget(self.dictionaryAddButton, 1, 2, 1, 1)

        self.retranslateUi(Form)
        self.wordInput.editingFinished.connect(Form.translateWord)
        self.playWordButton.clicked.connect(Form.playWord)
        self.dictionaryAddButton.clicked.connect(Form.saveWord)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.wordInput, self.playWordButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Word:"))
        self.dictionaryLabel.setText(_translate("Form", "Dictionary:"))
        self.playWordButton.setText(_translate("Form", "Play"))
        self.dictionaryAddButton.setText(_translate("Form", "Add"))

import resources_rc
