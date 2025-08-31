from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


class AttributeModel(QStandardItemModel):
    def __init__(self, headers = ("Attribute", "Value"), data=None, parent=None):
        super().__init__(parent)
        self.headers = headers
        self.data = data
        
    def loadData(self, data):
        self.data = data
        self.clear()
        self.setHorizontalHeaderLabels(self.headers)
        self.load()
        
    def load(self):
        if self.data == None:
            return
        
        for headings in self.data:
            parent = QStandardItem(headings)
            parent.setFlags(Qt.NoItemFlags)
            for dictionary in self.data[headings]:
                value = self.data[headings][dictionary]
                # The key is uneditable
                child0 = QStandardItem(dictionary)
                child0.setFlags(Qt.NoItemFlags |
                                Qt.ItemIsEnabled)
                # The value is editable
                child1 = QStandardItem(str(value))
                child1.setFlags(Qt.ItemIsEnabled |
                                Qt.ItemIsEditable |
                                ~ Qt.ItemIsSelectable)
                parent.appendRow([child0, child1])
            self.appendRow(parent)
            
    def getDict(self):
        dictionary = dict()
        for tableIndex in range(self.rowCount()):
            headingIndex = self.index(tableIndex, 0)
            dictionary[headingIndex.data()] = {}
            for headingRowIndex in range(self.rowCount(headingIndex)):
                attributeIndex = self.index(headingRowIndex, 0, headingIndex)
                valueIndex = self.index(headingRowIndex, 1, headingIndex)
                dictionary[headingIndex.data()][attributeIndex.data()] = valueIndex.data()
        return dictionary