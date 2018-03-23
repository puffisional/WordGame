import sys
from PyQt5.Qt import QWidget, QMainWindow, QApplication
from ui import mainWindowTemplate
from classes.guess_word_view import GuessWordView
from googletrans import Translator
from google_speech import Speech, SpeechSegment
from classes.guess_word_game import GuessWordGame

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
    game = GuessWordGame("en", "de")
    w = MainWindow(game)
    w.show()
    
    app.exec_()
    
