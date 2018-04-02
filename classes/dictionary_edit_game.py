from WordGame.classes.dictionary_edit_view import DictionaryEditView
from WordGame.classes.game import Game


class DictionaryEditGame(Game):
    
    def __init__(self, dictionary):
        Game.__init__(self, dictionary)
        
        self.graphicView = DictionaryEditView(self)
