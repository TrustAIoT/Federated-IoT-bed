# Development and Validation of A Heterogeneous Wireless Mesh IoT Testbed with Distributed Machine Learning

## 1 About the Project 

The development of IoT devices has led to increased interests in distributed machine learning on edge devices for many researchers. However, a multitude of current distributed machine learning research is validated mainly by simulation alone. To fill the reality gap, testbeds are developed for physical deployments of these machine learning models. In this report, we present our current implementation of a wireless mesh IoT testbed consisting of the following heterogeneous devices: Raspberry Pi 4 Model B, Jetson Nano, and Jetson Orin Nano. Our wireless mesh testbed is connected through a mesh ad-hoc network, where packets are routed using the popular routing protocol, B.A.T.M.A.N IV. To validate the setup of our testbed and the multi-hop capabilities of B.A.T.M.A.N IV, we query a variety of network metrics in single-hop and multi-hop scenarios. In addition, we perform an experiment on federated learning across our testbed, in which we utilize the popular FedAVG aggregation server to train a Resnet 18 model for image classification using the Cifar10 dataset. We analyze the result of our experiment across heterogeneous devices to discover potential problems in the naive assumption of homogeneity across clients. In particular, physical deployment of models on IoT devices significantly enlarges the training time, and with the need to communicate across distance, enlarges communication time. We thus recommend some research directions to solve the problems, in which our testbed can provide assistance in physical deployment.

With the popularity of Internet of Things (IoT) devices in the market, researchers increased their attention leveraging the mass computational power available from the massive pool of IoT devices [1]. Distributed Machine Learning (DML) research has been accelerated during the current century, of which various models and techniques investigate different aspects like architecture, communication, protocols, applications, security and privacy. However, the performance evaluation and deployments of these models often utilized simulation techniques. These simulation tools are capable of simulating various delays and network conditions across devices, but various nuances of communication between devices are still missing from various simulation models. In addition, much machine learning research assumes homogeneity across various conditions such as statistical homogeneity in data and models, and system homogeneity in devices. To fill the reality gap, testbeds are developed for physical deployments of these machine learning models.

## 2 Network Topology 

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


