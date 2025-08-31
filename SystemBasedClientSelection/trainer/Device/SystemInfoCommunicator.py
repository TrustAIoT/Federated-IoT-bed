from fedml.core.distributed.communication.mqtt.mqtt_manager import MqttManager
import logging
import json

class SystemInfoCommunication(object):
    def __init__(self, host, port,
                 username, password, 
                 client_id=0, 
                 client_ids=None,
                 topic="stats",
                 _on_message_callback=None):
        self.client_id = client_id
        self.client_ids = client_ids
        self.topic = topic
        self.last_will_topic, self.last_will_msg = self._init_last_will()
        self.on_message_callback = _on_message_callback
        self.mqtt_manager = MqttManager(host, port, username, password,
                               180, self.client_id,
                               last_will_topic=self.last_will_topic,
                               last_will_msg=json.dumps(self.last_will_msg))
        self._init_connect()
        self._init_heartbeat()

    def __del__(self):
        self.mqtt_manager.loop_stop()
        self.mqtt_manager.disconnect()  
    
    def _init_last_will(self):
        last_will_topic = "status/alive/" + str(self.client_id) 
        last_will_msg = {"ID": str(self.client_id), "status": "OFFLINE"}
        return last_will_topic, last_will_msg

    def _init_heartbeat(self):
        heartbeat_msg = {"ID": str(self.client_id), "status": "ONLINE"}
        self.mqtt_manager.send_message(self.last_will_topic, json.dumps(heartbeat_msg))
        
    def _init_connect(self):
        self.mqtt_manager.connect()
        self.mqtt_manager.loop_start()
        # Subsribe to a topic for server-client
        if self.client_id == 0:
            # server
            for client_ID in self.client_ids:
                destination = self.topic + "/" + str(client_ID)
                self.subsribe(destination, self.on_message_callback)
        else:
            # client
            destination = self.topic + "/" + str(0) + "/" + str(self.client_id)
            self.subsribe(destination, self.on_message_callback)
        
    def subsribe(self, topic, callback=None):
        print("Subscribe to " + topic)
        self.mqtt_manager.add_message_listener(topic, callback)
        self.mqtt_manager.subscribe_msg(topic)
    
    def send_message(self, message: dict, receiver_id = "all"):
        if self.client_id == 0:
            if receiver_id == "all":
                # server
                for client_ID in self.client_ids:
                    destination = self.topic + "/" + str(0) + "/" + str(client_ID)
                    #print("Send to " + destination)
                    self.mqtt_manager.send_message(destination, json.dumps(message))
            else:
                # server
                destination = self.topic + "/" + str(0) + "/" + str(receiver_id)
                #print("Send to " + destination)
                self.mqtt_manager.send_message(destination, json.dumps(message))
        else:
            # client
            destination = self.topic + "/" + str(self.client_id)
            #print("Send to " + destination)
            self.mqtt_manager.send_message(destination, json.dumps(message))
