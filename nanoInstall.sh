#!/bin/bash

#Installation Script for Raspberry Pi 3/4  
#WIP Do not run this script unless you are sure of what you are doing

echo "Beginning Installation Script for Raspberry Pi"
sudo apt update 
sudo apt install python3-pip
sudo apt-get install libopenmpi-dev

echo "Installing FedML and its dependencies..."
pip3 install -r "./pirequirements.txt"
echo "Finished installing FedML."
