from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from QGraphViz.QGraphViz import QGraphVizManipulationMode

from Processes.NetworkQuery import NetworkQuery
from Utility.GraphParser import GraphParser

class NetworkController(QObject):
    def __init__(self, model):
        super().__init__()
        self.model = model
        def node_selected(node):
            self.model.selectNode(node)
    
        def edge_selected(edge):
            self.model.selectEdge(edge)
    
        def node_invoked(node):
            print("Node Double Clicked: " + node.name)
    
        def edge_invoked(edge):
            print("Edge Double Clicked: " + str(edge))
            
        self.model.graph.core.node_selected_callback = node_selected
        self.model.graph.core.edge_selected_callback = edge_selected
        self.model.graph.core.node_invoked_callback = node_invoked
        self.model.graph.core.edge_invoked_callback = edge_invoked
        
        self.model.graph.manipulation_mode = QGraphVizManipulationMode.Nodes_Move_Mode
        
        self.networkQuery = NetworkQuery()
        self.networkQuery.batadv_vis_query_finished.connect(self.generateGraphFromQuery)
        self.networkQuery.start_batadv_vis_query(interval_ms=2000)
    
    @pyqtSlot(str)
    def generateGraphFromQuery(self, query):
        GraphParser.parse_batadv_vis_jsondoc_with_string(self.model, query)
        self.model.build()
    
    @pyqtSlot(str)
    def generateGraphFromFile(self, filename):
        GraphParser.parse_batadv_vis_jsondoc_with_file(self.model, filename)
        self.model.build()
    
    