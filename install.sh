#!/bin/sh

apt-get update
apt-get -y install python3-gpiozero
apt-get -y install python3-flask
apt-get -y install python3-w1thermsensor

grep -q "^dtoverlay=w1-gpio" /boot/config.txt

if [ $? -ne 0 ]
  then echo "\ndtoverlay=w1-gpio\n" >> /boot/config.txt
fi

echo "\nPlease reboot to finish installation\n"
