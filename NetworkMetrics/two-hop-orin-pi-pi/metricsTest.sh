#!/bin/bash

echo "Query originators"
sudo batctl o | tee $1
echo "Query ping"
sudo batctl ping -R d8:3a:dd:21:c1:92 -c 20 | tee -a $1
echo "Query throughput"
sudo batctl tp d8:3a:dd:21:c1:92 -t 20000 | tee -a $1
echo "Finish"

