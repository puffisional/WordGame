from classes.graphic_view import GraphicView
from WordGame.ui.insertWordTemplate import Ui_Form
from PyQt5.Qt import pyqtSlot


class InsertWordView(Ui_Form, GraphicView):
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        self.dictionarySelect.addItems(self.game.dictionary.keys())
        
        self.game.onLanguageSwitch.connect(self.onLanguageSwitch)
        self.game.onWordTranslated.connect(self.onWordTranslated)
        
    def translateWord(self):
        word = self.wordInput.text()
        self.game.translate(word)
        
    def playWord(self):
        word = self.wordInput.text()
        self.game.sayWord(word, self.game.fromLanguage)
    
    def playTranslation(self):
        word = self.translationInput.text()
        self.game.sayWord(word, self.game.toLanguage)
    
    def saveWord(self):
        word = self.wordInput.text()
        translation = self.translationInput.text()
        dictionary = self.dictionarySelect.currentText()
        self.game.insertWord(word, translation, dictionary)
    
    @pyqtSlot()
    def onLanguageSwitch(self):
        word = self.wordInput.text()
        translation = self.translationInput.text()
        
        self.translationInput.setText(word)
        self.wordInput.setText(translation)
    
    @pyqtSlot('QString', 'QString')   
    def onWordTranslated(self, word, translation):
        self.translationInput.setText(translation)
