#!/bin/bash

#Install LCD Driver
rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD35-show 180

#Update Font Size
sed -i "s|FONTFACE=.*|FONTFACE=\"Terminus\"|g" /etc/default/console-setup
sed -i "s|FONTSIZE=.*|FONTSIZE=\"14x28\"|g" /etc/default/console-setup

reboot