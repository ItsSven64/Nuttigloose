import os
import sys

import tkinter as tk
from PIL import ImageTk
import subprocess

import MainGraphic.Annoyance as ay

def reset():
    os.remove("Installed.txt")
    file = open("Installed.txt", "w")
    file.close()
    print("Cleared!")

def install(app):
    os.chdir("..\MainGraphic")
    ay.delay(1)
    subprocess.run([sys.executable, "Annoyance.py"], check=True)
    file = open("Installed.txt", "a")
    file.write(app)

def start():
    global apptk
    global taskknop
    global calcknop
    global pressed_calc
    global pressed_task
    global gameknop
    global pressed_game
    global glue_app
    apptk = tk.Tk()
    apptk.geometry("700x700")
    apptk.resizable(False, False)
    os.chdir("..\Images")
    taskknop = ImageTk.PhotoImage(ImageTk.Image.open("Taakbeheer pictogram.jpg").resize((100, 99)))
    calcknop = ImageTk.PhotoImage(ImageTk.Image.open("Rekenmachine pictogram .png").resize((100, 100)))
    pressed_calc = ImageTk.PhotoImage(ImageTk.Image.open('Rekenmachine pictogram geopend.png').resize((100, 100)))
    pressed_task = ImageTk.PhotoImage(ImageTk.Image.open("Taakbeheer pictogram geopend.jpg").resize((100, 100)))
    gameknop = ImageTk.PhotoImage(ImageTk.Image.open("Game pictogram .png").resize((99, 100)))
    pressed_game = ImageTk.PhotoImage(ImageTk.Image.open("Game pictogram geopend.png").resize((100, 100)))
    glue_app = ImageTk.PhotoImage(ImageTk.Image.open("Lijm pictogram .png").resize((100, 100)))

    downloadcalc = tk.Button(apptk, image=calcknop, command=lambda m="Calc": install(m))
    downloadtask = tk.Button(apptk, image=taskknop, command=lambda m="Task": install(m))
    downloadgame = tk.Button(apptk, image=gameknop, command=lambda m="Game": install(m))
    downloadglue = tk.Button(apptk, image=glue_app, command=lambda m="Glue": install(m))
    downloadword = tk.Button(apptk, image=gameknop, command=lambda m="Word": install(m))
    resetbutton = tk.Button(apptk, text="RESET", command=reset)
    resetbutton.place(x=600, y=30)
    downloadcalc.place(x=30, y=30)
    downloadword.place(x=30, y=150)
    downloadgame.place(x=30, y=270)
    downloadglue.place(x=30, y=390)
    downloadtask.place(x=30, y=510)

start()
apptk.mainloop()
