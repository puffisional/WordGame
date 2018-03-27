from classes.graphic_view import GraphicView
from PyQt5.QtWidgets import QPushButton
from WordGame.ui.textTranslateTemplate import Ui_Form
from PyQt5.QtGui import QTextCursor
import re

ACTION_TRANSLATE_ALL = 0
ACTION_START_TRANSLATION = 1


class TextTranslateView(Ui_Form, GraphicView):
    
    currentAction = ACTION_TRANSLATE_ALL
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        
        self.game.onSentenceTranslated.connect(self.onSentenceTranslated)
        self.game.onSentenceStepPlay.connect(self.setStepSentenceTranslation)
    
    def setStepSentenceTranslation(self, sentence, sentenceStart, sentenceEnd):
        self.translatedTextInput.setPlainText(sentence)
        
        cursor = self.textToTranslateInput.textCursor()
        cursor.setPosition(sentenceStart)
        cursor.setPosition(sentenceEnd, QTextCursor.KeepAnchor)
        self.textToTranslateInput.setTextCursor(cursor)
        self.textToTranslateInput.setFocus()
    
    def translateAll(self):
        self.currentAction = ACTION_TRANSLATE_ALL
        
        inputText = self.textToTranslateInput.toPlainText()
        if inputText == '': return
        
        self.game.translateSentence(inputText)
    
    def startTranslation(self):
        self.currentAction = ACTION_START_TRANSLATION
        inputText = re.split("\.+|\?+|\!+|;+", self.textToTranslateInput.toPlainText())
        inputText = ".\n".join([sentence.strip() for sentence in inputText])
        self.textToTranslateInput.setPlainText(inputText.strip())
        if inputText == '': return
        
        self.game.readOriginalFlag = self.readOriginalCheckbox.isChecked()
        self.game.translateSentence(inputText)
       
    def onSentenceTranslated(self, sentence, translation):
        if self.currentAction == ACTION_TRANSLATE_ALL:
            self.translatedTextInput.setPlainText(" ".join(translation.translations))
        elif self.currentAction == ACTION_START_TRANSLATION:
            self.game.startStepTranslation(translation)

    def stopTranslation(self):
        self.game.stopStepTranslation()
    
    def pauseTranslation(self):
        pass
    
    def translateNextWord(self):
        pass
    
    def translateNextSentence(self):
        pass
    
    def translatePreviousWord(self):
        pass
    
    def translatePreviousSentence(self):
        pass
