import tkinter as tk
import tkinter.ttk as ttk
import random

import MainGraphic.Annoyance as ay



def calcinit():
    global calcroot
    global Label_Text
    global rst
    rst = False
    Label_Text = ""
    calcroot = tk.Tk()
    calcroot.geometry("255x250")
    calcroot.resizable(False, False)
    tk.Button(calcroot, text="1", command=lambda m="1": button_pressed(m), height=2, width=5).place(x=5, y=200)
    tk.Button(calcroot, text="2", command=lambda m="2": button_pressed(m), height=2, width=5).place(x=5, y=150)
    tk.Button(calcroot, text="3", command=lambda m="3": button_pressed(m), height=2, width=5).place(x=5, y=100)
    tk.Button(calcroot, text="4", command=lambda m="4": button_pressed(m), height=2, width=5).place(x=5, y=50)
    tk.Button(calcroot, text="5", command=lambda m="5": button_pressed(m), height=2, width=5).place(x=55, y=200)
    tk.Button(calcroot, text="9", command=lambda m="9": button_pressed(m), height=2, width=5).place(x=55, y=150)
    tk.Button(calcroot, text="-", command=lambda m="-": button_pressed(m), height=2, width=5).place(x=55, y=100)
    tk.Button(calcroot, text="+", command=lambda m="+": button_pressed(m), height=2, width=5).place(x=55, y=50)
    tk.Button(calcroot, text="^", command=lambda m="**": button_pressed(m), height=2, width=5).place(x=105, y=200)
    tk.Button(calcroot, text="X", command=lambda m="*": button_pressed(m), height=2, width=5).place(x=105, y=150)
    tk.Button(calcroot, text=".", command=lambda m=".": button_pressed(m), height=2, width=5).place(x=105, y=100)
    tk.Button(calcroot, text="0", command=lambda m="0": button_pressed(m), height=2, width=5).place(x=105, y=50)
    tk.Button(calcroot, text="(", command=lambda m="(": button_pressed(m), height=2, width=5).place(x=155, y=200)
    tk.Button(calcroot, text=")", command=lambda m=")": button_pressed(m), height=2, width=5).place(x=155, y=150)
    tk.Button(calcroot, text="!", command=lambda m="factorial(": button_pressed(m), height=2, width=5).place(x=155, y=100)
    tk.Button(calcroot, text="7", command=lambda m="7": button_pressed(m), height=2, width=5).place(x=155, y=50)
    tk.Button(calcroot, text="6", command=lambda m="6": button_pressed(m), height=2, width=5).place(x=205, y=200)
    tk.Button(calcroot, text="8", command=lambda m="8": button_pressed(m), height=2, width=5).place(x=205, y=150)
    tk.Button(calcroot, text="", command=lambda m="": button_pressed(m), height=2, width=5).place(x=205, y=100)
    tk.Button(calcroot, text=",", command=lambda m=",": button_pressed(m), height=2, width=5).place(x=205, y=50)
    tk.Button(calcroot, text="=", command=execute, height=2, width=5).place(x=205, y=5)
    tk.Button(calcroot, text="C", command=clear, height=2, width=5).place(x=155, y=5)
    calcroot.mainloop()

def button_pressed(tag):
    global Label_Text
    global lbl
    global rst
    tuple = (tag, Label_Text)
    Label_Text = ''.join(tuple)
    lbl = tk.Label(text=Label_Text)
    lbl.place(x=10, y=5)

def execute():
    global Label_Text
    global rstlbl
    global rst
    randomlist = [0, 1, 2, 3, 4, 5, 6]
    try:
        ay.delay(5, False)
        result = eval(Label_Text)
        result = (result - random.choice(randomlist))
    except SyntaxError:
        ay.delay(10, False)
        result = "Error"
    Label_Text = "                   "
    lbl = tk.Label(text=Label_Text)
    lbl.place(x=10, y=5)
    Label_Text = ''
    ay.ping("Results are in!", str(result), 5)

def clear():
    global Label_Text
    Label_Text = "               "
    lbl = tk.Label(text=Label_Text)
    lbl.place(x=10, y=5)
    Label_Text = ""


if __name__ == '__main__':
    calcinit()
    calcroot.mainloop()