## 3 Hardware Devices 
| Item | Description | Image |
|------|-------------|-------|
| Waveshare Jetson Nano Development/Expansion Kit BO1 (3x) | The Jetson Nano developer boards utilize NVIDIA’s JetPack SDK to provide a full development environment for hardware-accelerated AI edge development. We utilize the Jetson Nanos as clients for gpu-accelerated distributed machine learning. [Link](https://www.amazon.com/dp/B09R4MH39B) | ![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/6ea33e27-aa26-4e1e-a36c-e359b6941534) |
| NVIDIA Jetson Orin Nano Developer Kit (1x) | The Jetson Orin developer board is a more powerful updated Jetson Nano module with up to 80x the performance of NVIDIA Jetson Nano. With the increased performance and 8 GB of RAM, the Jetson Orin Nano Developer Kit helps give our testbed extreme heterogeneity across our training devices. This heterogeneity allows our testbed to better research and evaluate distributed learning issues and research topics such as asynchronous federated learning. For our testbed, we utilize the Jetson Orin to work as gateway devices for our mesh network and similar to Jetson Nano as clients for gpu-accelerated distributed machine learning. [Link](https://www.amazon.com/dp/B09R4MH39B) | ![image.jpg](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/75047b39-7fba-4efc-a49d-b9653e437eb0) |
| Raspberry Pi 4 Model B 2019 Quad Core 64 Bit Wifi Bluetooth (4GB) (3x) | The Raspberry Pi 4 Model B is a tiny desktop computer with performance comparable to entry-level x86 PC systems. The Raspberry Pi 4 Model B both increases the heterogeneity of our testbed’s architecture with its lack of GPUs and serves to easily collect sensor data through its well-documented 40-pin GPIO header. For our testbed, we utilize the Raspberry Pi 4 Model Bs to both collect sensor data and run our distributed learning server through FedML integration. [Link](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X) | ![image.jpg](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/9deace18-9b6f-421d-b61b-620eb0ca0574) |
| Raspberry Pi Pico W with Pre-Soldered Header (3x) | The Raspberry Pi Pico W is a small low-cost high-performance microcontroller board featuring Infineon’s CYW43439 wireless chip for Wi-Fi 4 wireless network control and communication and 26 GPIO pins. For our testbed, we will utilize the Pico W’s GPIO pins for collecting sensor data to train our lab’s models in the future. [Link](https://www.amazon.com/Pico-Raspberry-Pre-Soldered-Dual-core-Processor/dp/B0BK9W4H2Q) | ![image.jpg](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/6a87a545-8ae2-4fcd-9f1c-f93b848cecc9) |
| Panda Wireless PAU0B AC600 Dual Band Wireless USB Adapter (1x) | The Panda Wireless USB adapter allowed us to configure our Jetson Nano module to act as a gateway connecting our testbed’s mesh network to our lab’s router’s internet connection. Any network interface could work for this purpose but we found the Panda Wireless adapter to be extremely easy to set up for our Linux environment compared to other adapters. [Link](https://www.amazon.com/dp/B08NPX2X4Z?tag=bravesoftwa04-20&linkCode=osi&th=1&psc=1&language=en_US) | ![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/af1d75d5-630d-40e9-b443-8efd0da69f66) |
| Sensor Kit | In order to create our own custom datasets for training our lab’s models we have purchased a sensor kit to allow our testbed to collect sensor data. The sensor kit features various sensor collection devices such as: - Temperature sensors - Microphone sound sensors - Vibration switch - Infrared sensor - Obstacle avoidance sensor - Infrared tracking sensor | ![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/5e1726e1-e5d4-43eb-97e0-8d3a6c50dc60) |

## 4 B.A.T.M.A.N. Advanced (batman-adv) Setup Guide

### 4.1 Overview of B.A.T.M.A.N Advanced:

B.A.T.M.A.N. Advanced (batman-adv) is a routing protocol designed for multi-hop ad hoc networks. This guide will walk you through the installation of batman-adv along with its associated tools, batctl and alfred. We will also explain the directory structure and how to use these tools to set up and manage your mesh network. batman-adv operates at layer 2, allowing for seamless data transmission across multiple nodes in a mesh network. This setup will help you get batman-adv up and running on your devices, enabling efficient routing and data sharing across your network.

#### Establishing Mesh Network:
BATMAN-adv is used to establish a robust and efficient mesh network among the devices. This enables seamless communication between nodes without relying on a central infrastructure. In a mesh network, each node acts as both a client and a router, forwarding data to other nodes. This decentralized approach ensures that the network remains operational even if some nodes fail or go offline, providing higher resilience and reliability.

#### Enhanced Reliability:
The self-healing and dynamic routing capabilities of BATMAN-adv ensure that the network remains reliable, even in the presence of node failures or changes in topology. The protocol constantly monitors the network and adapts to changes by finding the best possible routes for data packets. This automatic reconfiguration enhances the network's ability to maintain continuous operation, which is crucial for applications requiring high availability and fault tolerance.

#### Improved Network Performance:
By optimizing routes and minimizing latency, BATMAN-adv helps achieve better network performance. The protocol's ability to dynamically select the most efficient paths for data transmission reduces delays and increases throughput. This is particularly important for applications that require real-time data transmission, such as video streaming, online gaming, and remote monitoring. Improved network performance ensures that data is delivered quickly and accurately, enhancing the overall user experience.

#### File Sharing:
Nodes can share files directly over the mesh network without the need for an internet connection. This peer-to-peer communication is facilitated by BATMAN-adv's efficient routing, which ensures that data packets are delivered reliably between nodes. This capability is particularly useful in environments where internet access is limited or unavailable, such as remote locations or disaster-stricken areas.

#### Surveillance Systems:
Cameras and sensors can transmit data efficiently across the network, providing real-time monitoring and security. BATMAN-adv ensures that video feeds and sensor data are routed through the most efficient paths, reducing latency and ensuring timely delivery. This is essential for surveillance systems that require continuous monitoring and immediate response to security events.

#### Emergency Communication:
In disaster scenarios, BATMAN-adv enables quick and reliable setup of communication networks for emergency response teams. The protocol's ability to create ad-hoc networks without relying on existing infrastructure is invaluable in situations where traditional communication systems are compromised. Emergency responders can quickly establish a mesh network to coordinate their efforts, share critical information, and maintain communication in challenging environments.

### 4.2 Update and Upgrade Your System:
```
sudo apt-get update
sudo apt-get upgrade
```
### 4.3 Install Required Packages:
```
sudo apt-get install build-essential git libnl-3-dev libnl-genl-3-dev
```
### 4.4 Clone the BATMAN-Adv Repository:
Navigate to your network-auto-configuration-master/batman/ directory and clone the BATMAN-Adv repository.
```
cd network-auto-configuration-master/batman
```
### 4.5 Build and Install BATMAN-Adv:
```
cd batman-adv
make
sudo make install
```
### 4.6 Load the BATMAN-Adv Kernel Module:
```
sudo modprobe batman-adv
```
### 4.7 Configuring BATMAN-Adv:

https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/blob/main/BATMAN%20.md


## 5 Setting up the FEDML 

FedML plays a crucial role in our project by providing a structured and efficient framework for implementing federated learning across distributed edge devices, such as the Jetson Nano Development/Expansion Kits. The use of FedML brings several key advantages and functionalities that are essential for the success of our distributed machine learning project. In summary, FedML is integral to our project as it provides the necessary tools and infrastructure to implement federated learning across distributed edge devices. Its capabilities in data privacy, scalability, cost efficiency, real-time processing, and flexibility make it an indispensable component for achieving our project goals effectively and efficiently. By leveraging FedML, we can harness the power of edge computing with the Jetson Nano kits to build a robust and scalable distributed machine learning system.

### 5.1 Clone the FedML Repository:
```
git clone https://github.com/FedML-AI/FedML.git
cd FedML
```
### 5.2 Install Dependencies:
```
pip install -r requirements.txt
```

### 5.3 Build MLOps Package:
```
cd benchmark
sh build_mlops_pkg.sh
```
## 6 An Overview of setting up FEDML and review architecture

https://doc.fedml.ai/federate/getting_started


## 7 Running the Main Application

### 7.1 Run the Application Script
```
cd project-root/application/
python App.py
```
## 8 Project Directory Structure 
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
├── Readme.md
├── test.gv
├── Application
│   ├── App.py
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
## 8.1 Major Files in the Directory :

### 8.1.1 BATMAN Advanced Files :
```
network-auto-configuration-master\Jetson-Nano-Projects\Projects\build\batman-adv-2022.3\net\batman-adv
```
**Network Configuration Scripts:**

**start-batman-adv.sh:**
This script configures your device to participate in an ad-hoc network using BATMAN-adv.
How it works: It sets up the necessary network interfaces, loads the BATMAN-adv module, and initializes the mesh network settings. By running this script, your device becomes part of the mesh network, enabling it to communicate with other devices running the same script.
start-batman-adv-client.sh:
Purpose: Similar to start-batman-adv.sh, but specifically tailored for client devices in the mesh network.
How it works: This script focuses on configuring devices that primarily act as clients, ensuring they can join the mesh network and communicate effectively with other nodes.
Installation Scripts:

**batmanInstall.sh:**
This script automates the installation of BATMAN-adv on your device.
How it works: It downloads the necessary BATMAN-adv packages, compiles the source code (if needed), and installs the software on your device. This script ensures that all the required dependencies and configurations are set up correctly.
Makefile:

**Makefile:**
Used for building and installing BATMAN-adv from source code.
How it works: The Makefile contains a set of directives used by the make build automation tool to compile and install BATMAN-adv. Running make followed by sudo make install will compile the BATMAN-adv source code and install it on your system.
Module Loading:

**sudo modprobe batman-adv:**
This command loads the BATMAN-adv kernel module into the running kernel.
How it works: The modprobe command is used to add or remove modules from the Linux kernel. By running sudo modprobe batman-adv, you ensure that the BATMAN-adv module is loaded and ready to handle network traffic on your device.

### 8.1.2 wandb Directory:
```
network-auto-configuration-master\SystemBasedClientSelection\wandb
```
**debug-cli.root.log, debug-cli.saintlab.log, debug-internal.log, debug.log, latest-run** : Log files generated by the Weights & Biases (wandb) tool for experiment tracking and logging.

### 8.1.3 ' torch_client.py ':
```
network-auto-configuration-master\Benchmarking
```
**Client-Side Federated Learning Operations**: This script is responsible for handling the client-side operations in a federated learning setup. Trains the local machine learning model on the client’s local dataset also Computes updates to the model parameters based on the local training data and Sends model updates to the central server and receives the global model parameters from the server.

### 8.1.4 ' torch_server.py ':
```
network-auto-configuration-master\Benchmarking
```
**Server-Side Federated Learning Operations**: This script is responsible for managing the server-side operations in a federated learning setup. Collects model updates from multiple clients and aggregates them to update the global model parameters also Sends the updated global model parameters back to the clients and Orchestrates the training rounds, ensuring synchronization between clients and the server. 

### 8.1.5 ' App.py ':

**1 Initializing the Application**: Setting up necessary configurations, initializing variables, and preparing the environment.

**2 Running Core Functionalities**: Executing the main functions of the application, such as processing data, running algorithms, or managing user interactions.

**3 Orchestrating Other Components**: Calling functions or methods from other modules and managing the workflow of the application.

**4 Handling Inputs and Outputs**: Managing input from users or other systems and producing the required outputs, whether they are files, visualizations, or other forms of data.

By serving as the central script, App.py acts as the entry point for the application, coordinating the different parts of the project to work together seamlessly.



