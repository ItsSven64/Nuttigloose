import os

import random
from time import *
from random import *

import PIL.ImageOps
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
    root.geometry("1000x502")
    root.resizable(False, False)
    background = ImageTk.Image.open("WindowsILL background.jpg")
    background = background.resize((1000, 500))
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
    backgroundlabel.pack()
    backgroundlabel.place(x=0, y=0)
    boop = ttk.Button(root, text="Hello!", command=Clearscreen, width=50, height=50)
    boop.pack()
    boop.place(x=10, y=50)



    root.lower()


    ScreenList.append(boop)


init()
Start()
print(ScreenList)
root.mainloop()
