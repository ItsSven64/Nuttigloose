import tkinter as tk
from PIL import ImageTk

def init():
    # Load assets
    global ScreenList
    global frm
    global taskroot
    global background
    global balk
    global windowknop
    global wordroot
    global symbollist
    global string
    global clear
    global symbol
    symbol = ''
    string = ""
    clear = False
    symbollist = ["Type Here!"]
    wordroot = tk.Tk()
    wordroot.geometry("1250x700")
    wordroot.resizable(True, True)
    wordroot.bind('<KeyRelease>', key_press)
    background = ImageTk.Image.open("../Images/WindowsILL background.jpg")
    background = background.resize((500, 500))
    background = ImageTk.PhotoImage(background)

def key_press(event):
    global clear
    global symbollist
    symbol = event.keysym
    match symbol:
        case 'BackSpace':
            symbol = ''
            symbollist.pop()
        case 'space':
            symbol = ' '
        case 'Return':
            clear = True
        case 'period':
            symbol = '.'

    symbollist = symbollist.append(symbol)
    string = str(symbollist)
    display = tk.Label(wordroot, text=symbollist)
    display.place(x=0, y=10)
    print(string)
    print("Been here")
if __name__ == '__main__':
    init()
    wordroot.mainloop()