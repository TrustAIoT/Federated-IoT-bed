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

![image.png](attachment:image.png)

## Project Directory Structure 
project-root/
├── application/
│   ├── Communication/
│   ├── Controllers/
│   ├── Examples/
│   ├── Models/
│   ├── Processes/
│   ├── Utility/
│   ├── Views/
│   ├── App.py
│   ├── Untitled.ipynb
│   └── ...
├── benchmark/
│   ├── config/
│   ├── data/
│   ├── trainer/
│   ├── wandb/
│   ├── __init__.py
│   ├── build_mlops_pkg.sh
│   ├── run_client.sh
│   ├── run_server.sh
│   ├── testing.py
│   ├── torch_client.py
│   ├── torch_server.py
│   └── ...
├── fedml/
│   ├── applications/
│   ├── benchmark/
│   ├── build-mlops-package/
│   ├── data/
│   ├── docs/
│   ├── fedml_api/
│   ├── fedml_core/
│   ├── fedml_experiments/
│   ├── fedml_iot/
│   ├── fedml_mobile/
│   ├── fedml_server/
│   ├── scripts/
│   ├── __init__.py
│   ├── async_fedml_source_code.sh
│   ├── CI-install.sh
│   ├── CI-script-fedavg-robust.sh
│   ├── CI-script-fedavg.sh
│   ├── CI-script-fednas.sh
│   ├── CI-script-framework.sh
│   ├── contributor.md
│   ├── INSTALL.md
│   ├── LICENSE
│   ├── publications.md
│   ├── README.md
│   └── ...
├── system_based_client_selection/
│   ├── config/
│   ├── data/
│   ├── model/
│   ├── trainer/
│   ├── wandb/
│   ├── main_fedml_system_selection.py
│   ├── run_client.sh
│   ├── run_server.sh
│   ├── run_simulation.sh
│   └── ...
├── batmanInstall.sh
├── nanoInstall.sh
├── piInstall.sh
├── pirequirements.txt
├── readme.md
├── test.gv
└── untitled.txt
## Hardware Devices 

![Jetson%20Nano.jpg](attachment:Jetson%20Nano.jpg)

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

http://localhost:8888/notebooks/Untitled2.ipynb?kernel_name=python3

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
