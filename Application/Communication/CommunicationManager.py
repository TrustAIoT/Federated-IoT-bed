from uuid import getnode as get_mac
from typing import List
import logging
import time

import paho.mqtt.client as mqtt

from Communication.Observer import Observer
from Communication.Message import Message


class CommunicationManager():
    def __init__(self, broker, port, 
                 username, password, 
                 client_id=0, 
                 client_num=0):
        # List Unacknowledged subscriptions
        self._unacked_sub = list()
        
        self._observers: List[Observer] = []
        self._client_id = client_id
        self.client_num = client_num
        # Construct a Client
        self._client = mqtt.Client(client_id=str(self._client_id))
        self._client.username_pw_set(username, password)
        self._client.on_connect = self._on_connect
        self._client.on_disconnect = self._on_disconnect
        self._client.on_message = self._on_message
        self._client.on_subscribe = self._on_subscribe
        # Connect to the broker
        self._client.connect(broker, port, 60)
        self._client.loop_start()

    def __del__(self):
        self._client.loop_stop()
        self._client.disconnect()

    @property
    def client_id(self):
        return self._client_id

    @property
    def topic(self):
        return self._topic

    def _on_connect(self, client, userdata, flags, rc):
        """
            [server]
            sending message topic (publish): serverID_clientID
            receiving message topic (subscribe): clientID

            [client]
            sending message topic (publish): clientID
            receiving message topic (subscribe): serverID_clientID

        """
        print("Connection returned with result code:" + str(rc))
        # Subsribe to a topic for all
        topic = self.topic + "/all"
        self.subscribe(topic)
            
        # Subsribe to a topic for server-client
        if self.client_id == 0:
            # server
            for client_ID in range(1, self.client_num+1):
                topic = self._topic + "/" + str(client_ID)
                self.subscribe(topic)
        else:
            # client
            topic = self._topic + "/" + str(0) + "/" + str(self.client_id)
            self.subscribe(topic)

    def subscribe(self, topic):
        result, mid = self._client.subscribe(topic, 0)
        self._unacked_sub.append(mid)
        status = "success" if result == mqtt.MQTT_ERR_SUCCESS else "failed"
        logging.info("%s subscribe to %s: %s" % (self.client_id, topic, status))
    
    def _on_message(self, client, userdata, msg):
        print(client, userdata)
        msg.payload = str(msg.payload, encoding='utf-8')
        # print("_on_message: " + str(msg.payload))
        self._notify(msg)

    @staticmethod
    def _on_disconnect(client, userdata, rc):
        print("Disconnection returned result:" + str(rc))

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        # print("onSubscribe :" + str(mid))
        self._unacked_sub.remove(mid)

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def _notify(self, msg):
        for observer in self._observers:
            observer.receive_message(msg.topic, msg.payload)

    def send_message(self, msg: Message):
        """
            [server]
            sending message topic (publish): serverID_clientID
            receiving message topic (subscribe): clientID

            [client]
            sending message topic (publish): clientID
            receiving message topic (subscribe): serverID_clientID

        """
        if self.client_id == 0:
            # server
            receiver_id = msg.get_receiver_id()
            topic = self._topic + "/" + str(0) + "/" + str(receiver_id)
            logging.info("sending message to %s" % str(topic))
            payload = msg.to_json()
            self._client.publish(topic, payload=payload)
            logging.info("sent")
        else:
            # client
            self._client.publish(self._topic + str(self.client_id), payload=msg.to_json())

    def send_message_to_all(self, msg: Message):
        self._client.publish(self._topic + "/all", payload=msg.to_json())
    
    def handle_receive_message(self):
        pass

    def stop_receive_message(self):
        pass