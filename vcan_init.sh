#!/bin/bash

sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up
echo "========================="
echo "vcan0 device initialized."
echo "========================="