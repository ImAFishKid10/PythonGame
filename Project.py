# Imports
from tkinter import *
import tkinter as tk
import math
# Window and window config
window = tk.Tk()
window.title("GUI")
window.geometry("800x800")

# General game variables
number = 0
clickPower = 1
cps = 0
displayNumber = 0

# Struct variables
sprice1 = 15
structCount1 = 0
structPower1 = 0.1
sprice2 = 100
structCount2 = 0
structPower2 = 1

# Upgrade variables
uprice1 = 100
upgradeCount1 = 0


# Updates text when button is clicked
def click():
    global number, clickPower, displayNumber
    number += clickPower
    updateUI()


# Struct functions: Upgrades the structs and increases the price of given struct
def struct1():
    global number, cps, structCount1, sprice1, displayNumber
    if number >= sprice1:
        number -= sprice1
        structCount1 += 1
        sprice1 = int(15 * 1.15 ** structCount1)
        updateUI()



def struct2():
    global number, cps, structCount2, sprice2, displayNumber
    if number >= sprice2:
        number -= sprice2
        structCount2 += 1
        sprice2 = int(100 * 1.15 ** structCount2)
        updateUI()


# Upgrade functions: Upgrades the given thing and increases the price of given upgrade
def upgrade1():
    global number, clickPower, uprice1, upgradeCount1, displayNumber, structPower1
    if number >= uprice1:
        number -= uprice1
        clickPower += 1
        structPower1 = structPower1 * 2
        uprice1 += (uprice1 * 5) - uprice1
        upgradeCount1 += 1
        updateUI()


def idle():
    global number, cps, window, structCount1, displayNumber
    cps = round(cps, 1)
    number += cps
    number = round(number, 1)
    window.after(1000, idle)
    updateUI()
    placeButtons()


def placeButtons():
    global number
    if number >= 15:
        structButton1.place(x=600)
    if number >= 100:
        structButton2.place(x=600, y=30)
    if structCount1 == 1:
        upgradeButton1.place(x=33)


def updateUI():
    global displayNumber, cps, number, structCount2, structCount1, structPower1, structPower2
    placeButtons()
    cps = (structCount1 * structPower1) + (structCount2 * structPower2)
    cps = round(cps, 1)
    number = round(number, 1)
    displayNumber = math.floor(number)
    score["text"] = str(displayNumber) + " CO2"
    structButton1["text"] = "Offset/s struct: " + str(sprice1) + " CO2 (" + str(structCount1) + ")"
    structButton2["text"] = "Offset/s struct: " + str(sprice2) + " CO2 (" + str(structCount2) + ")"
    perSecond["text"] = str(cps) + " Offset/s"
    upgradeButton1["text"] = "Click power upgrade: " + str(uprice1) + " CO2 (" + str(upgradeCount1) + ")"


# Score text
score = Label(window, text="0 CO2", font="Helvetica, 20", padx=20, pady=20)
score.pack()

# Clicker button
button1 = Button(window, command=click, pady=15, padx=20)
button1.pack()

# CO2/s
perSecond = Label(window, text="0 Offset/s", font="Helvetica, 20", padx=20, pady=0)
perSecond.pack()

# Struct buttons
structButton1 = Button(window, text="Offset/s struct: 10 CO2 (0)", command=struct1)
structButton2 = Button(window, text="Offset/s struct: 100 CO2 (0)", command=struct2)

# Upgrade buttons
upgradeButton1 = Button(window, text="Click power upgrade: 50 CO2 (0)", command=upgrade1)

idle()
window.mainloop()
