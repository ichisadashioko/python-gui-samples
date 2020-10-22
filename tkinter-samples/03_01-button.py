#!/usr/bin/env python3
# encoding=utf-8
import tkinter as tk

app = tk.Tk()

# basic buttons
btn1 = tk.Button(app, text='Button 1')
btn2 = tk.Button(app, text='Button 2')

btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.RIGHT)

label = tk.Button(app, text='0')

# event callback


def label_counter():
    count = int(str(label['text']))
    count += 1
    label.config(text=str(count))


btn = tk.Button(app, text='increase', width=30, command=label_counter)

btn.pack()
label.pack()

app.mainloop()
