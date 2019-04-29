import tkinter as tk

app = tk.Tk()
app.geometry('250x250')

radio_value = tk.IntVar()

# basic radio button
# radio_1 = tk.Radiobutton(app, text='January', variable=radio_value, value=1)
# radio_2 = tk.Radiobutton(app, text='Febuary', variable=radio_value, value=2)
# radio_3 = tk.Radiobutton(app, text='March', variable=radio_value, value=1)
# # if the radio buttons have the same value, they will be toggled all together when one is toggled.

# radio_1.grid(column=0, row=0)
# radio_2.grid(column=0, row=1)
# radio_3.grid(column=0, row=2)

# change indicator type
radio_1 = tk.Radiobutton(
    app,
    text='January',
    variable=radio_value,
    value=1,
    indicatoron=0,
)
radio_2 = tk.Radiobutton(
    app,
    text='Febuary',
    variable=radio_value,
    value=2,
    indicatoron=2,
)
radio_3 = tk.Radiobutton(
    app,
    text='March',
    variable=radio_value,
    value=1,
    indicatoron=1,
)

radio_1.grid(column=0, row=0)
radio_2.grid(column=0, row=1)
radio_3.grid(column=0, row=2)


app.mainloop()
