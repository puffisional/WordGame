from classes.guess_word_view import GuessWordView
from classes.game import Game

class GuessWordGame(Game):
    
    def __init__(self, fromLanguage, toLanguage):
        self.graphicView = GuessWordView()
        Game.__init__(self, fromLanguage, toLanguage)
        
    