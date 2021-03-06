# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QMainWindow, QApplication
from ui import mainWindowTemplate
from WordGame.classes.insert_word_game import InsertWordGame
from PyQt5.QtWidgets import QErrorMessage
from WordGame.classes.text_translate_game import TextTranslateGame
from classes.dictionary_edit_game import DictionaryEditGame
from classes.game import Game
from classes.language_dictionary import LanguageDictionary
import os


class MainWindow(QMainWindow, mainWindowTemplate.Ui_MainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.languageDictionary = LanguageDictionary(os.path.join("./", "resources", "dictionary.data"), "en", "de")
        self.games = [InsertWordGame(self.languageDictionary),
                      TextTranslateGame(self.languageDictionary),
                      DictionaryEditGame(self.languageDictionary)]
        
        self.game = self.games[0]
        self._init_ui()
        
    def _init_ui(self):
        self.setupUi(self)
        
        self.errorDialog = QErrorMessage(self.window())
        self.statusbar.hide()
        
        self.game.onError.connect(self.showError)
        
        self.setActiveView(0)
    
    def showError(self, message):
        self.errorDialog.showMessage(message)
    
    def setFromLanguage(self, language):
        self.game.setFromLanguage(language)
        
    def setToLanguage(self, language):
        self.game.setToLanguage(language)
    
    def switchLanguage(self):
        self.game.switchLanguage()
        
        fromLanguage = self.wordLanguageSelect.currentText()
        toLanguage = self.translationLanguageSelect.currentText()
        
        self.wordLanguageSelect.setCurrentIndex(self.wordLanguageSelect.findText(toLanguage))
        self.translationLanguageSelect.setCurrentIndex(self.translationLanguageSelect.findText(fromLanguage))
    
    def setActiveView(self, index):
        if self.game:
            self.game.graphicView.setParent(None)
        
        self.game = self.games[index]
        self.graphicsFrame.layout().addWidget(self.game.graphicView)
        
        for _ in range(10):
            app.processEvents()
        
#         self.adjustSize()

    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    
    app.exec_()
