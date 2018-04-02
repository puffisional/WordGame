from WordGame.classes.insert_word_view import InsertWordView
from WordGame.classes.game import Game

class InsertWordGame(Game):
    
    def __init__(self, dictionary):
        Game.__init__(self, dictionary)
        self.graphicView = InsertWordView(self)