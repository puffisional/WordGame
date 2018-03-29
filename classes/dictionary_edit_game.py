from WordGame.classes.dictionary_edit_view import DictionaryEditView
from WordGame.classes.game import Game

class DictionaryEditGame(Game):
    
    def __init__(self, fromLanguage, toLanguage):
        Game.__init__(self, fromLanguage, toLanguage)
        
        self.graphicView = DictionaryEditView(self)