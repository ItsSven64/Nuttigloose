import os

import random
from time import *
from random import *

import PIL.ImageOps
from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk

import MainGraphic.Annoyance as ay


def init():
     # Load assets
    global ScreenList
    global frm
    global taskroot
    global background
    global balk
    global windowknop
    taskroot = Tk()
    taskroot.geometry("500x502")
    taskroot.resizable(False, False)
    background = ImageTk.Image.open("../Images/WindowsILL background.jpg")
    background = background.resize((500, 500))
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.Image.open("../Images/WindowsILL menubalk.png")
    windowknop = ImageTk.Image.open("../Images/WindowsILL windowsknop.png")
    windowknop = ImageTk.PhotoImage(windowknop)




def start():
    bckgrnd = ttk.Label(image= background)
    bckgrnd.pack()
    bckgrnd.place(x=0, y=0)
    btn1 = ttk.Button(text='Click to get current programs!', command=ay.letsmove, width=30)
    btn1.pack()
    btn1.place(x=50, y=250)

def TaskMain():
    init()
    start()
    taskroot.mainloop()

if __name__ == '__main__':
    init()
    start()
