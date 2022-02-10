import os

import random
import tkinter as ttk
from time import time, sleep
import string


def delay(total, dev):
    if not dev:
        StrtMs = time()
        while True:
            print("")
            if (time() - StrtMs) >= total: break

def letsmove(root, dev):
    if not dev:
        list = [25, 50, 100, 200, 500, -500, -200, -100, -50, -25]
        choice1 = random.choice(list)
        choice2 = random.choice(list)
        argument = ("+"+str(choice1)+"+"+str(choice2))
        root.geometry(argument)
