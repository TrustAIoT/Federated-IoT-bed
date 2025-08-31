import json
import os

from QGraphViz.QGraphViz import QGraphViz
from Utility.Math import Math

class GraphParser:    
    @staticmethod
    def parse_batadv_vis_jsondoc(networkModel, json_dict):
        nodes = json_dict["vis"]
        for node in nodes:
            primary_MAC = node["primary"]
            neighbors = node["neighbors"]
            for neighbor in neighbors:
                neighbor_MAC = neighbor["neighbor"]
                metric = float(neighbor["metric"])
                if networkModel.checkNodeExist(primary_MAC) == False:
                    networkModel.addNode(name=primary_MAC, shape="box", fillcolor="orange")
                if networkModel.checkNodeExist(neighbor_MAC) == False:
                    networkModel.addNode(name=neighbor_MAC, shape="box", fillcolor="orange")
                networkModel.addEdgeByName(primary_MAC, 
                                           neighbor_MAC, 
                                           paintParameter= {"width": Math.clampFloatToInt(metric, 1.0, 2.0, 3, 10)}, 
                                           metrics={"vis-metric":metric})
        
    @staticmethod
    def parse_batadv_vis_jsondoc_with_string(networkModel, jsonString):
        GraphParser.parse_batadv_vis_jsondoc(networkModel, json.loads(jsonString))
    
    @staticmethod
    def parse_batadv_vis_jsondoc_with_file(networkModel, filename):
        # Move to current directory
        file_path = os.path.dirname(__file__)
        if file_path != "":
            os.chdir(file_path)
            os.chdir("..")
        # Load json file
        with open(filename, 'r') as f:
            GraphParser.parse_batadv_vis_jsondoc(networkModel, json.load(f))