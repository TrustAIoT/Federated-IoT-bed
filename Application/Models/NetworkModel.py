from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget
from QGraphViz.QGraphViz import QGraphViz 
from QGraphViz.DotParser import Graph
from QGraphViz.Engines import Dot

from Models.NodeModel import NodeModel
from Models.EdgeModel import EdgeModel

class NetworkModel(QWidget):
    #############################################
    # Signal Definitions
    #############################################
    node_added = pyqtSignal(NodeModel)
    node_removed = pyqtSignal(NodeModel)
    edge_added = pyqtSignal(EdgeModel)
    edge_removed = pyqtSignal(EdgeModel)
    graph_built = pyqtSignal(bool)
    node_selected = pyqtSignal(NodeModel)
    edge_selected = pyqtSignal(EdgeModel)
    
    
    def __init__(self):
        super().__init__()
        self.graph = QGraphViz(hilight_Nodes=True, 
                               hilight_Edges=True, 
                               auto_freeze=True,
                               min_cursor_edge_dist=5)
        # Create A new Graph using Dot layout engine
        self.graph.new(Dot(Graph("Main_Graph"), show_subgraphs=True, font = QFont("Arial", 12),margins=[20,20]))
        # Contain NodeModel
        self.nodes = []
        # Contain EdgeModel
        self.adjacencyList = []
        # Contain current selected node
        self.selectedNode = None
        self.selectedEdge = None
        self.oldSelectedEdge = None
    
    def checkNodeExist(self, name):
        return any(nodeModel.node.name == name for nodeModel in self.nodes)
    
    def addNode(self, name=None, label=None, shape = None, fillcolor="orange", color="black"):
        if self.checkNodeExist(name):
            return
        if name == None:
            name = "Node" + str(len(self.nodes))
        if label == None:
            label = str(len(self.nodes))
        if shape == None:
            node = self.graph.addNode(self.graph.engine.graph, name, label=label, fillcolor=fillcolor, color=color)
        else:
            node = self.graph.addNode(self.graph.engine.graph, name, label=label, shape=shape, fillcolor=fillcolor, color=color)
        
        added_node = NodeModel(node)
        self.nodes.append(added_node)
        self.adjacencyList.append([])
        
        self.node_added.emit(added_node)
        self.node_selected.emit(added_node)
    
    def checkEdgeExist(self, source_index, target_index):   
        return any(edgeModel.isSameEdge(source_index, target_index) for edgeModel in self.adjacencyList[source_index])
    
    def addEdgeByName(self, source_name, target_name, paintParameter={}, metrics=None):
        source_index = next(index for index, nodeModel in enumerate(self.nodes) if nodeModel.node.name == source_name)
        target_index = next(index for index, nodeModel in enumerate(self.nodes) if nodeModel.node.name == target_name)
        self.addEdgeByIndex(source_index, target_index, paintParameter, metrics)
    
    def addEdgeByIndex(self, source_index, target_index, paintParameter={}, metrics=None):
        if self.checkEdgeExist(source_index, target_index):
            added_edge = next(edgeModel for edgeModel in self.adjacencyList[source_index] 
                              if edgeModel.isSameEdge(source_index, target_index))
            added_edge.addMetrics(source_index, target_index, metrics)
        else:
            edge = self.graph.addEdge(self.nodes[source_index].node, self.nodes[target_index].node, paintParameter)
            added_edge = EdgeModel(edge, source_index, target_index)
            added_edge.addMetrics(source_index, target_index, metrics)
            self.adjacencyList[source_index].append(added_edge)
            self.adjacencyList[target_index].append(added_edge)
        self.edge_added.emit(added_edge) 
        
    def selectNode(self, node):
        self.selectedNode = next(nodeModel for nodeModel in self.nodes if nodeModel.node == node)
        print("Node Selected: " + str(self.selectedNode))
        self.node_selected.emit(self.selectedNode)
    
    def selectEdge(self, edge):
        self.oldSelectedEdge = self.selectedEdge
        self.selectedEdge = self.getEdgeModel(edge)
        print("Edge Selected: " + str(self.selectedEdge))
        self.edge_selected.emit(self.selectedEdge)
    
    def getEdgeModel(self, edge):
        source_index = next(index for index, nodeModel in enumerate(self.nodes) if nodeModel.node.name == edge.source.name)
        target_index = next(index for index, nodeModel in enumerate(self.nodes) if nodeModel.node.name == edge.dest.name)
        return next(edgeModel for edgeModel in self.adjacencyList[source_index]
                    if edgeModel.isSameEdge(source_index, target_index))
    
    def build(self):
        self.graph.build()
        self.graph_built.emit(True)     