from classes.insert_word_view import InsertWordView
from classes.game import Game

class InsertWordGame(Game):
    
    def __init__(self, fromLanguage, toLanguage):
        Game.__init__(self, fromLanguage, toLanguage)
        
        self.graphicView = InsertWordView(self)