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

![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/2c517eea-754e-4754-a9b4-b48b69558782)

## Project Directory Structure 
project-directory/
```plaintext
project-directory/
.
├── BATMAN.ipynb
├── batmanInstall.sh
├── directory_tree.txt
├── nanoInstall.sh
├── piInstall.sh
├── pirequirements.txt
├── Read me.ipynb
├── readme.md
├── test.gv
├── Application
│   ├── App.py
│   ├── Untitled.ipynb
├── Benchmarking
│   ├── build_mlops_pkg.sh
│   ├── run_client.sh
│   ├── run_server.sh
│   ├── testing.py
│   ├── torch_client.py
│   ├── torch_server.py
├── data
│   ├── custom_data_loader.py
│   ├── efficient_loader.py
│   ├── without_reload.py
├── trainer
│   ├── classification_aggregator.py
│   ├── classification_trainer.py
├── wandb
├── FedML-fedml_v0.6_before_fundraising
│   ├── async_fedml_source_code.sh
│   ├── CI-install.sh
├── Jetson-Nano-Projects
│   ├── requirements.txt
│   ├── Projects
│       ├── start-batman-adv-client.sh
│       ├── start-batman-adv.sh
├── Raspberry-Pi-Projects
│   ├── requirements.txt
│   ├── Projects
```
## Hardware Devices 
| Item | Description | Image |
|------|-------------|-------|
| Waveshare Jetson Nano Development/Expansion Kit BO1 (3x) | The Jetson Nano developer boards utilize NVIDIA’s JetPack SDK to provide a full development environment for hardware-accelerated AI edge development. We utilize the Jetson Nanos as clients for gpu-accelerated distributed machine learning. [Link](https://www.amazon.com/dp/B09R4MH39B) | ![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/6ea33e27-aa26-4e1e-a36c-e359b6941534) |
| NVIDIA Jetson Orin Nano Developer Kit (1x) | The Jetson Orin developer board is a more powerful updated Jetson Nano module with up to 80x the performance of NVIDIA Jetson Nano. With the increased performance and 8 GB of RAM, the Jetson Orin Nano Developer Kit helps give our testbed extreme heterogeneity across our training devices. This heterogeneity allows our testbed to better research and evaluate distributed learning issues and research topics such as asynchronous federated learning. For our testbed, we utilize the Jetson Orin to work as gateway devices for our mesh network and similar to Jetson Nano as clients for gpu-accelerated distributed machine learning. [Link](https://www.amazon.com/dp/B09R4MH39B) | ![image.jpg](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/75047b39-7fba-4efc-a49d-b9653e437eb0) |
| Raspberry Pi 4 Model B 2019 Quad Core 64 Bit Wifi Bluetooth (4GB) (3x) | The Raspberry Pi 4 Model B is a tiny desktop computer with performance comparable to entry-level x86 PC systems. The Raspberry Pi 4 Model B both increases the heterogeneity of our testbed’s architecture with its lack of GPUs and serves to easily collect sensor data through its well-documented 40-pin GPIO header. For our testbed, we utilize the Raspberry Pi 4 Model Bs to both collect sensor data and run our distributed learning server through FedML integration. [Link](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X) | ![image.jpg](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/9deace18-9b6f-421d-b61b-620eb0ca0574) |
| Raspberry Pi Pico W with Pre-Soldered Header (3x) | The Raspberry Pi Pico W is a small low-cost high-performance microcontroller board featuring Infineon’s CYW43439 wireless chip for Wi-Fi 4 wireless network control and communication and 26 GPIO pins. For our testbed, we will utilize the Pico W’s GPIO pins for collecting sensor data to train our lab’s models in the future. [Link](https://www.amazon.com/Pico-Raspberry-Pre-Soldered-Dual-core-Processor/dp/B0BK9W4H2Q) | ![image.jpg](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/6a87a545-8ae2-4fcd-9f1c-f93b848cecc9) |
| Panda Wireless PAU0B AC600 Dual Band Wireless USB Adapter (1x) | The Panda Wireless USB adapter allowed us to configure our Jetson Nano module to act as a gateway connecting our testbed’s mesh network to our lab’s router’s internet connection. Any network interface could work for this purpose but we found the Panda Wireless adapter to be extremely easy to set up for our Linux environment compared to other adapters. [Link](https://www.amazon.com/dp/B08NPX2X4Z?tag=bravesoftwa04-20&linkCode=osi&th=1&psc=1&language=en_US) | ![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/af1d75d5-630d-40e9-b443-8efd0da69f66) |
| Sensor Kit | In order to create our own custom datasets for training our lab’s models we have purchased a sensor kit to allow our testbed to collect sensor data. The sensor kit features various sensor collection devices such as: - Temperature sensors - Microphone sound sensors - Vibration switch - Infrared sensor - Obstacle avoidance sensor - Infrared tracking sensor | ![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/5e1726e1-e5d4-43eb-97e0-8d3a6c50dc60) |
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
```
cd project-root/application/
python App.py
```


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
