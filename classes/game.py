from googletrans import Translator
import os
import json
import time
import random

DICT_KNOWN = "Known"
DICT_UNKNOWN = "Unknown"

class Game():
    
    graphicView = None
    translator = Translator()
    dictionary = None
    dictionaryFile = os.path.join("./", "resources", "dictionary.data")
    
    def __init__(self, fromLanguage, toLanguage):
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
            
        self.saveWord("price", DICT_UNKNOWN)
        print(self.randomWord(DICT_UNKNOWN, self.toLanguage))
        
    def start(self):
        pass
       
    def translate(self, text):
        return self.translator.translate(text, self.toLanguage, self.fromLanguage)
    
    def nextWord(self):
        return "Fuck you"
    
    def saveWord(self, word, dictionary):
        self.dictionary[dictionary][self.fromLanguage][self.toLanguage][word] = (self.translate(word).text, time.time())
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
    
    def _initWordVector(self, dictionary):
        vector = list(self.dictionary[dictionary][self.fromLanguage][self.toLanguage].keys())
        self.wordVector = {dictionary:{self.fromLanguage:{self.toLanguage:vector}}}
