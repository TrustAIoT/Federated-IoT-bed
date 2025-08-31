from Communication.CommunicationManager import CommunicationManager
from Communication.Observer import Observer
from Communication.Message import Message

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from uuid import getnode as get_mac

class GatewayController(QObject):
    class GatewayObserver(Observer):
        def receive_message(self, msg_type, msg_params):
            pass
              
    def __init__(self, networkModel):
        super().__init__()
        self.networkModel = networkModel
        self.client = CommunicationManager(broker="192.168.123.1", port=1883, topic="status",
                                           username="jetson", password="jetson", 
                                           client_id=0)
        self.gatewayObserver = self.GatewayObserver()
        self.client.add_observer(self.gatewayObserver)
        
        self.networkModel.node_added.connect(self.onNodeAdded)
        self.networkModel.node_removed.connect(self.onNodeRemoved)
        
    def onNodeAdded(self, node):
        if node.name != get_mac():
            pass      
        self.updateMACList()

    def onNodeRemoved(self, node):
        self.updateMACList()
    
    def getMACDict(self):
        listOfMACs = [node.name for node in self.networkModel.nodes]
        try:
            listOfMACs.remove(get_mac())
        except ValueError:
            pass
        
        msg = Message(type=0, sender_id=self.client.client_id, receiver_id=None)
        msg.add_params("MAC", listOfNames)
        self.client.send_message_to_all(msg)
        
        
        
    
    
        