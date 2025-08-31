#!/bin/bash

sudo sh -c "echo $1 > /sys/class/hwmon/hwmon1/target_pwm"
