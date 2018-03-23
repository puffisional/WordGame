
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.Qt import QPainter, QRectF, QRect, QBrush, Qt, QOpenGLContext,\
    QWidget, QTimer, QPoint

class GraphicView(QWidget):
    
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self._init_ui()
    
    def setupUi(self, form):
        pass
    
    def _init_ui(self):
        self.setupUi(self)