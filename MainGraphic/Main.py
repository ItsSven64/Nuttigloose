import os
import subprocess
import sys

import keyboard as kb

import PIL.ImageOps
from PIL import ImageTk, Image
import tkinter as ttk

import Annoyance as ay
import Calculator


def init():
    # Load assets
    global frm
    global root
    global background
    global balk
    global windowknop
    os.chdir("MainGraphic")
    root = ttk.Tk()
    root.geometry("1000x502")
    root.resizable(False, False)
    background = ImageTk.Image.open("WindowsILL background.jpg")
    background = background.resize((1000, 500))
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.Image.open("WindowsILL menubalk.png")
    windowknop = ImageTk.Image.open("WindowsILL windowsknop.png")
    windowknop = ImageTk.PhotoImage(windowknop)


def open(file):
    subprocess.run([sys.executable, file], check=True)

def on_click(id):
    global button1
    match id:
        case 1:
            button1 = True


def Start():
    backgroundlabel = ttk.Label(image=background)
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    task = ttk.Button(root, text="Task", command=lambda m='Taakbeheer.py': open(m), height=3, width=6)
    task.place(x=20, y=20)
    calc = ttk.Button(root, text="Calc", command=lambda m='Calculator.py': open(m), height=3, width=6)
    calc.place(x=22, y=100)
    root.lower()





if __name__ == '__main__':
    init()
    Start()
    root.mainloop()
