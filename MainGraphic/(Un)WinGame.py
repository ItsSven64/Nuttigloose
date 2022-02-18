import os
import tkinter as tk
import random

import time

def init():
    global counter
    global root
    global target
    global clickedtime
    global timer
    global responsetime
    global recordtime
    os.chdir(os.path.join((os.getcwd()), 'MainGraphic'))
    print(os.getcwd())
    counter = 0
    root = tk.Tk()
    root.geometry("1000x250")
    root.resizable(False, False)
    targetimg = tk.PhotoImage(file="../Images/target(100x100).png")
    target.place(x=1, y=5)
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


if __name__ == '__main__':
    init()
    root.mainloop()
