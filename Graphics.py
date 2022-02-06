from tkinter import *
from tkinter import ttk

def Init():
    global root
    global frm
    root = Tk()
    root.geometry("1000x1000")
    root.resizable(False, False)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
def Button(Text, column, row):
    ttk.Button(frm, text=Text, command=lambda m=Text: pressed(m)).grid(column=column, row=row)

def DisplayText(Text, column, row):
    ttk.Label(frm, text=Text).grid(column=column, row=row)

def pressed(Message):
    match Message:
        case "Quit":
            DisplayText("Nope", 1, 1)

Init()
root.mainloop()