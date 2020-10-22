#!/usr/bin/env python3
# encoding=utf-8
import tkinter as tk
import tkinter.font

app = tk.Tk()

label_1 = tk.Label(app, text='Times 20', font=('Times', 20), bg='black', fg='white')
label_2 = tk.Label(app, text='Times 20 Italic', font=('Times', 20, 'italic'))

font_3 = tk.font.Font(font=('Helvetica', 20, tk.font.BOLD))
font_3 = tk.font.Font(family='Helvetica', size=20, weight=tk.font.BOLD, underline=1, overstrike=1)
label_3 = tk.Label(app, text='Helvetica 20 bold underline overstrike', font=font_3)

label_1.pack()
label_2.pack()
label_3.pack()

app.mainloop()
