from classes.graphic_view import GraphicView
from PyQt5.QtWidgets import QPushButton, QGridLayout, QTableWidgetItem,\
    QHeaderView, QApplication, QLabel
from WordGame.ui.dictionaryEditTemplate import Ui_Form
from classes.qTableWidgetInteractive import QTableWidgetInteractive
from PyQt5.Qt import pyqtSlot

class DictionaryEditView(Ui_Form, GraphicView):
    
    def _init_ui(self):
        GraphicView._init_ui(self)
        
        self.dictionaryTable = QTableWidgetInteractive()
        self.dictionaryWordsFrame.layout().addWidget(self.dictionaryTable)
        
        self.dictionaryTable.setColumnCount(2)
        self.dictionaryTable.setRowCount(0)
        
        for index, headerTitle in enumerate(["Word", "Translation"]):
            item = QTableWidgetItem(headerTitle)
            self.dictionaryTable.setHorizontalHeaderItem(index, item)

#         self.dictionaryTable.horizontalHeader().resizeSection(0, 160)
        self.dictionaryTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.dictionaryTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        self.dictionarySelect.addItems(self.game.dictionary.keys())
        self.moveDictionarySelect.addItems(self.game.dictionary.keys())
        
        self.game.onDictionaryAdd.connect(self.onDictionaryAdd)
        self.game.onDictionaryRemove.connect(self.onDictionaryRemove)
        self.game.onWordMove.connect(self.onWordMove)
        
        self.dictionaryTable.cellDoubleClicked.connect(self.sayWord)
        
    @pyqtSlot()
    def addDictionary(self):
        dictionary = self.dictionaryNameInput.text()
        self.game.addDictionary(dictionary)
    
    @pyqtSlot()
    def removeDictionary(self):
        dictionary = self.dictionarySelect.currentText()
        self.game.removeDictionary(dictionary)
    
    @pyqtSlot()
    def moveWord(self):
        
        ranges = self.dictionaryTable._getRanges(True)
        fromDictionary = self.dictionarySelect.currentText()
        toDictionary = self.moveDictionarySelect.currentText()
        words = []
        for start, end in ranges:
            for row in range(start, end+1):
                words.append( self.dictionaryTable.cellWidget(row, 0).text() )
        
        self.game.moveWord(words, fromDictionary, toDictionary)

    @pyqtSlot('QString')
    def changeDictionary(self, dictionary):
        words = self.game.getWords(dictionary)
        self.dictionaryTable.setRowCount(0)
        
        for _ in range(10):
            QApplication.processEvents()
        
        self.dictionaryTable.setRowCount(len(words.keys()))
        
        for row, (key, item) in enumerate(words.items()):
            self.dictionaryTable.setCellWidget(row, 0, QLabel(key))
            self.dictionaryTable.setCellWidget(row, 1, QLabel(item))
        
    @pyqtSlot('QString')    
    def onDictionaryAdd(self, dictionary):
        self.dictionarySelect.addItem(dictionary)
        self.moveDictionarySelect.addItem(dictionary)
        
    @pyqtSlot('QString')    
    def onDictionaryRemove(self, dictionary):
        index = self.dictionarySelect.findText(dictionary)
        self.dictionarySelect.removeItem(index)
        self.moveDictionarySelect.removeItem(index)
    
    @pyqtSlot('int', 'int') 
    def sayWord(self, row, column):
        language = (self.game.fromLanguage, self.game.toLanguage)[column]
        word = self.dictionaryTable.cellWidget(row, column).text()
        
        self.game.sayWord(word, language)
    
    @pyqtSlot('PyQt_PyObject', 'QString', 'QString', 'QString', 'QString') 
    def onWordMove(self, words, fromDictionary, toDictionary, fromLanguage, toLanguage):
        self.changeDictionary(fromDictionary)