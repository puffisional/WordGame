# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QMainWindow, QApplication
from ui import mainWindowTemplate
from classes.insert_word_game import InsertWordGame


class MainWindow(QMainWindow, mainWindowTemplate.Ui_MainWindow):
    
    def __init__(self, game):
        QMainWindow.__init__(self)
        self.game = game
        self._init_ui()
        
    def _init_ui(self):
        self.setupUi(self)
        
        self.graphicsFrame.layout().addWidget(self.game.graphicView)
        self.statusbar.hide()
        
    def setFromLanguage(self, language):
        self.game.fromLanguage = language
        
    def setToLanguage(self, language):
        self.game.toLanguage = language
    
    def switchLanguage(self):
        self.game.switchLanguage()
        
        fromLanguage = self.wordLanguageSelect.currentText()
        toLanguage = self.translationLanguageSelect.currentText()
        
        self.wordLanguageSelect.setCurrentIndex(self.wordLanguageSelect.findText(toLanguage))
        self.translationLanguageSelect.setCurrentIndex(self.translationLanguageSelect.findText(fromLanguage))

    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    game = InsertWordGame("en", "de")
    w = MainWindow(game)
    w.show()
    
    for _ in range(10):
        app.processEvents()
        
    w.adjustSize()
    
    app.exec_()
