#!/bin/bash

while ! lsmod | grep -q batman_adv;
do
	echo "batman-adv is not loaded yet ... sleep for 5 seconds"
	sleep 5
done

echo "Start adhoc mode and join a wavelength"
#sudo iw dev wlan0 del
#sudo iw phy phy0 interface add wlan0 type ibss

sudo ip link set up mtu 1468 dev wlan0
sudo iw dev wlan0 ibss join my-mesh-network 2412 HT20

echo "Allow batman to manage wlan0 (Wifi)"
sudo batctl if add wlan0
sudo batctl gw_mode server
sudo sysctl -w net.ipv4.ip_forward=1


sudo iptables -t nat -A POSTROUTING -o ra0 -j MASQUERADE
sudo iptables -A FORWARD -i ra0 -o bat0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i bat0 -o ra0 -j ACCEPT

echo "Start batman virtual interface"
sudo ip link set up dev bat0

echo "Configure ip address for virtual interface"
sudo ip addr add 192.168.123.1/24 dev bat0
sudo ifconfig bat0 broadcast 192.168.123.255 

echo "Restart DNS server"
sudo systemctl restart dnsmasq.service

echo "Set up alfred and batadv-vis in 3 seconds"
sleep 3
sudo alfred -i wlan0 -m &
sudo batadv-vis -i bat0 -s &

