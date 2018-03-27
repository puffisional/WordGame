from classes.game import Game
from classes.text_translate_view import TextTranslateView
from threading import Thread
from PyQt5.Qt import pyqtSignal
from threading import Event


class TextTranslateGame(Game):
    
    onSentenceStepPlay = pyqtSignal(['QString', 'int', 'int'])
    stopEvent = Event()
    readOriginalFlag = True
    
    def __init__(self, fromLanguage, toLanguage):
        Game.__init__(self, fromLanguage, toLanguage)
        
        self.graphicView = TextTranslateView(self)
        
    def startStepTranslation(self, translation):
        if self.stopEvent.isSet(): return
        
        self.stopEvent.clear()
        steps = []
        
        sentenceStart = 0
        for index, originalSentence in enumerate(translation.sentences):
            sentenceEnd = sentenceStart + len(originalSentence)
            steps.append((sentenceStart, sentenceEnd, originalSentence, translation.translations[index]))
            sentenceStart = sentenceEnd
        
        def readSentences():
            
            for sentenceStart, sentenceEnd, sentence, translation in steps:
                if self.stopEvent.isSet(): break
                self.onSentenceStepPlay.emit(translation, sentenceStart, sentenceEnd)
                
                if self.readOriginalFlag:
                    self.sayWord(sentence, self.fromLanguage, blocking=True)
                    
                if self.stopEvent.isSet(): break
                self.sayWord(translation, self.toLanguage, blocking=True)
                
            self.stopEvent.clear()
        
        Thread(target=readSentences).start()
    
    def stopStepTranslation(self):
        self.stopEvent.set()