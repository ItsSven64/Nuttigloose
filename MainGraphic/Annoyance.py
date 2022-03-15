import os

import requests
from plyer import notification

import random
import tkinter as ttk
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

def flash(photo1, photo_object, photo2, Seconds, time):
    xCord = photo_object.place_info()
    yCord = photo_object.place_info()
    photo1.place(x=xCord, y=yCord)
    check = True
    counter = 0
    while check:
        photo2.place(x=xCord, y=yCord)
        time.sleep(time)
        photo1.place(x=xCord, y=yCord)
        time.sleep(time)
        counter = counter + time*2
        if counter == Seconds:
            check = False

def flash(photo1, photo_object, photo2, Seconds, time):
    xCord = photo_object.place_info()
    yCord = photo_object.place_info()
    photo1.place(x=xCord, y=yCord)
    check = True
    counter = 0
    while check:
        photo2.place(x=xCord, y=yCord)
        time.sleep(time)
        photo1.place(x=xCord, y=yCord)
        time.sleep(time)
        counter = counter + time * 2
        if counter == Seconds:
            check = False

if __name__ == '__main__':
    ping("HEY", ':D', 10)