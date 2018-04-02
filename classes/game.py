import random
from google_speech import Speech
from PyQt5.Qt import QObject, pyqtSignal
from threading import Event, Thread
from classes.translator import Translator, TranslatedSentence
from builtins import isinstance

Speech.MAX_SEGMENT_SIZE = 200


class Game(QObject):
    
    graphicView = None
    translator = Translator()
    
    onLanguageSwitch = pyqtSignal()
    onTranslationStart = pyqtSignal()
    onWordTranslated = pyqtSignal(['QString', 'PyQt_PyObject'])
    onSentenceTranslated = pyqtSignal(['QString', 'PyQt_PyObject'])
    onTranslationEnd = pyqtSignal()
    onError = pyqtSignal(['QString'])
    onDictionaryAdd = pyqtSignal(['QString'])
    onDictionaryRemove = pyqtSignal(['QString'])
    onWordMove = pyqtSignal(['PyQt_PyObject', 'QString', 'QString', 'QString', 'QString'])
    
    def __init__(self, dictionary):
        QObject.__init__(self)
        
        self.voicePlayEvent = Event()
        self.dictionary = dictionary
            
    def start(self):
        pass
    
    def translate(self, word, fromLanguage=None, toLanguage=None, blocking=False):
        if fromLanguage is None: fromLanguage = self.fromLanguage()
        if toLanguage is None: toLanguage = self.toLanguage()
        
        def _translate():
            self.onTranslationStart.emit()
            translation = self.translator.translate(word, toLanguage, fromLanguage)
            if translation is not None:
                self.onWordTranslated.emit(word, translation)
            else:
                self.onError.emit("Translation error")
            self.onTranslationEnd.emit()
            return translation
        
        if not blocking:       
            Thread(target=_translate).start()
        else: 
            return _translate()   
    
    def translateSentence(self, sentence, fromLanguage=None, toLanguage=None, blocking=False):
        if fromLanguage is None: fromLanguage = self.fromLanguage()
        if toLanguage is None: toLanguage = self.toLanguage()
        
        def _translate():
            self.onTranslationStart.emit()
            translation = self.translator.translate(sentence, toLanguage, fromLanguage, translationClass=TranslatedSentence)
            if translation is not None:
                self.onSentenceTranslated.emit(sentence, translation)
            else:
                self.onError.emit("Translation error")
            self.onTranslationEnd.emit()
            return translation
        
        if not blocking:       
            Thread(target=_translate).start()
        else: 
            return _translate()   
    
    def insertWord(self, word, translation, dictionary, fromLanguage=None, toLanguage=None):
        if fromLanguage is None: fromLanguage = self.fromLanguage()
        if toLanguage is None: toLanguage = self.toLanguage()
        
        self.dictionary[dictionary][fromLanguage][toLanguage][word] = translation
        self.dictionary.updateFile()
        
    def randomWord(self, dictionary, language):
        fromWord = random.choice(self.wordVector[dictionary][self.fromLanguage()][self.toLanguage()])
        if language == self.fromLanguage():
            return fromWord
        else:
            return self.dictionary[dictionary][self.fromLanguage()][self.toLanguage()][fromWord][0]
    
    def evaluate(self, word, quess):
        return word == quess
    
    def sayWord(self, word, language, blocking=False):
        def _play():
            self.voicePlayEvent.set()
            voice = Speech(word, language)
            voice.play(["speed", "1", "pad", "1", "1"])
            self.voicePlayEvent.clear()
        
        if not blocking:   
            Thread(target=_play).start()
        else:
            _play()
            
    def getWords(self, dictionary, fromLanguage=None, toLanguage=None):
        if fromLanguage is None: fromLanguage = self.fromLanguage()
        if toLanguage is None: toLanguage = self.toLanguage()
        return self.dictionary[dictionary][fromLanguage][toLanguage]
    
    def switchLanguage(self):
        toLaguage, fromLanguage = self.toLanguage(), self.fromLanguage()
        self.setToLanguage(fromLanguage)
        self.setFromLanguage(toLaguage)
        self.onLanguageSwitch.emit()

    def addDictionary(self, dictionary):
        if self.dictionary.get(dictionary) is None:
            self.dictionary[dictionary] = {}
            self.dictionary[dictionary][self.fromLanguage()] = {}
            self.dictionary[dictionary][self.fromLanguage()][self.toLanguage()] = {}
                
            self.dictionary.updateFile()
            self.onDictionaryAdd.emit(dictionary)
    
    def removeDictionary(self, dictionary):
        if self.dictionary.get(dictionary) is None: return
        
        del self.dictionary[dictionary][self.fromLanguage()]
        self.onDictionaryRemove.emit(dictionary)
        self.dictionary.updateFile()
    
    def moveWord(self, words, fromDictionary, toDictionary, fromLanguage=None, toLanguage=None):
        if not isinstance(words, (tuple, list)):
            words = [words]
        if fromLanguage is None: fromLanguage = self.fromLanguage()
        if toLanguage is None: toLanguage = self.toLanguage()
        
        dictionary = self.dictionary[fromDictionary][fromLanguage][toLanguage]
        
        for word in words:
            translation = dictionary[word]
            del dictionary[word]
            self.dictionary[toDictionary][fromLanguage][toLanguage][word] = translation
            
        self.dictionary.updateFile()
        self.onWordMove.emit(words, fromDictionary, toDictionary, fromLanguage, toLanguage)
    
    
    def fromLanguage(self):
        return self.dictionary.fromLanguage
    
    def toLanguage(self):
        return self.dictionary.toLanguage
    
    def setFromLanguage(self, language):
        self.dictionary.fromLanguage = language
        
    def setToLanguage(self, language):
        self.dictionary.toLanguage = language