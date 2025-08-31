from Models.AttributeModel import AttributeModel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

class EdgeModel(QWidget):
    #############################################
    # Signal Definitions
    #############################################
    metrics_changed = pyqtSignal(AttributeModel)
    
    #############################################
    # Property Definitions
    #############################################   
    @property
    def metrics_f2s(self):
        return self._metrics_f2s
    
    @metrics_f2s.setter
    def metrics_f2s(self, value):
        self._metrics_f2s = value
        self.metricModel.loadData(self.getMetrics())
        self.metrics_changed.emit(self.metricModel)
    
    @property
    def metrics_s2f(self):
        return self._metrics_s2f
    
    @metrics_s2f.setter
    def metrics_s2f(self, value):
        self._metrics_s2f = value
        self.metricModel.loadData(self.getMetrics())
        self.metrics_changed.emit(self.metricModel)
    
    def __init__(self, edge, first_index, second_index, 
                             metrics_f2s=None, metrics_s2f=None):
        super().__init__()
        self.metricModel = AttributeModel()
        self.edge = edge
        self.first_index = first_index
        self.second_index = second_index
        self.metrics_f2s = metrics_f2s
        self.metrics_s2f = metrics_s2f
    
    def __str__(self) -> str:
        return "Edge: " + str(self.first_index) + " -> " + str(self.second_index)
    
    def isSameEdge(self, first_index, second_index):
        return (self.first_index == first_index and self.second_index == second_index) or \
               (self.first_index == second_index and self.second_index == first_index)
               
    def addMetrics(self, first_index, second_index, metrics):
        if first_index == self.first_index and second_index == self.second_index:
            self.metrics_f2s = metrics
        elif first_index == self.second_index and second_index == self.first_index:
            self.metrics_s2f = metrics
        else:
            print("Error: EdgeModel.addMetrics: The edge does not exist.")
            
    def getMetrics(self):
        edgeInfo = dict()
        edgeInfo["Node One"] = self.first_index
        edgeInfo["Node Two"] = self.second_index
        dictionary = dict()
        dictionary["Edge"] = edgeInfo
        # Dependency on the order of the metrics instantiation
        if hasattr(self, "metrics_f2s") and self.metrics_f2s != None:
            dictionary["From One to Two"] = self.metrics_f2s
        if hasattr(self, "metrics_s2f") and self.metrics_s2f != None:
            dictionary["From Two to One"] = self.metrics_s2f
        return dictionary
    
        