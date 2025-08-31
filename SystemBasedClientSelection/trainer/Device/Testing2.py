import logging
import time
from SystemInfoCommunicator import SystemInfoCommunication
from DeviceInfo import DeviceInfo
import psutil
import json
    
class Testing:
    def __init__(self):
        self.communicator_startup = SystemInfoCommunication("192.168.123.1", 1883, 
                                                    "jetson", "jetson",
                                                    1, 1,
                                                    topic="startup", 
                                                    _on_message_callback=self.message_callback_startup)
        self.communicator_stats = SystemInfoCommunication("192.168.123.1", 1883, 
                                                    "jetson", "jetson",
                                                    1, 1,
                                                    topic="stats", 
                                                    _on_message_callback=self.message_callback_stats)
        time.sleep(1)
        self.communicator_startup.send_message({"MAC_Address" : self.get_mac_address()})
        self.destination_MAC = None
        time.sleep(1000)
        
    def message_callback_startup(self, topic, payload):
        print("Received the topic: {}, message: {}.".format(topic, payload))
        if self.destination_MAC == None:
            self.communicator_startup.send_message({"MAC_Address" : self.get_mac_address()})
            payload = json.loads(payload)
            self.destination_MAC = payload["MAC_Address"]
            self.deviceQuery = DeviceInfo(self.destination_MAC, self.comp_callback, self.network_callback)
    def message_callback_stats(self, topic, payload):
        print("Received the topic: {}, message: {}.".format(topic, payload))
    def comp_callback(self, message):
        self.communicator_stats.send_message(message)
    def network_callback(self, message):
        self.communicator_stats.send_message(message)
    def get_mac_address(self):
        return psutil.net_if_addrs()['wlan0'][1].address

if __name__ == "__main__":
    testing = Testing()
    
    time.sleep(1000)
    
