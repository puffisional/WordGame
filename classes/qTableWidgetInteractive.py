# -*- coding: utf-8 -*-
'''
##########    MAIN IMPORTS    ##########
'''

# GLOBAL IMPORTS
from numpy import sign
from PyQt5.QtCore import pyqtSignal, QItemSelectionModel
from PyQt5.QtWidgets import QTableWidget, QWidget, QHBoxLayout
from PyQt5.Qt import Qt

'''
########## CLASS DECLARATIONS ##########
'''

class QTableWidgetInteractive(QTableWidget):
    
    SigselectionMoveUp = pyqtSignal(object)
    SigselectionMoveDown = pyqtSignal(object)
    SigselectionMoveTop = pyqtSignal(object)
    SigselectionMoveBottom = pyqtSignal(object)
    SigselectionRemoved = pyqtSignal(object)
    
    def setCellWidget(self, *args, **kwargs):
        row, column, widget = args[0], args[1], args[2]
        self._updateItemMeta(widget, row, column)
        return QTableWidget.setCellWidget(self, *args, **kwargs)
    
    def moveUp(self, ranges=None):
        if ranges is None: ranges = self._getRanges()           
        self._moveRange(ranges, 1)
        self.SigselectionMoveUp.emit(ranges)
        return True
    
    def moveDown(self, ranges=None):
        if ranges is None: ranges = self._getRanges(True)
        self._moveRange(ranges, -1)
        self.SigselectionMoveDown.emit(ranges)
        return True
    
    def moveTop(self, ranges=None):
        if ranges is None: ranges = self._getRanges()
        pos = ranges[0][0]
        self._moveRange(ranges, pos)
        self.SigselectionMoveTop.emit(ranges)
        return True
    
    def moveBottom(self, ranges=None):
        if ranges is None: ranges = self._getRanges(True)
        pos = ranges[0][1]
        rows = self.rowCount()
        self._moveRange(ranges, (pos - rows) + 1)
        self.SigselectionMoveBottom.emit(ranges)
        return True
    
    def moveRelative(self, rowIndex, byRows):
        rows = self.rowCount()
        
        if (rowIndex == 0 and byRows >= 0) or ((rowIndex + 1) == rows and byRows <= 0): return False
        
        if sign(byRows) == 1:
            retIndex = newRowIndex = rowIndex - byRows
            oldRowIndex = rowIndex + 1
        else:
            newRowIndex = rowIndex + (-byRows + 1)
            oldRowIndex = rowIndex
            retIndex = newRowIndex - 1
        
        self.insertRow(newRowIndex)

        for i in range(self.columnCount()):
            item = self.takeItem(oldRowIndex, i)
            if item is not None:
                self.setItem(newRowIndex, i, item)
            else:
                item = self.cellWidget(oldRowIndex, i)
                self.setCellWidget(newRowIndex, i, item)
            
        self.removeRow(oldRowIndex)
        
        return retIndex
    
    def _updateItemMeta(self, item, row, column):
        if item is None: return
        
        setattr(item, "row", row)
        setattr(item, "column", column)
    
    def remove(self, ranges=None):
        if ranges is None: ranges = self._getRanges(True)
         
        for (start, end) in ranges:
            if start == end: 
                self.removeRow(start)
                continue

            numRows = abs(end - start) + 1
            while numRows != 0:
                self.removeRow(start)
                numRows -= 1
             
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._updateItemMeta(self.cellWidget(row, column), row, column)
                
        self.SigselectionRemoved.emit(ranges)
    
    def setRowBackground(self, row, color):
        for i in range(self.columnCount()):
            item = self.item(row, i)
            if item is not None:
                item.setBackground(color)
            else:
                self.cellWidget(row, i).setStyleSheet("QWidget{background-color:%s}" % (color.name()))
    
    def rowBackground(self, row):
        item = self.item(row, 0)
        color = item.background().color().name()
        if color == "#000000": return None
        return color
                
    def _moveRange(self, ranges, byRows):
        selectRows = []
        
        for (start, end) in ranges:

            if byRows < 0: 
                (start, end) = (end, start)
                step = -1
                end -= 1
            else: 
                step = 1
                end += 1
            
            for row in range(start, end, step):
                newRow = self.moveRelative(row, byRows)
                if newRow is False: return
                else: selectRows.append(newRow)
        
        sm = self.selectionModel()
        itemSelection = sm.selection()
        
        for row in selectRows:
            if row is None: continue
            self.selectRow(row)
            itemSelection.merge(sm.selection(), QItemSelectionModel.Select)
            
        sm.clearSelection()
        sm.select(itemSelection, QItemSelectionModel.Select)
        
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._updateItemMeta(self.cellWidget(row, column), row, column)
        
    def _getRanges(self, reverseOrder=False):
        order = []
        ranges = self.selectedRanges()
        
        for rowRange in ranges:
            start = rowRange.bottomRow()
            end = rowRange.topRow()
            order.append((start, end))
        
        order = [sorted(tup) for tup in order]
        order = sorted(order, key=lambda tup: tup[1])
        if reverseOrder == True: order.reverse()
        return order
    
    def selectRanges(self, ranges):
        sm = self.selectionModel()
        itemSelection = sm.selection()
        for r in ranges:
            for row in r:
                self.selectRow(row)
                itemSelection.merge(sm.selection(), QItemSelectionModel.Select)
        sm.clearSelection()
        sm.select(itemSelection, QItemSelectionModel.Select)
        
    @staticmethod
    def _columnwidget(childWidget):
        widget = QWidget()
        widget.setStyleSheet("QWidget{background-color:transparent}")
        layout = QHBoxLayout(widget)
        layout.addWidget(childWidget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        setattr(widget, "row", None)
        setattr(widget, "column", None)
        return widget
