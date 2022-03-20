import os
import subprocess
import sys
import datetime as dt
import keyboard as kb
import PIL.ImageOps
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.ttk as ttk
import random
import mouse

import MainGraphic.Annoyance as ay
import MainGraphic.Calculator as calc
import MainGraphic.unwingame as uwg
import MainGraphic.Taakbeheer as task
import MainGraphic.uselessbox as box

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
    global glue_app
    global lastkey
    global opened_list
    global dev
    global sticky
    global HOTELAD
    global HOTELAD2
    global menu
    menu = 0
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
    glue_app = ImageTk.PhotoImage(ImageTk.Image.open("Lijm pictogram .png").resize((100, 100)))
    HOTELAD = ImageTk.PhotoImage(ImageTk.Image.open("RojalParck.png").resize((300, 300)))
    HOTELAD2 = ImageTk.PhotoImage(ImageTk.Image.open("Onbetrouwbare ad hotelkamer Project Informatica 2.png").resize((300, 300)))

def checkinstalled(app):
    os.chdir("..\MainGraphic")
    try:
        file = open("Installed.txt", "r")
    except FileNotFoundError:
        return False
    check = file.read()
    if check.find(app) != -1:
        return True
    else:
        print("No")
        return False

def add_onderbalk(file):
    global opened_list
    tot_items = len(opened_list)
    match file:
        case "Calculator.py":
            menu = ttk.Button(root, image=pressed_calc, command=lambda m=file: openapp(m, False))
        case "Taakbeheer.py":
            menu = ttk.Button(root, image=pressed_task, command=lambda m=file: openapp(m, False))
        case "unwingame.py":
            menu = ttk.Button(root, image=pressed_game, command=lambda m=file: openapp(m, False))
        case "Letter.py":
            menu = ttk.Button(root, image=pressed_game, command=lambda m=file: openapp(m, False))
        case "uselessbox.py":
            menu = ttk.Button(root, image=pressed_game, command=lambda m=file: openapp(m, False))
    menu.place(x=(tot_items * 50), y=402)
    root.update()

def openapp(file, bool=True):
    global opened_list
    opened_list.append(file)
    if bool: add_onderbalk(file)
    ay.delay(1, dev)
    os.chdir("../MainGraphic")
    try:
        subprocess.run([sys.executable, "Annoyance.py"], check=True)
    finally:
        subprocess.run([sys.executable, file], check=True)

def Start():
    backgroundlabel = tk.Label(image=background)
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)
    if checkinstalled("Task"):
        task = ttk.Button(root, image=taskknop, command=lambda m='Taakbeheer.py': openapp(m))
        task.place(x=20, y=20)
    if checkinstalled("Calc"):
        calc = tk.Button(root, image=calcknop, command=lambda m='Calculator.py': openapp(m))
        calc.place(x=22, y=150)
    if checkinstalled('Game'):
        game = tk.Button(root, image=gameknop, command=lambda m='unwingame.py': openapp(m))
        game.place(x=21, y=280)
    if checkinstalled("Glue"):
        glue = tk.Button(root, image=glue_app, command=stay_here)
        glue.place(x=150, y=20)
    if checkinstalled("box"):
        box = tk.Button(root,image=gameknop, command=lambda m='uselessbox.py':openapp(m))
        box.place(x=150,y=150)
    if checkinstalled("Word"):
        word = tk.Button(root, image=gameknop, command=lambda m='Letter.py': openapp(m))
        word.place(x=152, y=150)
    onderbalk = tk.Label(root, image=balk)
    onderbalk.place(x=0, y=400)
    zoek = tk.Button(root, text="ZOEK", command=search)
    zoek.place(x=800, y=440)
    today = dt.datetime.now()
    randomjaar = random.randint(0, today.year)
    date = today.year-randomjaar, 12- today.month, 30- today.day
    time = 24-today.hour, ":", 60-today.minute
    label = tk.Label(root, text=date, fg="black")
    label1 = tk.Label(root, text=time, fg="black")
    label.place(relx=0.997, rely=0.898, anchor='se')
    label1.place(relx=0.989, rely=0.85, anchor='se')

def search():
    ay.delay(0.5)
    ay.ping("Search result:", "Niks gevonden", 1)

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
