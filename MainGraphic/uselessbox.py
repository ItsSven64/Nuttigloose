from tkinter import *
import tkinter as tk
import random

movable1 = 0
movable2 = 0
movable3 = 0
movable4 = 0
def useless():
    global boxroot
    global movable1
    global movable2
    global movable3
    global movable4
    boxroot = tk.Tk()
    boxroot.geometry("1000x502")
    boxroot.resizable(False, False)
    boxroot.configure(bg='#3197e0')
    target1()
    target2()
    target3()
    target4()
    boxroot.mainloop()


def target1():
    global target1
    target1 = tk.Button(boxroot, command=lambda: [no1(), sink1()], text="exit", bg="#FFB6C1")
    target1.place(x=0, y=0)

def target2():
    global target2
    target2 = tk.Button(boxroot,command=lambda:[no2(), sink2()], text="exit", bg="#FFFF99")
    target2.place(x=50, y=50)

def target3():
    global target3
    target3 = tk.Button(boxroot, command=lambda:[no3(), sink3()], text="exit", bg="#ADD8E6")
    target3.place(x=120, y=20)
def target4():
    global target4
    target4 = tk.Button(boxroot, command=lambda: [no4(), sink4()], text="exit", bg="#90EE90")
    target4.place(x=320, y=150)

def no1():
    if (movable1%2)==0:
        randomizer()
    else:
        boxroot.mainloop
def no2():
    if (movable2%2)==0:
        randomizer()
    else:
        boxroot.mainloop
def no3():
    if (movable3%2)==0:
        randomizer()
    else:
        boxroot.mainloop
def no4():
    if (movable4%2)==0:
        randomizer()
    else:
        boxroot.mainloop

def sink1():
    global movable1
    target1.config(relief=SUNKEN)
    if (movable1%2)==0:
        old1=movable1
        movable1=old1+1
def sink2():
    global movable2
    target2.config(relief=SUNKEN)
    if (movable2%2)==0:
        old2=movable2
        movable2=old2+1

def sink3():
    global movable3
    target3.config(relief=SUNKEN)
    if (movable3%2)==0:
        old3=movable3
        movable3=old3+1

def sink4():
    global movable4
    target4.config(relief=SUNKEN)
    if (movable4%2)==0:
        old4=movable4
        movable4=old4+1

def randomizer():
    global raise1
    global raise2
    global raise3
    global raise4
    global movable1
    global movable2
    global movable3
    global movable4
    raise1 = random.randint(1,1000)
    raise2 = random.randint(1,1000)
    raise3 = random.randint(1,1000)
    raise4 = random.randint(1,1000)
    maybewin= random.randint(1,10)
    if raise1 < 990 and (movable1%2)!=0:
        move1()
        old1=movable1
        movable1=old1+1
    if raise2 < 990 and (movable2%2)!=0:
        old2=movable2
        movable2=old2+1
        move2()
    if raise3 < 990 and (movable3%2)!=0:
        old3=movable3
        movable3=old3+1
        move3()
    if raise4 < 990 and (movable4%2)!=0:
        old4 = movable4
        movable4 = old4 + 1
        move4()
    if (movable1 % 2) != 0 and (movable2 % 2) != 0 and (movable3 % 2) != 0 and (movable4 % 2) != 0 and maybewin != 1:
        move1()
        move2()
        move3()
        move4()
        movable1=0
        movable2=0
        movable3=0
        movable4=0


def move1():
    target1.config(relief=RAISED)
    xlist1 = list(range(0, 900))
    ylist1 = list(range(20, 200))
    x1 = random.choice(xlist1)
    y1 = random.choice(ylist1)
    target1.place(x=x1, y=y1)


def move2():
    target2.config(relief=RAISED)
    xlist2 = list(range(0, 900))
    ylist2 = list(range(20, 200))
    x2 = random.choice(xlist2)
    y2 = random.choice(ylist2)
    target2.place(x=x2, y=y2)

def move3():
    target3.config(relief=RAISED)
    xlist3 = list(range(0, 900))
    ylist3 = list(range(20, 200))
    x3 = random.choice(xlist3)
    y3 = random.choice(ylist3)
    target3.place(x=x3, y=y3)

def move4():
    target4.config(relief=RAISED)
    xlist4 = list(range(0, 900))
    ylist4 = list(range(20, 200))
    x4 = random.choice(xlist4)
    y4 = random.choice(ylist4)
    target4.place(x=x4, y=y4)

if __name__ == '__main__':
    useless()