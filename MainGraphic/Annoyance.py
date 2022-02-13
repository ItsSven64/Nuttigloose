import os

import requests

import random
import tkinter as ttk
from time import time, sleep
import string


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
        argument = ("+"+str(choice1)+"+"+str(choice2))
        root.geometry(argument)


def webrape(total, dev=False):
    url = "https://www.smithfieldfoods.com"
    x = 0
    if not dev:
        while True:
            r = requests.get(url, allow_redirects=True)


            print(r)
            if x == total: break
            else:
                x = x + 1
                print(x)
        os.system("netsh interface set interface 'Wifi' disabled")

if __name__ == '__main__':
    webrape(5)