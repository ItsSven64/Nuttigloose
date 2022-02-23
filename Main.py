import os
import subprocess
import sys

import keyboard as kb
import PIL.ImageOps
from PIL import ImageTk, Image
import tkinter as ttk
import random

import MainGraphic.Annoyance as ay
import MainGraphic.Calculator
import MainGraphic.unwingame as uwg

def maininit():
    # Load assets
    global frm
    global root
    global background
    global balk
    global windowknop
    global gameknop
    global pressed_game
    global taskknop
    global pressed_task
    global calcknop
    global lastkey
    os.chdir("Images")
    root = ttk.Tk()
    root.geometry("1000x502")
    root.resizable(False, False)
    root.title("WindowsIll 1.0")
    root.bind('<KeyRelease>', keypress_handler)
    background = ImageTk.Image.open("WindowsILL background.jpg")
    background = background.resize((1000, 500))
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.Image.open("WindowsILL menubalk.png")
    windowknop = ImageTk.PhotoImage(ImageTk.Image.open("WindowsILL windowsknop.png").resize((75, 75)))
    taskknop = ImageTk.PhotoImage(ImageTk.Image.open("Taakbeheer pictogram.jpg").resize((100, 99)))
    calcknop = ImageTk.PhotoImage(ImageTk.Image.open("Rekenmachine pictogram .png").resize((100, 100)))
    pressed_task = ImageTk.PhotoImage(ImageTk.Image.open("Taakbeheer pictogram geopend.jpg").resize((99,100)))
    gameknop = ImageTk.PhotoImage(ImageTk.Image.open("Game pictogram .png").resize((99, 100)))
    pressed_game = ImageTk.PhotoImage(ImageTk.Image.open("Game pictogram geopend.png").resize((100, 98)))

def open(file):
    """match file:
        case "unwingame.py":
            game = ttk.Button(root, image=pressed_game)
            game.place(x=21, y=180)
        case "Taakbeheer.py":
            task = ttk.Button(root, image=pressed_task)
            task.place(x=20, y=20)"""
    ay.delay(2, dev)
    os.chdir("../MainGraphic")
    subprocess.run([sys.executable, file], check=True, shell=True)

def Start():
    backgroundlabel = ttk.Label(image=background)
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    task = ttk.Button(root, image=taskknop, command=lambda m='Taakbeheer.py': open(m))
    task.place(x=20, y=20)
    calc = ttk.Button(root, image=calcknop, command=lambda m='Calculator.py': open(m))
    calc.place(x=22, y=150)
    game = ttk.Button(root, image=gameknop, command=lambda m='unwingame.py': open(m))
    game.place(x=21, y=280)

def keypress_handler(event):
    global dev
    match event.keysym:
        case "m":
            dev = True
            boop = ttk.Message(root, text="DEVMODE", width=100)
            boop.place(x=0, y=0)
            ay.delay(2)



def all():
    choice = random.choice(list(range(1,10)))
    print(choice)
    for x in range(choice):
        ttk.Tk()
    maininit()
    Start()
    root.mainloop()

if __name__ == '__main__':
    all()
