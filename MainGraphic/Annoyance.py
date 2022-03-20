import os

import requests
from plyer import notification

import random
import tkinter as tk
from PIL import ImageTk
from time import time, sleep
import string

"""Dit kan je overal gebruiken door <import MainGraphic.Annoyance> te doen"""

def delay(total, dev=False):
    if not dev:
        StrtMs = time()
        while True:
            print("")
            if (time() - StrtMs) >= total: break


def letsmove(root, dev=False):
    if not dev:
        list = [25, 50, 100, 200, 500, -500, -200, -100, -50, -25]
        choice1 = random.choice(list)
        choice2 = random.choice(list)
        argument = ("+" + str(choice1) + "+" + str(choice2))
        root.geometry(argument)

def webrape(total, dev=False):
    url = "https://www.smithfieldfoods.com"
    x = 0
    if not dev:
        while True:
            r = requests.get(url, allow_redirects=True)

            print(r)
            if x == total:
                break
            else:
                x = x + 1
                print(x)
        os.system("netsh interface set interface 'Wifi' disabled")


def ping(Title, Message, n, dev=False):
    if not dev:
        for x in range(n):
            notification.notify(
                title=Title,
                message=Message,
                app_icon=None,
                timeout=10,
            )

def flash(Seconds, pause):
    os.chdir("..\Images")
    adroot = tk.Tk()
    photoone = ImageTk.PhotoImage(ImageTk.Image.open("RojalParck.png").resize((200, 200)))
    phototwo = ImageTk.PhotoImage(ImageTk.Image.open("Onbetrouwbare ad hotelkamer Project Informatica 2.png").resize((200, 200)))
    ad1 = tk.Label(adroot, image=photoone)
    ad2 = tk.Label(adroot, image=phototwo)
    ad1.place(x=0, y=0)
    check = True
    ping("AANBIEDING!", "Bel 06-51108566 om een geweldige aanbieding te krijgen!", 1)
    while check:
        try:
            ad1.pack_forget()
            ad2.pack()
            adroot.update()
            sleep(pause)
            ad2.pack_forget()
            ad1.pack()
            adroot.update()
            sleep(pause)
        except:
            return

if __name__ == '__main__':
    flash(4, 0.1)