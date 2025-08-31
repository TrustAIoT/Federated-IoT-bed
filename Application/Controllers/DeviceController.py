from Communication.CommunicationManager import CommunicationManager
from Communication.Observer import Observer
from Communication.Message import Message

class DeviceController(object):
    def __init__(self, host = "192.168.123.1", port = 1883, topic = "status", username = "jetson", password = "jetson", client_id = 0):
        super().__init__()
        self.client = CommunicationManager(broker = host, port = port, topic = topic, 
                                           username = username, password = password, 
                                           client_id = client_id)