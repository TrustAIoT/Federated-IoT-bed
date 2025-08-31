import logging
from collections import OrderedDict
from typing import List, Tuple, Dict

import torch
from torch import nn

import numpy as np

from fedml.core import ServerAggregator
from fedml.ml.aggregator.agg_operator import FedMLAggOperator
import fedml

from .Device.SystemInfoCommunicator import SystemInfoCommunication

import psutil
import json


class SystemAwareAggregator(ServerAggregator):
    def __init__(self, model, args):
        super().__init__(model, args)
        self.cpu_transfer = False if not hasattr(self.args, "cpu_transfer") else self.args.cpu_transfer
        self.clientStats = {}
        self.client_real_ids = json.loads(self.args.client_id_list)
        if self.args.rank == 0:
            self._init_device_query()

    def _init_device_query(self):
        self.communicator_stats = SystemInfoCommunication(self.args.mqtt_broker, 1883,
                                                    self.args.broker_username, self.args.broker_password,
                                                    self.args.rank, self.client_real_ids,
                                                    topic="stats",
                                                    _on_message_callback=self.message_callback_stats)

    def message_callback_stats(self, topic, payload):
        client_id = topic.split("/")[-1]
        if client_id not in self.clientStats:
            self.clientStats[client_id] = {}
        self.clientStats[client_id].update(json.loads(payload))
        fedml.logging.info("Current stats of client: {}, message: {}.".format(client_id, str(self.clientStats[client_id])))
    
    def get_model_params(self):
        if self.cpu_transfer:
            return self.model.cpu().state_dict()
        return self.model.state_dict()

    def set_model_params(self, model_parameters):
        self.model.load_state_dict(model_parameters)

    def on_before_aggregation(
        self, raw_client_model_or_grad_list: List[Tuple[float, OrderedDict]]
    ):
        #fedml.logging.info("\n\n\ndo decoding here for raw_client_model_or_grad_list\n\n\n")
        client_idxs = [i for i in range(len(raw_client_model_or_grad_list))]
        return raw_client_model_or_grad_list, client_idxs

    def aggregate(self, raw_client_model_or_grad_list: List[Tuple[float, OrderedDict]]):
        #fedml.logging.info("\n\n\ndo aggregation here for raw_client_model_or_grad_list\n\n\n")
        return FedMLAggOperator.agg(self.args, raw_client_model_or_grad_list)

    def client_selection(self, round_idx, client_id_list_in_total, client_num_per_round):
        """
        Args:
            round_idx: round index, starting from 0
            client_id_list_in_total: this is the real edge IDs.
                                    In MLOps, its element is real edge ID, e.g., [64, 65, 66, 67];
                                    in simulated mode, its element is client index starting from 1, e.g., [1, 2, 3, 4]
            client_num_per_round:

        Returns:
            client_id_list_in_this_round: sampled real edge ID list, e.g., [64, 66]
        """
        fedml.logging.info("do client_selection here")
        for client_id in client_id_list_in_total:
            if client_id in self.clientStats:
                fedml.logging.info("Client " + str(self.clientStats[client_id]))
        if client_num_per_round == len(client_id_list_in_total):
            return client_id_list_in_total
        np.random.seed(round_idx)  # make sure for each comparison, we are selecting the same clients each round
        client_id_list_in_this_round = np.random.choice(client_id_list_in_total, client_num_per_round, replace=False)
        return client_id_list_in_this_round

    def test(self, test_data, device, args):
        model = self.model

        model.to(device)
        model.eval()

        metrics = {
            "test_correct": 0,
            "test_loss": 0,
            "test_precision": 0,
            "test_recall": 0,
            "test_total": 0,
        }

        criterion = nn.CrossEntropyLoss().to(device)

        with torch.no_grad():
            for batch_idx, (x, target) in enumerate(test_data):
                x = x.to(device)
                target = target.to(device)
                pred = model(x)
                loss = criterion(pred, target)

                
                _, predicted = torch.max(pred, 1)
                correct = predicted.eq(target).sum()

                metrics["test_correct"] += correct.item()
                metrics["test_loss"] += loss.item() * target.size(0)
                if len(target.size()) == 1:  #
                    metrics["test_total"] += target.size(0)
                elif len(target.size()) == 2:  # for tasks of next word prediction
                    metrics["test_total"] += target.size(0) * target.size(1)
        return metrics
    
    
