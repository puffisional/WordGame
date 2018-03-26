from classes.game import Game
from classes.text_translate_view import TextTranslateView
from threading import Thread
from PyQt5.Qt import pyqtSignal

class TextTranslateGame(Game):
    
    onSentenceStepPlay = pyqtSignal(['QString'])
    
    def __init__(self, fromLanguage, toLanguage):
        Game.__init__(self, fromLanguage, toLanguage)
        
        self.graphicView = TextTranslateView(self)
        
    def startStepTranslation(self, translation):
        
        def readSentences():
            for index, translatedSentence in enumerate(translation.translations):
                self.onSentenceStepPlay.emit(translatedSentence.strip())
                self.sayWord(translation.sentences[index].strip(), self.fromLanguage, blocking=True)
                self.sayWord(translatedSentence.strip(), self.toLanguage, blocking=True)
        
        Thread(target=readSentences).start()