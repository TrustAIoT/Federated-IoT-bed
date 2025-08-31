from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def receive_message(self, msg_topic, msg_payload) -> None:
        pass