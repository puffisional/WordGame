from classes.graphic_view import GraphicView
from PyQt5.QtWidgets import QPushButton
from WordGame.ui.guessWorldTemplate import Ui_Form

class GuessWordView(Ui_Form, GraphicView):
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        
        self.buttonLayout.addWidget(QPushButton("Kakacik"))
        self.graphicsWidget.layout().addWidget(QPushButton("Kakacik"))