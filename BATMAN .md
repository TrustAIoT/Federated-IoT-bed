# B.A.T.M.A.N. Advanced (batman-adv) Setup Guide

## Run the Installation Script:
chmod +x install_batman_adv.sh
./install_batman_adv.sh

## Running and Testing the Setup

### 1 Load the Kernel Module:


sudo modprobe batman-adv

### 2 Add Network Interfaces to batman-adv:
sudo batctl if add <network-interface>

sudo ip link set up dev bat0

## Testing Conectivity 

## 1 Check the Status of Interfaces:
sudo batctl if

### 2 Ping Between Nodes:

Ensure batman-adv is running on all nodes in your network, then use ping to test connectivity.
ping <other-node-ip>

## Monitoring and Managing the Network

### 1 View Routing Table
sudo batctl o

### 2 Check the log: 
sudo dmesg | grep batman-adv

## Results Storage

batman-adv: Routing information and logs can be accessed using batctl commands.

batctl: Provides a suite of commands to manage and monitor batman-adv.

alfred: Collects and distributes information among nodes, results can be accessed using ' alfred ' commands.
