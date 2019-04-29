import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('200x100')

label_top = tk.Label(
    app,
    text='Choose your favourite dish',
)

label_top.grid(column=0, row=0)

combobox = ttk.Combobox(
    app, 
    values=[
        'Sushi',
        'Pizza',
        'Spaghetti',
        'Butter chicken',
        'Fish pie',
    ]
)

print(dict(combobox))
combobox.grid(column=0, row=1)
combobox.current(1)

print(combobox.current(), combobox.get())

# binding event
def selected_event(event):
    print(event)
    print(combobox.get())

combobox.bind('<<ComboboxSelected>>', selected_event)

app.mainloop()