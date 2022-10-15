
import numbers
import tkinter as tk
from tkinter import *
from tkinter import ttk
import wargameChoises as wgc

maxRowlen = 4

wgc.loadMaps()
wgc.loadCountries()
wgc.initializePlayers(2)


root = Tk()
root.title("Wargame RD Match roller")
frm = ttk.Frame(root, padding=10)
frm.grid()
playercountField = tk.IntVar()

def runScript():
    map = wgc.rollmap(2)
    ttk.Label(frm, text=(map["Name"],map["Size(Given)"],map["Type"])).grid(column=1, row=0)
    
    wgc.rerollplayers()
    wgc.addAllowedCountires()
    for i,player in enumerate(wgc.players):
        ttk.Label(frm, text=("Player",i+1,":")).grid(column=0, row=i+2)
        ttk.Label(frm, text=(player)).grid(column=1, row=i+2)
    


ttk.Label(frm, text="Amount of Players").grid(column=0, row=0)

ttk.Label(frm, text=playercountField.get()).grid(column=2, row=0)
ttk.Label(frm, text="Map").grid(column=1, row=0)


#ttk.Label(frm, text=txtP1).grid(column=0, row=i+1)
#ttk.Label(frm, text=(player)).grid(column=1, row=i+1)

ttk.Button(frm, text="Roll Dice", command=runScript).grid(column=0, row=maxRowlen)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=maxRowlen)
root.mainloop()