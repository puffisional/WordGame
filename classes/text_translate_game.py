from classes.game import Game
from classes.text_translate_view import TextTranslateView
from threading import Thread
from PyQt5.Qt import pyqtSignal
from threading import Event
from classes.language_dictionary import DICT_UNKNOWN


class TextTranslateGame(Game):
    
    onSentenceStepPlay = pyqtSignal(['QString', 'int', 'int'])
    stopEvent = Event()
    readOriginalFlag = True
    
    def __init__(self, dictionary):
        Game.__init__(self, dictionary)
        
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
                    self.sayWord(sentence, self.fromLanguage(), blocking=True)
                    
                if self.stopEvent.isSet(): break
                self.sayWord(translation, self.toLanguage(), blocking=True)
                
                for word in sentence.split():
                    translation = self.translate(word, blocking=True)
                    if translation is None: continue
                    
                    if not self.isWordKnown(word):
                        self.insertWord(word, translation.translations[0][1][0], DICT_UNKNOWN)
                
            self.stopEvent.clear()
        
        Thread(target=readSentences).start()
    
    def stopStepTranslation(self):
        self.stopEvent.set()