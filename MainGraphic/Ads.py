import os
import sys
import tkinter as tk
import random
from PIL import ImageTk
from googleads import ad_manager
from googleads import oauth2
from importlib import *


# Initialize the GoogleRefreshTokenClient using the credentials you received
# in the earlier steps.
oauth2_client = oauth2.GoogleServiceAccountClient(
    "windowsill-2d8fa575450a.json", oauth2.GetAPIScope('ad_manager'))

# Initialize the Ad Manager client.
ad_manager_client = ad_manager.AdManagerClient(oauth2_client, "WindowsIll")

def openad():
    global root
    global MILFAD
    sizeychoice = 300
    sizexchoice = 250
    sizechoice = (str(sizeychoice)+"x"+str(sizexchoice))
    namelist = ["Hotel Reduction!", "GET IT TODAY", "2 viruses detected, take action!", "Hot MILFS in your area!"]
    namechoice = random.choice(list(range(0, (len(namelist)))))
    root = tk.Tk()
    root.geometry(sizechoice)
    root.resizable(False, False)
    root.title(namelist[namechoice])
    os.chdir("..\Images")
    match namechoice:
        case 0:
            HOTELAD = ImageTk.PhotoImage(ImageTk.Image.open("RojalParck.png").resize((sizeychoice, sizexchoice)))
            tk.Label(image=HOTELAD).place(x=0, y=0)
        case 3:
            MILFAD = ImageTk.PhotoImage(ImageTk.Image.open("MILF-AD.png").resize((sizeychoice, sizexchoice)))
            tk.Label(image=MILFAD).place(x=0, y=0)
    root.mainloop()

if __name__ == '__main__':
    openad()
