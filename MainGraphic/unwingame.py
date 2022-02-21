import os
import tkinter as tk
import random
from PIL import ImageTk

import time
import MainGraphic.Annoyance as ay

def gameinit():
    global counter
    global root
    global target
    global clickedtime
    global timer
    global responsetime
    global recordtime
    global targetimg
    try:
        os.chdir(os.path.join((os.getcwd()), 'MainGraphic'))
    except FileNotFoundError:
        pass
    counter = 0
    root = tk.Tk()
    root.geometry("1000x250")
    root.resizable(False, False)
    targetimg = ImageTk.Image.open("../Images/target(100x100).png")
    targetimg = ImageTk.PhotoImage(targetimg)
    tk.Button(command=lose, height=250, width=1000).place(x=0, y=0)
    target = tk.Button(root, image=targetimg, command=move)
    target.place(x=0, y=0)
    clickedtime = time.time()
    responsetime = 100
    recordtime = 999
    timer = tk.Label(root, text="0")


def move():
    global counter
    global oldtime
    global clickedtime
    global timer
    global responsetime
    global oldresptime
    global recordtime
    oldtime = clickedtime
    clickedtime = time.time()
    oldresptime = responsetime
    responsetime = round((clickedtime - oldtime), 2)
    if responsetime < recordtime:
        recordtime = responsetime
        record = tk.Label(root, text=recordtime)
        record.place(x=550, y=0)
    else:
        lose()
    xlist = list(range(0, 900))
    ylist = list(range(20, 200))
    x = random.choice(xlist)
    y = random.choice(ylist)
    target.place(x=x, y=y)
    counter = counter + 1
    tk.Label(root, text=counter).place(x=490, y=0)
    timer.lower()
    timer = tk.Label(root, text=responsetime)
    timer.place(x=510, y=0)

def lose():
    tk.Label(root, text="You lost!").place(x=400, y=100)
    ay.delay(5)
    exit()

if __name__ == '__main__':
    gameinit()
    root.mainloop()
