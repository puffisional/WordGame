from classes.graphic_view import GraphicView
from PyQt5.QtWidgets import QPushButton
from WordGame.ui.insertWordTemplate import Ui_Form

class InsertWordView(Ui_Form, GraphicView):
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        
        self.dictionarySelect.addItems(self.game.dictionary.keys())
        
    def translateWord(self):
        word = self.wordInput.text()
        fromLanguage = self.wordLanguageSelect.currentText()
        toLanguage = self.translationLanguageSelect.currentText()
        translation = self.game.translate(word, fromLanguage, toLanguage)
        self.translationInput.setText(translation.text)
        
    def playWord(self):
        word = self.wordInput.text()
        language = self.wordLanguageSelect.currentText()
        self.game.sayWord(word, language)
    
    def playTranslation(self):
        word = self.translationInput.text()
        language = self.translationLanguageSelect.currentText()
        self.game.sayWord(word, language)
    
    def removeWord(self):
        pass
    
    def saveWord(self):
        fromLanguage = self.wordLanguageSelect.currentText()
        toLanguage = self.translationLanguageSelect.currentText()
        translation = self.translationInput.text()
        dictionary = self.dictionarySelect.currentText()
        self.game.insertWord(translation, dictionary, fromLanguage, toLanguage)
        
    def switchWordInput(self):
        fromLanguage = self.wordLanguageSelect.currentText()
        toLanguage = self.translationLanguageSelect.currentText()
        word = self.wordInput.text()
        translation = self.translationInput.text()
        
        self.wordLanguageSelect.setCurrentIndex(self.wordLanguageSelect.findText(toLanguage))
        self.translationLanguageSelect.setCurrentIndex(self.translationLanguageSelect.findText(fromLanguage))
        self.translationInput.setText(word)
        self.wordInput.setText(translation)
        