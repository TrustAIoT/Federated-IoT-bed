import os
import yaml
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from Models.AttributeModel import AttributeModel

from enum import Enum

class NodeModel(QWidget):
    #############################################
    # Signal Definitions
    #############################################
    attributes_loaded = pyqtSignal(AttributeModel)
    type_changed = pyqtSignal(str)
    source_path_changed = pyqtSignal(str)
    entry_path_changed = pyqtSignal(str)
    
    #############################################
    # Property Definitions
    #############################################
    @property
    def type(self):
        return self._type
        
    @type.setter
    def type(self, value):
        self._type = value
        self.type_changed.emit(value)
        
    @property
    def source_path(self):
        return self._source_path
    
    @source_path.setter
    def source_path(self, value):
        self._source_path = value
        self.source_path_changed.emit(value)
        
    @property
    def entry_path(self):
        return self._entry_path
    
    @entry_path.setter
    def entry_path(self, value):
        self._entry_path = value
        self.entry_path_changed.emit(value)
        
    @property
    def config_path(self):
        return self._config_path
    
    @config_path.setter
    def config_path(self, value):
        self._config_path = value
        self.loadAttributes(self._config_path)
        self.attributes_loaded.emit(self.attributeModel)
    
    def __init__(self, node=None, _type="Deactivated", _source_path=None, _entry_path=None, _config_path=None):
        super().__init__()
        self.attributeModel = AttributeModel()
        self.node = node
        self._type = _type
        self._source_path = _source_path
        self._entry_path = _entry_path
        self._config_path = _config_path
    
    def __str__(self) -> str:
        return "Node: " + str(self.node.name) + "|" + \
               " Type: " + str(self.type) + "|" + \
               " Source: " + str(self.source_path) + "|" + \
               " Entry: " + str(self.entry_path) + "|" + \
               " Config: " + str(self.config_path)
     
    def loadAttributes(self, config_path):
        # Renew the content of attributeModel
        if config_path == None or config_path == "":
            self.attributeModel.clear()
            return
        # Move to current directory
        file_path = os.path.dirname(__file__)
        if file_path != "":
            os.chdir(file_path)
            os.chdir("..")
        # Reading from yaml file
        # print("Loading attributes from " + os.getcwd() + "/" + config_path)
        with open(config_path, 'r') as stream:
            self.attributeModel.loadData(yaml.safe_load(stream))

            
    
        
    
    