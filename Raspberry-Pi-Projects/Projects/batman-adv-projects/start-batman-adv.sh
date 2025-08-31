#!/bin/bash
# To reinstate the wlan0 interface, reboot or do:
# iw phy phy0 interface add wlan0 type managed
#echo "Switch to BATMAN_V"
#sudo batctl ra BATMAN_V

echo "Turn wlan0 into ad-hoc mode"
#sudo iw dev wlan0 del
#sudo iw phy phy0 interface add wlan0 type ibss
sudo ip link set up mtu 1468 dev wlan0
sudo iw dev wlan0 ibss join my-mesh-network 2412

#echo "Switch to batman_v"
#sudo modprobe batman-adv
#sudo batctl ra BATMAN_V

echo "Allow batman-adv to manage wlan0"
sudo batctl if add wlan0
sudo batctl gw_mode client

echo "Set up virtual interface"
sudo ip link set up dev bat0
sudo ip addr add 192.168.123.2/24 dev bat0
sudo ifconfig bat0 broadcast 192.168.123.255

echo "Set up alfred and batadv-vis in 3 seconds"
sleep 3
sudo alfred -i wlan0 -m &
sudo batadv-vis -i bat0 -s &
