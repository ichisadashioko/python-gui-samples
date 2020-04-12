import tkinter as tk
from functools import partial

app = tk.Tk()

# basic button
# btn1 = tk.Button(app, text='Button 1')
# btn2 = tk.Button(app, text='Button 2')

# btn1.pack(side=tk.LEFT)
# btn2.pack(side=tk.RIGHT)

# callback
# label = tk.Button(app, text='0')

# def label_counter():
#     count = int(str(label['text']))
#     count += 1
#     label.config(text=str(count))

# btn = tk.Button(app, text='increase', width=30, command=label_counter)

# btn.pack()
# label.pack()

# callback with arguments
label = tk.Button(app, text='0')

def label_counter(num: int):
    count = int(str(label['text']))
    count += num
    label.config(text=str(count))

btn = tk.Button(app, text='increase', width=30, command=partial(label_counter, 2))

btn.pack()
label.pack()

app.mainloop()