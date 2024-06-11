# Development and Validation of A Heterogeneous Wireless Mesh IoT Testbed with Distributed Machine Learning

# About the Project 

The development of IoT devices has led to increased interests in distributed machine learning on edge devices for many researchers. However, a multitude of current distributed machine learning research is validated mainly by simulation alone. To fill the reality gap, testbeds are developed for physical deployments of these machine learning models. In this report, we present our current implementation of a wireless mesh IoT testbed consisting of the following heterogeneous devices: Raspberry Pi 4 Model B, Jetson Nano, and Jetson Orin Nano. Our wireless mesh testbed is connected through a mesh ad-hoc network, where packets are routed using the popular routing protocol, B.A.T.M.A.N IV. To validate the setup of our testbed and the multi-hop capabilities of B.A.T.M.A.N IV, we query a variety of network metrics in single-hop and multi-hop scenarios. In addition, we perform an experiment on federated learning across our testbed, in which we utilize the popular FedAVG aggregation server to train a Resnet 18 model for image classification using the Cifar10 dataset. We analyze the result of our experiment across heterogeneous devices to discover potential problems in the naive assumption of homogeneity across clients. In particular, physical deployment of models on IoT devices significantly enlarges the training time, and with the need to communicate across distance, enlarges communication time. We thus recommend some research directions to solve the problems, in which our testbed can provide assistance in physical deployment.

With the popularity of Internet of Things (IoT) devices in the market, researchers increased their attention leveraging the mass computational power available from the massive pool of IoT devices [1]. Distributed Machine Learning (DML) research has been accelerated during the current century, of which various models and techniques investigate different aspects like architecture, communication, protocols, applications, security and privacy. However, the performance evaluation and deployments of these models often utilized simulation techniques. These simulation tools are capable of simulating various delays and network conditions across devices, but various nuances of communication between devices are still missing from various simulation models. In addition, much machine learning research assumes homogeneity across various conditions such as statistical homogeneity in data and models, and system homogeneity in devices. To fill the reality gap, testbeds are developed for physical deployments of these machine learning models.

# Network Topology 

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

![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/c126bc5d-abc5-47ef-8fdc-a2ba8ec21c6f)

# Project Structure 

### /application/

