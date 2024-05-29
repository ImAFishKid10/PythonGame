# Imports
from tkinter import *
import tkinter as tk
import datetime
import math

start = datetime.datetime.now()
# Window and window config
window = tk.Tk()
window.title("GUI")
window.geometry("600x600")

# General game variables
number = 0
clickPower = 1
cps = 0

# Struct variables
sprice1 = 10
sincrement1 = 1
structCount1 = 0
sprice2 = 100
sincrement2 = 10
structCount2 = 0

# Upgrade variables
uprice1 = 50
upgradeCount1 = 0


# Updates text when button is clicked
def click():
    global number, clickPower
    number += clickPower
    score["text"] = str(number) + " CO2"


# Struct functions: Upgrades the structs and increases the price of given struct
def struct1():
    global number, cps, structCount1, sincrement1, sprice1
    if number >= sprice1:
        number -= sprice1
        sprice1 += int(sincrement1)
        sincrement1 += (sincrement1 * 1.3) - sincrement1
        score["text"] = str(number) + " CO2"
        cps += 0.1
        structCount1 += 1
        structButton1["text"] = "Offset/s struct: " + str(sprice1) + " CO2 (" + str(structCount1) + ")"


def struct2():
    global number, cps, structCount2, sincrement2, sprice2
    if number >= sprice2:
        number -= sprice2
        sprice2 += int(sincrement2)
        sincrement2 += (sincrement2 * 2.1) - sincrement2
        score["text"] = str(number) + " CO2"
        cps += 1
        structCount2 += 1
        structButton2["text"] = "Offset/s struct: " + str(sprice2) + " CO2 (" + str(structCount2) + ")"


# Upgrade functions: Upgrades the given thing and increases the price of given upgrade
def upgrade1():
    global number, clickPower, uprice1, upgradeCount1
    if number >= uprice1:
        number -= uprice1
        clickPower += 1
        uprice1 += (uprice1 * 5) - uprice1
        upgradeCount1 += 1
        upgradeButton1["text"] = "Click power upgrade: " + str(uprice1) + " CO2 (" + str(upgradeCount1) + ")"


def idle():
    global number, cps, window, structCount1
    cps = round(cps, 1)
    number += cps
    number = round(number, 1)
    displayNumber = math.floor(number)
    print(number)
    print(displayNumber)
    placeButtons()
    window.after(1000, idle)
    score["text"] = str(number) + " CO2"
    perSecond["text"] = str(cps) + " Offset/s"
    placeButtons()


def placeButtons():
    global number
    if number >= 10:
        structButton1.place(x=400)
    if number >= 100:
        structButton2.place(x=400, y=20)
    if structCount1 == 10:
        upgradeButton1.place(x=33)


# Struct buttons
structButton1 = Button(window, text="Offset/s struct: 10 CO2 (0)", command=struct1)
structButton2 = Button(window, text="Offset/s struct: 100 CO2 (0)", command=struct2)

# Upgrade buttons
upgradeButton1 = Button(window, text="Click power upgrade: 50 CO2 (0)", command=upgrade1)

# Score text
score = Label(window, text="0 CO2", font="Helvetica, 20", padx=20, pady=50)
score.pack()

perSecond = Label(window, text="0 Offset/s", font="Helvetica, 20", padx=20, pady=10)
perSecond.pack()

# Clicker button
button1 = Button(window, command=click)
button1.place(x=275, y=100, width=50, height=50)

idle()
window.mainloop()
