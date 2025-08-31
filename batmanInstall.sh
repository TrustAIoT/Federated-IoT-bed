#!/bin/bash

#WIP Do not run this script unless you are sure of what you are doing

echo "Installation script for batman-adv"

echo "Getting wget if it is not already installed"
pip3 install wget


#Download batman-adv, batctl, and alfred into their own shared directory
mkdir batman-adv
cd batman-adv
wget https://downloads.open-mesh.org/batman/stable/sources/batman-adv/batman-adv-2023.1.tar.gz
wget https://downloads.open-mesh.org/batman/stable/sources/batctl/batctl-2023.1.tar.gz
wget https://downloads.open-mesh.org/batman/stable/sources/alfred/alfred-2023.1.tar.gz

#Extract tar files into their own folders and clean up directory
tar -xvzf batman-adv-2023.1.tar.gz
tar -xvzf batctl-2023.1.tar.gz
tar -xvzf alfred-2023.1.tar.gz
rm batman-adv-2023.1.tar.gz
rm batctl-2023.1.tar.gz
rm alfred-2023.1.tar.gz

#Build batman-adv
cd batman-adv-2023.1
sudo make
cd ..

#Build batctl
cd batctl-2023.1
sudo apt-get install libnl-genl-3-dev
sudo make 
sudo mv batctl /usr/bin
cd ..

#Build alfred
cd alfred-2023.1
sudo make 

