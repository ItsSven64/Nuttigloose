from re import *

from tkinter import *
from tkinter import ttk


def init():
    global frm
    global root
    root = Tk()
    root.geometry("1000x1000")
    root.resizable(False, False)
    frm = ttk.Frame(root, padding=10)
    frm.grid()


def Button(Text, column, row):
    ttk.Button(frm, text=Text, command=lambda m=Text: pressed(m)).grid(column=column, row=row)


def DisplayText(Text, column, row):
    global Label
    Label = ttk.Label(frm, text=Text).grid(column=column, row=row)


def pressed(Message):
    print(Message)

    match Message:
        case "Quit":
            Label.destroy()
            DisplayText("Nope", 1, 1)
        case "Empty":
            pass


init()
Button("Quit", 1, 1)
root.mainloop()
