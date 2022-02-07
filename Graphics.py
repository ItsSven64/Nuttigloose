from time import *
imor
from tkinter import *
from tkinter import ttk


def init():
    global frm
    global root
    root = Tk()
    root.geometry("1000x1001")
    root.resizable(False, False)
    frm = ttk.Frame(root, padding=10)
    frm.grid()


def Button(Text, column, row):
    BTNid = [ttk.Button(frm, text=Text, command=on_click(Text)).grid(column=column, row=row), Text]
    return BTNid

def DisplayText(Text, column, row):
    TXTid = [ttk.Label(frm, text=Text).grid(column=column, row=row), Text]
    return TXTid


def on_click(BTNid):
    global stage
    match BTNid:
        case "Start loading!":
            stage = 1

def DeClick():
    clicked = False



stage = 0
init()
Button("Start loading", 1, 1)
Button("Start loading!", 50, 100)
DisplayText("Welcome to Nuttigloos!", 1, 1)
while True:
    match stage:
        case 0:

        case 1:
            print("Click!")
            stage = 0
    root.mainloop()
