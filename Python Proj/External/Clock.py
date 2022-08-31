from tkinter import *
from time import *

root = Tk()
root.title("Clock")


def time_update():
    time_var = strftime("%H:%M:%S %p")
    clock.config(text=time_var)
    clock.after(200, time_update)


clock = Label(root, font=("DS-Digital", 90), bg="black", fg="yellow")
clock.pack()

time_update()

root.mainloop()
