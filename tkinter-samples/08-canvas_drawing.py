#!/usr/bin/env python3
# encoding=utf-8
import io

import tkinter as tk

import numpy as np
from PIL import Image


class Pen():
    def __init__(self):
        self.down = False
        self.x = None
        self.y = None


app = tk.Tk()

CANVAS_WIDTH = 640
CANVAS_HEIGHT = 640

canvas = tk.Canvas(
    app,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
)

# canvas.pack()
canvas.grid(column=0, row=0)

label = tk.Label(
    app,
    text='Label here'
)

label.grid(column=0, row=1)

pen = Pen()


def key_press(event):
    global pen
    # print(event)
    if event.keycode == 16:  # shift key
        pen.down = True
        # print('Shift key is pressed')


def key_release(event):
    global pen
    # print(event)
    # print(event.char)

    if event.char == 's':
        ps: str = canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        # print(type(img))

        # require Ghostscript to be installed
        np_img = np.array(img)
        print(np_img.shape)

        # TODO export image

    elif event.char == 'c':
        canvas.create_rectangle(
            0,
            0,
            CANVAS_WIDTH,
            CANVAS_HEIGHT,
            fill='black',
        )

    elif event.keycode == 16:  # shift key
        pen.down = False
        pen.x = None
        pen.y = None
        # print('Shift key is released')


def mouse_move_event(event):
    global pen, canvas
    if pen.down:
        if (pen.x is None) or (pen.y is None):
            pen.x = event.x
            pen.y = event.y
        else:
            line_width = 5  # 5px line width
            canvas.create_line(
                pen.x,
                pen.y,
                event.x,
                event.y,
                width=line_width,
                fill='white',
            )

            pen.x = event.x
            pen.y = event.y

    # print(event)


# sample drawing method of Canvas widget
# canvas.create_line(0, 0, 200, 200)
# canvas.create_rectangle(0, 0, 50, 50, fill='black')

canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill='black')

canvas.bind('<Motion>', mouse_move_event)

app.bind('<KeyRelease>', key_release)
app.bind('<KeyPress>', key_press)

print('''
Hold Shift and move mouse to draw
Press C key to clear
Press S key to save canvas as image (TODO)
''')

app.mainloop()