The **application/** directory is the core component of the project, containing the primary code and utilities necessary to run and manage the distributed machine learning system. The main purposes of this directory are:

1. **Managing Application Workflow**:
   - The **Controllers/** subdirectory contains controllers that are responsible for orchestrating and managing the workflow of the application, ensuring that different components interact seamlessly.

2. **Handling Communication**:
   - The **Communication/** subdirectory deals with the protocols and mechanisms required for inter-device communication, ensuring efficient data transfer and synchronization.

3. **Machine Learning Models**:
   - The **Models/** subdirectory stores the machine learning models used in the application, including their architecture and configuration.

4. **Process Management**:
   - The **Processes/** subdirectory includes scripts and modules that handle various processes necessary for the application, such as data preprocessing, training, and evaluation.

5. **Utility Functions**:
   - The **Utility/** subdirectory contains utility scripts and functions that provide auxiliary support to the main components, such as logging, data manipulation, and configuration handling.

6. **View Layer Management**:
   - The **Views/** subdirectory manages the view layer of the application, which might include visualization and user interface components.

7. **Main Application Script**:
   - **App.py** is the main script that initiates and runs the application, integrating all the components and managing the overall execution flow.

8. **Interactive Development and Testing**:
   - **Untitled.ipynb** is a Jupyter notebook designed for interactive development and testing, allowing developers to experiment with code snippets, visualize data, and debug the application in a more flexible environment.

Overall, the **application/** directory serves as the backbone of the project, containing all the essential components required to develop, run, and manage the distributed machine learning system efficiently.

### /benchmark/

The **benchmark/** directory is dedicated to benchmarking the federated learning setup, providing scripts, configurations, and data necessary to evaluate the performance of the system. The main purposes of each component in this directory are:

1. **Configuration Management**:
   - **config/**: Contains configuration files that define the settings and parameters for the benchmark tests, ensuring consistent and reproducible benchmarking results.

2. **Benchmark Data**:
   - **data/**: Stores the data used specifically for benchmarking purposes, allowing tests to be run on consistent datasets.

3. **Training Scripts**:
   - **trainer/**: Includes the training scripts and modules tailored for the benchmarking process, facilitating the evaluation of model training performance under different conditions.

4. **Logging and Metrics**:
   - **wandb/**: Contains logs and metrics tracked using Weights and Biases (wandb), a popular tool for experiment tracking and visualization, enabling detailed analysis of benchmark results.

5. **Module Initialization**:
   - **__init__.py**: Initializes the benchmark module, making it a recognizable Python package and enabling the use of its scripts and configurations.

6. **MLOps Package Building**:
   - **build_mlops_pkg.sh**: A script to build the MLOps package, preparing the necessary components for machine learning operations and integrations.

7. **Client and Server Scripts**:
   - **run_client.sh**: A script to run the client-side processes for benchmarking, initiating the client’s participation in federated learning.
   - **run_server.sh**: A script to run the server-side processes for benchmarking, managing the aggregation and coordination of client models.

8. **Testing Scripts**:
   - **testing.py**: Scripts designed to test the benchmark setup, ensuring that all components are functioning correctly and performance metrics are accurately captured.

9. **PyTorch Client and Server**:
   - **torch_client.py**: A script for the client-side implementation of federated learning using PyTorch, responsible for local model training and communication with the server.
   - **torch_server.py**: A script for the server-side implementation of federated learning using PyTorch, handling model aggregation and coordination among clients.

Overall, the **benchmark/** directory serves to provide a comprehensive environment for assessing and validating the performance of the federated learning system, with tools and scripts tailored for detailed benchmarking and analysis.

### /fedml/

The **fedml/** directory contains the core FedML framework and its associated components, facilitating the development and deployment of federated learning applications. The main purposes of each component in this directory are:

1. **Applications**:
   - **applications/**: Contains various applications that utilize the FedML framework, showcasing how FedML can be applied to different use cases and scenarios.

2. **Benchmarking**:
   - **benchmark/**: Includes scripts and configurations for benchmarking the FedML framework, similar to the benchmarking directory at the root level, allowing users to assess the performance of FedML in different setups.

3. **MLOps Package Building**:
   - **build-mlops-package/**: Scripts designed to build MLOps packages, preparing the necessary components for operationalizing machine learning workflows with FedML.

4. **Data Management**:
   - **data/**: Stores datasets and data management scripts used within the FedML framework, supporting data preprocessing and handling for federated learning tasks.

5. **Documentation**:
   - **docs/**: Contains documentation for the FedML framework, providing guidance and reference materials for users and developers.

6. **FedML API**:
   - **fedml_api/**: Includes the core API components of the FedML framework, offering interfaces and functions for implementing federated learning models and processes.

7. **Core Components**:
   - **fedml_core/**: Houses the core components and utilities of the FedML framework, including algorithms, communication protocols, and system management tools.

Overall, the **fedml/** directory provides a comprehensive environment for developing, deploying, and benchmarking federated learning applications using the FedML framework.

# Hardware Devices 

![image.png](https://github.com/giridharsamineni/FEDML-AND-DISTRUBUTED-NETWORK/assets/81721268/f94e32ec-8087-4476-a00b-b09dca973ebd)

# SETTING UP HARDWARE DEVICES 

When developing an IoT testbed for wireless distributed machine learning, detailing the software environment decisions and considerations is crucial. This section covers the software environments for the various devices used in training.

Shared Frameworks/Modules
All devices (except Raspberry Pi Pico W) have the following software installed:

TensorFlow ~2.4
PyTorch ~1.12
FedML
Batman-Adv
Device-Specific Environment Details

### Jetson Nano Development Kit

Jetpack: 4.6

L4T 32.6.1

OS: Ubuntu 20.04.6 LTS

Linux Kernel: 4.9.253-tegra

### Jetson Orin Nano Developer Kit

Jetpack: 5.1.1 L4T 35.3.1

OS: Ubuntu 20.04.6 LTS

Linux Kernel: 5.10.104-tegra

### Raspberry Pi 4 Model B

OS: Debian GNU/Linux 11 (bullseye)

Linux Kernel: 6.1.21-v8+

### Raspberry Pi Pico WH

Environment: Raspberry Pi Pico Python SDK (MicroPython environment for RP2040 microcontrollers)

# Setting up the FEDML 

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

# B.A.T.M.A.N. Advanced (batman-adv) Setup Guide

## 1 Overview of B.A.T.M.A.N Advanced 

B.A.T.M.A.N. Advanced (batman-adv) is a routing protocol designed for multi-hop ad hoc networks. This guide will walk you through the installation of batman-adv along with its associated tools, batctl and alfred. We will also explain the directory structure and how to use these tools to set up and manage your mesh network. batman-adv operates at layer 2, allowing for seamless data transmission across multiple nodes in a mesh network. This setup will help you get batman-adv up and running on your devices, enabling efficient routing and data sharing across your network.

## 2 Prerequisites

Ensure you have a Linux-based system.

Basic knowledge of terminal commands.

wget and pip3 installed on your system

## 3 Installation Steps 

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
