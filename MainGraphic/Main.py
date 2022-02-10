import os


import keyboard as kb

import PIL.ImageOps
from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk

import Annoyence as ay


def init():
    # Load assets
    global ScreenList
    global frm
    global root
    global background
    global balk
    global windowknop
    os.chdir("MainGraphic")
    root = Tk()
    root.geometry("1000x502")
    root.resizable(False, False)
    background = ImageTk.Image.open("WindowsILL background.jpg")
    background = background.resize((1000, 500))
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.Image.open("WindowsILL menubalk.png")
    windowknop = ImageTk.Image.open("WindowsILL windowsknop.png")
    windowknop = ImageTk.PhotoImage(windowknop)


def OpenTaakbeheer():
    exec(open("Taakbeheer.py").read())


def on_click(id):
    global button1
    match id:
        case 1:
            button1 = True


def Start():
    backgroundlabel = ttk.Label(image=background)
    backgroundlabel.image = background
    backgroundlabel.pack()
    backgroundlabel.place(x=0, y=0)
    boop = ttk.Button(root, text="Hello!", command=OpenTaakbeheer, width=50)
    boop.pack()
    boop.place(x=10, y=50)
    root.lower()





if __name__ == '__main__':
    init()
    ay.delay(1)
    Start()
    if kb.is_pressed('b'):
        print("You're in control!")
    root.mainloop()
