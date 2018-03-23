# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QWidget, QMainWindow, QApplication
from ui import mainWindowTemplate
from classes.guess_word_view import GuessWordView
from classes.guess_word_game import GuessWordGame
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
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    game = InsertWordGame("en", "de")
    w = MainWindow(game)
    w.show()
    
    app.exec_()