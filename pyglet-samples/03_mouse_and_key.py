import pyglet
from pyglet.window import key

import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    window = pyglet.window.Window()

    @window.event
    def on_key_press(symbol, modifiers):
        # print('A key was pressed')
        # print(symbol, modifiers)
        if symbol == key.A:
            print('The "A" key was pressed.')
        elif symbol == key.LEFT:
            print("The left arrow key was pressed.")
        elif symbol == key.ENTER:
            print("The enter key was pressed.")
        elif symbol == key.P:
            window_img = pyglet.image.get_buffer_manager().get_color_buffer()
            img_data = window_img.get_image_data() # pyglet.image.ImageData
            
            img_bytes = img_data.data

            np_img = np.fromstring(img_bytes, dtype=np.uint8)
            np_img = np.reshape(np_img, (img_data.height, img_data.width, -1))

            print(img_data)
            print(type(img_bytes))
            print(len(img_bytes))
            print(np_img.shape)

    @window.event
    def on_draw():
        window.clear()

    # window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()
