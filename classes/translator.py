# -*- coding: utf-8 -*-

from googletrans import Translator as googleTranslator
from googletrans.compat import PY3, unicode
from googletrans.constants import LANGCODES, LANGUAGES, SPECIAL_CASES
from googletrans.client import EXCLUDES

class Translated():
    
    text = None
    wordClass = None
    translations = None
    
    def __init__(self, dest, data):
        self.translations = []
        self.text = data[0][0][0]
        if data[1] is not None:
            self.wordClass = data[1][0][0]
            
            for d in data[1]:
                if dest == "de" and d[0] == "Substantiv":
                    self.translations.append((d[0], ["%s %s" % (d[2][0][-1], w) for w in d[1]]))
                else:
                    self.translations.append((d[0], d[1]))
        else:
            self.translations.append(("word", [data[0][0][0]]))
        

class TranslatedSentence():
    
    sentences = None
    translations = None
    
    def __init__(self, dest, data):
        self.sentences = [] #data[0][0][1]
        self.translations = [] #data[0][0][0]
        
        for d in data[0]:
            self.sentences.append(d[1])
            self.translations.append(d[0])
        
class Translator(googleTranslator):
    
    def translate(self, text, dest='en', src='auto', translationClass=Translated):
        dest = dest.lower().split('_', 1)[0]
        src = src.lower().split('_', 1)[0]

        if src != 'auto' and src not in LANGUAGES:
            if src in SPECIAL_CASES:
                src = SPECIAL_CASES[src]
            elif src in LANGCODES:
                src = LANGCODES[src]
            else:
                raise ValueError('invalid source language')

        if dest not in LANGUAGES:
            if dest in SPECIAL_CASES:
                dest = SPECIAL_CASES[dest]
            elif dest in LANGCODES:
                dest = LANGCODES[dest]
            else:
                raise ValueError('invalid destination language')

        if isinstance(text, list):
            result = []
            for item in text:
                translated = self.translate(item, dest=dest, src=src)
                result.append(translated)
            return result

        origin = text
        data = self._translate(text, dest, src)
        
        # this code will be updated when the format is changed.
        translated = ''.join([d[0] if d[0] else '' for d in data[0]])

        # actual source language that will be recognized by Google Translator when the
        # src passed is equal to auto.
        try:
            src = data[2]
        except Exception:  # pragma: nocover
            pass

        pron = origin
        try:
            pron = data[0][1][-2]
        except Exception:  # pragma: nocover
            pass
        if not PY3 and isinstance(pron, unicode) and isinstance(origin, str):  # pragma: nocover
            origin = origin.decode('utf-8')
        if dest in EXCLUDES and pron == origin:
            pron = translated

        # for python 2.x compatbillity
        if not PY3:  # pragma: nocover
            if isinstance(src, str):
                src = src.decode('utf-8')
            if isinstance(dest, str):
                dest = dest.decode('utf-8')
            if isinstance(translated, str):
                translated = translated.decode('utf-8')
                
        # put final values into a new Translated object
        try:
            result = translationClass(dest, data)
        except Exception as e:
            print(e)
            return None
        
        return result
