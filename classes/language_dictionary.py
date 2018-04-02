import os
import json

DICT_KNOWN = "Known"
DICT_UNKNOWN = "Unknown"

class LanguageDictionary(dict):
    
    def __init__(self, dictionaryFilepath, fromLanguage, toLanguage):
        
        self.dictionaryFilepath = dictionaryFilepath
        self.fromLanguage = fromLanguage
        self.toLanguage = toLanguage
        self.wordVector = {}
        
        dict.__init__(self)
        
        if not os.path.exists(self.dictionaryFilepath):
            self[DICT_KNOWN] = {}
            self[DICT_UNKNOWN] = {}
            self.updateDictionaryFile()
        else:
            with open(self.dictionaryFilepath, "r") as fp:
                self.update(json.load(fp))
        
        for dictionary in self.keys():
            if self.fromLanguage not in self[dictionary]:
                self[dictionary][self.fromLanguage] = {}
            if self.toLanguage not in self[dictionary][self.fromLanguage]:
                self[dictionary][self.fromLanguage][self.toLanguage] = {}
            if self.toLanguage not in self[dictionary]:
                self[dictionary][self.toLanguage] = {}
            if self.fromLanguage not in self[dictionary][self.toLanguage]:
                self[dictionary][self.toLanguage][self.fromLanguage] = {}
            self._initWordVector(dictionary)
    
    def _initWordVector(self, dictionary):
        vector = list(self[dictionary][self.fromLanguage][self.toLanguage].keys())
        self.wordVector = {dictionary:{self.fromLanguage:{self.toLanguage:vector}}}
    
    def updateFile(self):
        with open(self.dictionaryFilepath, "w+") as fp:
            json.dump(self, fp)