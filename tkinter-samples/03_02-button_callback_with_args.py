#!/usr/bin/env python3
# encoding=utf-8
import tkinter as tk
from functools import partial

app = tk.Tk()

# callback with arguments
label = tk.Button(app, text='0')


def label_counter(num: int):
    count = int(str(label['text']))
    count += num
    label.config(text=str(count))


btn = tk.Button(
    app,
    text='increase',
    width=30,
    command=partial(label_counter, 2),
)

btn.pack()
label.pack()

app.mainloop()
