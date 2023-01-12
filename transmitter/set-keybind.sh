#!/bin/bash

cat >> ~/.bashrc << EOF

stty -echoctl
tput civis
bind -x '"\C-[":"python3 ~/pi-attention/transmitter/button1.py 2>/dev/null"'
bind -x '"\C-]":"python3 ~/pi-attention/transmitter/button2.py 2>/dev/null"'
clear
/usr/bin/python3 ~/pi-attention/weather/weather.py 2>/dev/null
EOF