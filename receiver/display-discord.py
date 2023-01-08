#!/usr/bin/env python

import signal
import time
import logging
from flask import Flask
from PIL import Image
from unicornhatmini import UnicornHATMini

app = Flask(__name__)
unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.5)

#Disable logging
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/')
def home():
    return "pi-attention is running"

@app.route('/api/text-discord', methods=['POST'])
def text_discord():
    for x in range(17):
        for y in range(7):
            unicornhatmini.set_pixel(x, y, 114, 137, 218)
    image = Image.open("text-discord.png")
    unicornhatmini.set_image(image)
    unicornhatmini.show()

@app.route('/api/text-come-over', methods=['POST'])
def text_come_over():
    for x in range(17):
        for y in range(7):
            unicornhatmini.set_pixel(x, y, 167, 36, 41)
    image = Image.open("text-comeover.png")
    unicornhatmini.set_image(image)
    unicornhatmini.show()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)