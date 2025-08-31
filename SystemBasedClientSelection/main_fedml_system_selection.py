import os
import sys

#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import fedml
from fedml import FedMLRunner

import logging

from getpass import getpass

from data.data_loader import load_data
from model.model import LogisticRegression
from trainer.SystemAwareAggregator import SystemAwareAggregator
from trainer.SystemAwareTrainer import SystemAwareTrainer

from fedml.model.cv.cnn import Cifar10FLNet

if __name__ == "__main__":
    # init FedML framework
    args = fedml.init()
    args.sudo_password = getpass("Please enter your sudoers password (optional): ")

    fedml.logging.info(args.mqtt_config_path)

    # init device
    device = fedml.device.get_device(args)

    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers:
        logger.setLevel(logging.INFO)

    # load data
    dataset, output_dim = fedml.data.load(args)

    # create model and trainer
    model = Cifar10FLNet()

    #dataset = None

    # create custome trainer and aggregator
    trainer = SystemAwareTrainer(model, args)
    aggregator = SystemAwareAggregator(model, args)
    
    # start training
    fedml_runner = FedMLRunner(args, device, dataset, model, trainer, aggregator)
    fedml_runner.run()
    
