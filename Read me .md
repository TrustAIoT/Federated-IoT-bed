# Development and Validation of A Heterogeneous Wireless Mesh IoT Testbed with Distributed Machine Learning

## About the Project 

The development of IoT devices has led to increased interests in distributed machine learning on edge devices for many researchers. However, a multitude of current distributed machine learning research is validated mainly by simulation alone. To fill the reality gap, testbeds are developed for physical deployments of these machine learning models. In this report, we present our current implementation of a wireless mesh IoT testbed consisting of the following heterogeneous devices: Raspberry Pi 4 Model B, Jetson Nano, and Jetson Orin Nano. Our wireless mesh testbed is connected through a mesh ad-hoc network, where packets are routed using the popular routing protocol, B.A.T.M.A.N IV. To validate the setup of our testbed and the multi-hop capabilities of B.A.T.M.A.N IV, we query a variety of network metrics in single-hop and multi-hop scenarios. In addition, we perform an experiment on federated learning across our testbed, in which we utilize the popular FedAVG aggregation server to train a Resnet 18 model for image classification using the Cifar10 dataset. We analyze the result of our experiment across heterogeneous devices to discover potential problems in the naive assumption of homogeneity across clients. In particular, physical deployment of models on IoT devices significantly enlarges the training time, and with the need to communicate across distance, enlarges communication time. We thus recommend some research directions to solve the problems, in which our testbed can provide assistance in physical deployment.

With the popularity of Internet of Things (IoT) devices in the market, researchers increased their attention leveraging the mass computational power available from the massive pool of IoT devices [1]. Distributed Machine Learning (DML) research has been accelerated during the current century, of which various models and techniques investigate different aspects like architecture, communication, protocols, applications, security and privacy. However, the performance evaluation and deployments of these models often utilized simulation techniques. These simulation tools are capable of simulating various delays and network conditions across devices, but various nuances of communication between devices are still missing from various simulation models. In addition, much machine learning research assumes homogeneity across various conditions such as statistical homogeneity in data and models, and system homogeneity in devices. To fill the reality gap, testbeds are developed for physical deployments of these machine learning models.

## Network Topology 

In this network,
some devices or nodes are connected to two or more nodes with a point-to-point link, but not all
devices are connected. This gives us the benefit of redundancy in some of our connections
without the required quadratic growth of connections that make large fully connected mesh
networks impractical. The redundancy of our network was an important consideration when
designing our wireless edge IoT testbed. We needed our testbed to be able to continue
distributed training even when one of our workers or client’s communications drops out to
properly assess deployment of distributed models. In real-world application of distributed
models, there often is no guaranteed strong connection between devices such as ethernet, but
rather wireless communication that is susceptible to dropping out due to elements such as
interference or even weather. Therefore, we have decided to use a mesh network to add both
extra redundancy and reliability to our connected devices as shown below in figure 1.

![image.png](https://private-user-images.githubusercontent.com/81721268/340063582-7683d920-fa38-4aed-8787-7d9a35087029.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MTA0NjQsIm5iZiI6MTcxODUxMDE2NCwicGF0aCI6Ii84MTcyMTI2OC8zNDAwNjM1ODItNzY4M2Q5MjAtZmEzOC00YWVkLTg3ODctN2Q5YTM1MDg3MDI5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjE2VDAzNTYwNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFlNzZkNWZlMWNhNDMwYmE2OGNlNGE3Y2EzNDE0OWY0MDExN2Q2OGU1N2FiYTZkODBlNGY3YjFiN2I3MDNmNjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.O5jlUyHAFW-_CdtQX_3GfHn6BzN9p0SgJsvGhxEeDnA)

## Project Directory Structure 
project-root/
├── docs/
│   ├── architecture.md
│   ├── installation.md
│   └── usage.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.yaml
│   ├── data/
│   │   ├── __init__.py
│   │   └── load_data.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── model.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helper_functions.py
│   └── tests/
│       ├── __init__.py
│       └── test_main.py
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
└── LICENSE

## Hardware Devices 

![Jetson%20Nano.jpg](https://private-user-images.githubusercontent.com/81721268/340063850-e1608d7b-af39-4e76-b229-ed209f77a235.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MTEwNjgsIm5iZiI6MTcxODUxMDc2OCwicGF0aCI6Ii84MTcyMTI2OC8zNDAwNjM4NTAtZTE2MDhkN2ItYWYzOS00ZTc2LWIyMjktZWQyMDlmNzdhMjM1LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjE2VDA0MDYwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNmNjIzYTA5YmFlZWYxNDdlZGM5NDZlYTE4YTI1NTMyMmUxYWYzMTgzM2NlNTNiM2NlZTU2ZTA1YjRmNzE1ZGImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.S3VjyckXDUb_GyaJv45O5NxaIvMxao1pghsHfrcvRRA)

## Setting up the FEDML 

FedML plays a crucial role in our project by providing a structured and efficient framework for implementing federated learning across distributed edge devices, such as the Jetson Nano Development/Expansion Kits. The use of FedML brings several key advantages and functionalities that are essential for the success of our distributed machine learning project. In summary, FedML is integral to our project as it provides the necessary tools and infrastructure to implement federated learning across distributed edge devices. Its capabilities in data privacy, scalability, cost efficiency, real-time processing, and flexibility make it an indispensable component for achieving our project goals effectively and efficiently. By leveraging FedML, we can harness the power of edge computing with the Jetson Nano kits to build a robust and scalable distributed machine learning system.

### 1 Clone the FedML Repository:
git clone https://github.com/FedML-AI/FedML.git
cd FedML

### 2 Install Dependencies:
pip install -r requirements.txt

### 3 Build MLOps Package
cd benchmark
sh build_mlops_pkg.sh

## An Overview of setting up FEDML and review architecture

https://doc.fedml.ai/federate/getting_started

## B.A.T.M.A.N. Advanced (batman-adv) Setup Guide

### 1 Overview of B.A.T.M.A.N Advanced 

B.A.T.M.A.N. Advanced (batman-adv) is a routing protocol designed for multi-hop ad hoc networks. This guide will walk you through the installation of batman-adv along with its associated tools, batctl and alfred. We will also explain the directory structure and how to use these tools to set up and manage your mesh network. batman-adv operates at layer 2, allowing for seamless data transmission across multiple nodes in a mesh network. This setup will help you get batman-adv up and running on your devices, enabling efficient routing and data sharing across your network.

### 2 Prerequisites

Ensure you have a Linux-based system.

Basic knowledge of terminal commands.

wget and pip3 installed on your system

### 3 Installation Steps 

The installation script performs the following tasks:

Installs wget if not already present.

Downloads the latest stable versions of batman-adv, batctl, and alfred.

Extracts the downloaded tar files.

Builds and installs batman-adv, batctl, and alfred.

https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/blob/main/BATMAN%20.md

## Running the Main Application

### 1 Run the Application Script
cd project-root/application/
python App.py

### 2 Monitoring and Logging

rack Metrics Using Weights and Biases
Ensure you have set up Weights and Biases (Wandb) for logging.
Logs and metrics will be stored in the project-root/benchmark/wandb/ directory.

### 3 Trubleshooting 

Ensure all devices are properly connected and can communicate with each other.

Check the logs in the wandb directory for any errors or issues during execution.

Refer to the documentation in fedml/README.md and other relevant README.md files for additional guidance and troubleshooting tips.


```python

```
