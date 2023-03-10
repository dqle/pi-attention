#!/usr/bin/env python

import logging
import time
import sys

from flask import Flask, request
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

app = Flask(__name__)
unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.1)

def scroll_text (text, color):

    rotation = 0
    if len(sys.argv) > 1:
        try:
            rotation = int(sys.argv[1])
        except ValueError:
            print("Usage: {} <rotation>".format(sys.argv[0]))
            sys.exit(1)

    unicornhatmini.set_rotation(rotation)
    display_width, display_height = unicornhatmini.get_shape()

    # Load 5x7 pixel font
    font = ImageFont.truetype("5x7.ttf", 8)

    # Measure the size of text
    text_width, text_height = font.getsize(text)

    # Create a new PIL image big enough to fit the text
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)

    # Draw the text into the image
    draw.text((display_width, -1), text, font=font, fill=255)

    offset_x = 0

    while offset_x + display_width < image.size[0]:
        for y in range(display_height):
            for x in range(display_width):
                r, g, b = color
                if image.getpixel((x + offset_x, y)) == 255:
                    unicornhatmini.set_pixel(x, y, r, g, b)
                else:
                    unicornhatmini.set_pixel(x, y, 0, 0, 0)

        offset_x += 1

        unicornhatmini.show()
        time.sleep(0.05)

#Disable logging
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/')
def home():
    return "pi-attention is running"

@app.route('/api/show-text', methods=['POST'])
def show_text():
    text = request.json['text']
    color = request.json['color'].split(",")
    color = [int(i) for i in color]
    scroll_text (text, color)
    return text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)