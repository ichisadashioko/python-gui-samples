#!/usr/bin/env python3
# encoding=utf-8
import os
from io import BytesIO

import tkinter as tk

import requests
from PIL import Image, ImageTk

app = tk.Tk()

image_filename = 'isekai_mahou.jpg'
if not os.path.exists(image_filename):
    print('downloading missing image')
    sample_image_url = 'https://i.imgur.com/lIjvcCJ.jpg'
    res = requests.get(sample_image_url)
    open(image_filename, mode='wb').write(res.content)

"""tk.PhotoImage only support GIF, PPM/PGM"""
image = ImageTk.PhotoImage(Image.open(image_filename))
label = tk.Label(app, image=image)
label.pack()

app.mainloop()
