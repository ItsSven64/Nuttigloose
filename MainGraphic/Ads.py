import tkinter as tk
import random

def openad():
    global root
    sizexlist = list(range(200,500))
    sizeylist = list(range(400, 1000))
    sizechoice = (str(random.choice(sizeylist))+"x"+str(random.choice(sizexlist)))
    namelist = ["BUY NOW!", "GET IT TODAY", "2 viruses detected, take action!", "Hot MILFS in your area!"]
    namechoice = random.choice(list(range(len(namelist))))
    root = tk.Tk()
    root.geometry(sizechoice)
    root.resizable(False, False)
    root.title(namelist[namechoice])


if __name__ == '__main__':
    openad()
    root.mainloop()