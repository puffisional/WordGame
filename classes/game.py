from googletrans import Translator
import json
import os
import random
from google_speech import Speech
from PyQt5.Qt import QObject, pyqtSignal
from threading import Event, Thread

DICT_KNOWN = "Known"
DICT_UNKNOWN = "Unknown"


class Game(QObject):
    
    graphicView = None
    translator = Translator()
    dictionary = None
    dictionaryFile = os.path.join("./", "resources", "dictionary.data")
    
    onLanguageSwitch = pyqtSignal()
    onWordTranslated = pyqtSignal(['QString', 'QString'])
    
    def __init__(self, fromLanguage, toLanguage):
        QObject.__init__(self)
        
        self.voicePlayEvent = Event()
        self.fromLanguage = fromLanguage
        self.toLanguage = toLanguage
        
        if not os.path.exists(self.dictionaryFile):
            self.dictionary = {
                DICT_KNOWN:{},
                DICT_UNKNOWN:{},
                }
            self.updateDictionaryFile()
        else:
            with open(self.dictionaryFile, "r") as fp:
                self.dictionary = json.load(fp)
        
        for dictionary in self.dictionary.keys():
            if self.fromLanguage not in self.dictionary[dictionary]:
                self.dictionary[dictionary][self.fromLanguage] = {}
            if self.toLanguage not in self.dictionary[dictionary][self.fromLanguage]:
                self.dictionary[dictionary][self.fromLanguage][self.toLanguage] = {}
            self._initWordVector(dictionary)
            
    def start(self):
        pass
    
    def translate(self, text, fromLanguage=None, toLanguage=None):
        if fromLanguage is None: fromLanguage = self.fromLanguage
        if toLanguage is None: toLanguage = self.toLanguage
        
        def _translate():
            translatedText = self.translator.translate(text, toLanguage, fromLanguage)
            self.onWordTranslated.emit(text, translatedText.text)
            
        Thread(target=_translate).start()
    
    def nextWord(self):
        return "Fuck you"
    
    def insertWord(self, word, translation, dictionary, fromLanguage=None, toLanguage=None):
        if fromLanguage is None: fromLanguage = self.fromLanguage
        if toLanguage is None: toLanguage = self.toLanguage
        self.dictionary[dictionary][fromLanguage][toLanguage][word] = translation
        self.updateDictionaryFile()
        
    def updateDictionaryFile(self):
        with open(self.dictionaryFile, "w+") as fp:
            json.dump(self.dictionary, fp)
    
    def randomWord(self, dictionary, language):
        fromWord = random.choice(self.wordVector[dictionary][self.fromLanguage][self.toLanguage])
        if language == self.fromLanguage:
            return fromWord
        else:
            return self.dictionary[dictionary][self.fromLanguage][self.toLanguage][fromWord][0]
    
    def evaluate(self, word, quess):
        return word == quess
    
    def sayWord(self, word, language):
        if self.voicePlayEvent.isSet(): return
        
        def _play():
            self.voicePlayEvent.set()
            voice = Speech(word, language)
            voice.play(["speed", "1", "pad", "0.8", "0.8"])
            self.voicePlayEvent.clear()
            
        Thread(target=_play).start()
        
    def _initWordVector(self, dictionary):
        vector = list(self.dictionary[dictionary][self.fromLanguage][self.toLanguage].keys())
        self.wordVector = {dictionary:{self.fromLanguage:{self.toLanguage:vector}}}
    
    def switchLanguage(self):
        self.fromLanguage, self.toLanguage = self.toLanguage, self.fromLanguage
        self.onLanguageSwitch.emit()