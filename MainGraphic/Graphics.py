import os

import random
from time import *
from random import *

from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk


def init():
    #Load assets
    global ScreenList
    global frm
    global root
    global background
    global balk
    global windowknop
    os.chdir("MainGraphic")
    print(os.getcwd())
    root = Tk()
    root.geometry("1000x1001")
    root.resizable(False, False)
    frm = ttk.Frame(root, padding=0)
    frm.grid()
    background = ImageTk.Image.open("WindowsILL background.jpg")
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.Image.open("WindowsILL menubalk.png")
    windowknop = ImageTk.Image.open("WindowsILL windowsknop.png")
    windowknop = ImageTk.PhotoImage(windowknop)
    ScreenList = []




def Clearscreen():
    root.destroy()



def on_click(id):
    global button1
    match id:
        case 1:
            button1 = True


def Start():
    global hello
    global boop
    backgroundlabel = ttk.Label(image=background)
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    hello = ttk.Label(frm, text="Hello")
    ScreenList.append(hello)
    hello.grid(column=1, row=1)
    boop = ttk.Button(frm, text="Hello!", command=Clearscreen)
    ScreenList.append(boop)
    boop.grid(column=5, row=1)

init()
Start()
print(ScreenList)
root.mainloop()
