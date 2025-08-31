from PyQt5.QtCore import QObject, pyqtSlot
import random

from Models.NodeModel import NodeModel

class NodeController(QObject):
    def __init__(self, model):
        super().__init__()
        # Contain Network Model
        self.model = model
    
    @pyqtSlot(str)
    def change_config(self, config_path):
        self.model.selectedNode.config_path = config_path
    
    @pyqtSlot(str)
    def change_type(self, type):
        if self.model.selectedNode == None:
            return
        self.model.selectedNode.type = type
    
    @pyqtSlot(str)    
    def change_source_folder(self, type):
        if self.model.selectedNode == None:
            return
        self.model.selectedNode.source_path = type

    @pyqtSlot(str)
    def change_entry_file(self, type):
        if self.model.selectedNode == None:
            return
        self.model.selectedNode.entry_path = type
       
 
        
    
    