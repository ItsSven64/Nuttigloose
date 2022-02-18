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
    global gameknop
    os.chdir("Images")
    root = ttk.Tk()
    root.geometry("1000x502")
    root.resizable(False, False)
    background = ImageTk.Image.open("../Images/WindowsILL background.jpg")
    background = background.resize((1000, 500))
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.Image.open("../Images/WindowsILL menubalk.png")
    windowknop = ImageTk.Image.open("../Images/WindowsILL windowsknop.png")
    windowknop = ImageTk.PhotoImage(windowknop)
    gameknop = ImageTk.Image.open("Game pictogram .png").resize((100, 100))
    gameknop = ImageTk.PhotoImage(gameknop)

def open(file):
    os.chdir("..\\MainGraphic")
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
    game = ttk.Button(root, text="Game", command=lambda m='(Un)WinGame.py': open(m))
    game.place(x=21, y=180)
    #root.lower()

if __name__ == '__main__':
    init()
    Start()
    root.mainloop()
