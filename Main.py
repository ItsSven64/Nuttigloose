import os
import subprocess
import sys

from PIL import ImageTk, Image
import tkinter as tk
import tkinter.ttk as ttk
import mouse

import MainGraphic.Ads as ad
import MainGraphic.Annoyance as ay
import MainGraphic.Calculator as calc
import MainGraphic.unwingame as uwg
import MainGraphic.Taakbeheer as task

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
    global pressed_calc
    global lastkey
    global opened_list
    global dev
    global sticky
    sticky = False
    dev = False
    os.chdir("Images")
    root = tk.Tk()
    root.geometry("1000x502")
    root.resizable(False, False)
    root.title("WindowsIll 1.0")
    opened_list = []
    s = ttk.Style()
    s.theme_use('vista')
    root.bind('<KeyRelease>', keypress_handler)
    background = ImageTk.Image.open("WindowsILL background.jpg")
    background = background.resize((1000, 500))
    background = ImageTk.PhotoImage(background)
    balk = ImageTk.PhotoImage(ImageTk.Image.open("WindowsILL menubalk.png").resize((1000, 50)))
    windowknop = ImageTk.PhotoImage(ImageTk.Image.open("WindowsILL windowsknop.png").resize((75, 75)))
    taskknop = ImageTk.PhotoImage(ImageTk.Image.open("Taakbeheer pictogram.jpg").resize((100, 99)))
    calcknop = ImageTk.PhotoImage(ImageTk.Image.open("Rekenmachine pictogram .png").resize((100, 100)))
    pressed_calc = ImageTk.PhotoImage(ImageTk.Image.open('Rekenmachine pictogram geopend.png').resize((40, 40)))
    pressed_task = ImageTk.PhotoImage(ImageTk.Image.open("Taakbeheer pictogram geopend.jpg").resize((40,40)))
    gameknop = ImageTk.PhotoImage(ImageTk.Image.open("Game pictogram .png").resize((99, 100)))
    pressed_game = ImageTk.PhotoImage(ImageTk.Image.open("Game pictogram geopend.png").resize((40, 40)))

def add_onderbalk(file):
    global opened_list
    tot_items = len(opened_list)
    match file:
        case "Calculator.py":
            menu = ttk.Label(root, image=pressed_calc)
        case "Taakbeheer.py":
            menu = ttk.Label(root, image=pressed_task)
        case "unwingame.py":
            menu = ttk.Label(root, image=pressed_game)
    menu.place(x=(tot_items * 50), y=455)
    root.mainloop(1)

def open(file):
    global opened_list
    opened_list.append(file)
    print(opened_list)
    add_onderbalk(file)
    ay.delay(2, dev)
    os.chdir("../MainGraphic")
    subprocess.run([sys.executable, file], check=True)
    print("Closed")

def Start():
    backgroundlabel = tk.Label(image=background)
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    task = ttk.Button(root, image=taskknop, command=lambda m='Taakbeheer.py': open(m))
    task.place(x=20, y=20)
    calc = tk.Button(root, image=calcknop, command=lambda m='Calculator.py': open(m))
    calc.place(x=22, y=150)
    game = tk.Button(root, image=gameknop, command=lambda m='unwingame.py': open(m))
    game.place(x=21, y=280)
    glue = tk.Button(root, image=gameknop, command=stay_here)
    glue.place(x=150, y=20)
    onderbalk = tk.Label(root, image=balk)
    onderbalk.place(x=0, y=450)

def keypress_handler(event):
    global dev
    match event.keysym:
        case "m":
            dev = True
            boop = tk.Message(root, text="DEVMODE", width=100)
            boop.place(x=0, y=0)
            ay.delay(2)

def stay_here():
    global pos
    global sticky
    pos = mouse.get_position()
    sticky = True
    print("CLICK")
    print(pos)

def all():
    maininit()
    Start()
    while True:
        if sticky:
            mouse.move(x=pos[0], y=pos[1], absolute=True)
            print("MOVE")
        root.update()


if __name__ == '__main__':
    all()
