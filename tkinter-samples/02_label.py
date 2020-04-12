# encoding=utf-8
import tkinter as tk
import tkinter.font
import requests
from io import BytesIO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

app = tk.Tk()

# basic label
# label = tk.Label(app, text='This is a Label')
# label.pack()

# more complicated labels
# label_1 = tk.Label(app, text='Times 20', font=('Times', 20), bg='black', fg='white')
# label_2 = tk.Label(app, text='Times 20 Italic', font=('Times', 20, 'italic'))

# # font_3 = tk.font.Font(font=('Helvetica', 20, tk.font.BOLD))
# font_3 = tk.font.Font(family='Helvetica', size=20, weight=tk.font.BOLD, underline=1, overstrike=1)
# label_3 = tk.Label(app, text='Helvetica 20 bold underline overstrike', font=font_3)

# label_1.pack()
# label_2.pack()
# label_3.pack()

# display image with label
# tk.PhotoImage only support GIF, PPM/PGM
# image = tk.PhotoImage(file='<image-path>')
# label = tk.Label(app, image=image)
# labe.pack()

app.mainloop()