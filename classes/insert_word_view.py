# -*- coding: utf-8 -*-

from classes.graphic_view import GraphicView
from WordGame.ui.insertWordTemplate import Ui_Form
from PyQt5.Qt import pyqtSlot, QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QHBoxLayout, \
    QSpacerItem, QSizePolicy
from PyQt5 import QtCore


class InsertWordView(Ui_Form, GraphicView):
    
    lastTranslation = None
    
    def __init__(self, game):
        self.translatedWordWidgets = []
        GraphicView.__init__(self, game)
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        
        self.dictionaryWidgets = (self.dictionaryLabel, self.dictionarySelect, self.dictionaryAddButton)
        self.dictionarySelect.addItems(self.game.dictionary.keys())
        self.game.onWordTranslated.connect(self.onWordTranslated)
        self.game.onError.connect(self.gameError)
        
        self.resizeToMinimum()
    
    @pyqtSlot()
    def translateWord(self):
        word = self.wordInput.text()
        if word == "": return
        
        self.game.translate(word)
    
    @pyqtSlot()   
    def playWord(self):
        word = self.wordInput.text()
        self.game.sayWord(word, self.game.fromLanguage())
    
    @pyqtSlot('QString')
    def playTranslation(self, word):
        self.game.sayWord(word, self.game.toLanguage())
    
    @pyqtSlot()
    def saveWord(self):
        word, translation = self.lastTranslation
        dictionary = self.dictionarySelect.currentText()
        self.game.insertWord(word, translation.translations[0][1][0], dictionary)
    
    @pyqtSlot('QString', 'PyQt_PyObject')   
    def onWordTranslated(self, word, translation):
        for widgets in self.translatedWordWidgets:
            for widget in widgets: widget.setParent(None)
        
        self.lastTranslation = (word, translation)   
        self.translatedWordWidgets = []
        
        row = 2
        for wordType, translations in translation.translations:
            self._addTranslatedWord(row, wordType, translations)
            row += 1
        
        self._moveDictionaryWidgets(row + 1)
        self.resizeToMinimum()
    
    def gameError(self, message):
        self.wordInput.setText("")
    
    def _addTranslatedWord(self, row, wordType, translations):
        label = QLabel("%s:" % wordType)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        inputTranslation = QWidget()
        inputTranslation.setLayout(QHBoxLayout())
        inputTranslation.layout().setContentsMargins(0, 0, 0, 0)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        inputTranslation.setSizePolicy(sizePolicy)
        
        for translatedWord in translations[:5]:
            wordButton = QPushButton(translatedWord)
            wordButton.setSizePolicy(sizePolicy)
            wordButton.clicked.connect(lambda event, word=translatedWord: self.playTranslation(word))
            inputTranslation.layout().addWidget(wordButton)
                
        self.layout().addWidget(label, row, 0)
        self.layout().addWidget(inputTranslation, row, 1, 1, 2)
        
        wordButton.setFocus()
        self.translatedWordWidgets.append((label, inputTranslation))
        
    def _moveDictionaryWidgets(self, row):
        for column, widget in enumerate(self.dictionaryWidgets):
            self.layout().addWidget(widget, row, column)
