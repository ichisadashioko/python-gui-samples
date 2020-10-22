import tkinter as tk

app = tk.Tk()
app.geometry('150x100')

check_var = tk.BooleanVar()
check_var.set(True)

# # basic checkbox
# checkbox = tk.Checkbutton(app, text='Check Box', var=check_var)
# checkbox.grid(column=0, row=0)

# select and deselect
# print(f'Checkbox state: {check_var.get()}')
# checkbox.select()
# print(f'Checkbox state: {check_var.get()}')
# checkbox.deselect()
# print(f'Checkbox state: {check_var.get()}')

# simulate a click (toggle)
# print(f'Checkbox state: {check_var.get()}')
# checkbox.toggle()
# print(f'Checkbox state: {check_var.get()}')
# checkbox.toggle()
# print(f'Checkbox state: {check_var.get()}')

# callback
def on_click():
    print('Oh. I\'m clicked')
checkbox = tk.Checkbutton(app, text='Check Box', var=check_var, command=on_click)
checkbox.grid(column=0, row=0)

app.mainloop()
