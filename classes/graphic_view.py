
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication

class GraphicView(QWidget):
    
    def __init__(self, game):
        self.game = game
        QWidget.__init__(self)
        self._init_ui()
    
    def setupUi(self, form):
        pass
    
    def _init_ui(self):
        self.setupUi(self)
    
    def resizeToMinimum(self):
        for _ in range(10):
            QApplication.processEvents()
        
        self.window().adjustSize()