import os

import psutil
from prettytable import PrettyTable

import random
from time import *
from random import *

import PIL.ImageOps
from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk

import Annoyance as ay


def init():
     # Load assets
    global ScreenList
    global frm
    global root
    global background
    global balk
    global windowknop
    root = Tk()
    root.geometry("500x502")
    root.resizable(False, False)
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
    btn1 = ttk.Button(text='Click to get current programs!', command=on_click, width=30)
    btn1.pack()
    btn1.place(x=50, y=250)


if __name__ == '__main__':
    init()
    start()
    root.mainloop()

def on_click():
 
    call('delete')
     
    print("Taak beheer")
 
    # Fetch the Network information
    print("Netwerk")
    table = PrettyTable(['Network', 'Status', 'Speed'])
    for key in psutil.net_if_stats().keys():
        name = key
        up = "Up" if psutil.net_if_stats()[key].isup else "Down"
        speed = psutil.net_if_stats()[key].speed
        table.add_row([name, up, speed])
    print(table)
 
    print("Geheugen")
    memory_table = PrettyTable(["Total", "Used",
                                "Available", "Percentage"])
    vm = psutil.virtual_memory()
    memory_table.add_row([
        vm.total,
        vm.used,
        vm.available,
        vm.percent
    ])
    print(memory_table)
     

    print("Processen")
    process_table = PrettyTable(['PID', 'PNAME', 'STATUS',
                                 'CPU', 'NUM THREADS'])
     
    for process in psutil.pids()[-10:]:
 
        try:
            p = psutil.Process(process)
            process_table.add_row([
                str(process),
                p.name(),
                p.status(),
                str(p.cpu_percent())+"%",
                p.num_threads()
                ])
             
        except Exception as e:
            pass
    print(process_table)
 
    time.sleep(0.5)