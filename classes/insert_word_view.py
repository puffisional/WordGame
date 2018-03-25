# -*- coding: utf-8 -*-

from classes.graphic_view import GraphicView
from WordGame.ui.insertWordTemplate import Ui_Form
from PyQt5.Qt import pyqtSlot, QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QHBoxLayout,\
    QSpacerItem, QSizePolicy
from PyQt5 import QtCore


class InsertWordView(Ui_Form, GraphicView):
    
    def __init__(self, game):
        self.translatedWordWidgets = []
        GraphicView.__init__(self, game)
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        
        self.dictionaryWidgets = (self.dictionaryLabel, self.dictionarySelect, self.dictionaryAddButton)
        self.dictionarySelect.addItems(self.game.dictionary.keys())
        self.game.onLanguageSwitch.connect(self.onLanguageSwitch)
        self.game.onWordTranslated.connect(self.onWordTranslated)
        
        self.resizeToMinimum()
    
    @pyqtSlot()
    def translateWord(self):
        word = self.wordInput.text()
        self.game.translate(word)
    
    @pyqtSlot()   
    def playWord(self):
        word = self.wordInput.text()
        self.game.sayWord(word, self.game.fromLanguage)
    
    @pyqtSlot('QString')
    def playTranslation(self, word):
        self.game.sayWord(word, self.game.toLanguage)
    
    @pyqtSlot()
    def saveWord(self):
        word = self.wordInput.text()
        translation = self.translationInput.text()
        dictionary = self.dictionarySelect.currentText()
        self.game.insertWord(word, translation, dictionary)
    
    @pyqtSlot()
    def onLanguageSwitch(self):
        return
        word = self.wordInput.text()
        translation = self.translationInput.text()
        
        self.translationInput.setText(word)
        self.wordInput.setText(translation)
    
    @pyqtSlot('QString', 'PyQt_PyObject')   
    def onWordTranslated(self, word, translation):
        for widgets in self.translatedWordWidgets:
            for widget in widgets: widget.setParent(None)
            
        self.translatedWordWidgets = []
        
        row = 2
        for wordType, translations in translation.translations:
            self._addTranslatedWord(row, wordType, translations)
            row += 1
        
        self._moveDictionaryWidgets(row + 1)
        self.resizeToMinimum()
    
    def _addTranslatedWord(self, row, wordType, translations):
        label = QLabel("%s:" % wordType)
        label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        inputTranslation = QWidget()
        inputTranslation.setLayout(QHBoxLayout())
        inputTranslation.layout().setContentsMargins(0, 0, 0, 0)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        inputTranslation.setSizePolicy(sizePolicy)
        
        for translatedWord in translations[:5]:
            wordButton = QPushButton(translatedWord)
            wordButton.setSizePolicy(sizePolicy)
            inputTranslation.layout().addWidget(wordButton)
            wordButton.clicked.connect(lambda event, word=translatedWord: self.playTranslation(word))
                
        self.layout().addWidget(label, row, 0)
        self.layout().addWidget(inputTranslation, row, 1, 1, 2)
        
        self.translatedWordWidgets.append((label, inputTranslation))
        
    def _moveDictionaryWidgets(self, row):
        for column, widget in enumerate(self.dictionaryWidgets):
            self.layout().addWidget(widget, row, column)
