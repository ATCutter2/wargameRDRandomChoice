
import numbers
import tkinter
from tkinter import *
from tkinter import ttk
import wargameChoises as wgc

maxRowlen = 2

wgc.loadMaps()
wgc.loadCountries()
players = 0


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Amount of Players").grid(column=0, row=0)
playercountField = ttk.Entry(frm,textvariable=numbers).grid(column=1, row=0)

def runScript():
    players = int(playercountField.get())
    
    wgc.rollmap(players)
    wgc.initializePlayers(players)
    wgc.addAllowedCountires()
    updateTTk()
    
def updateTTk():
    ttk.Label(frm, text="Map").grid(column=0, row=0)
    ttk.Label(frm, text=(wgc.map["Name"],wgc.map["Size(Given)"],wgc.map["Type"])).grid(column=1, row=0)
    for i,player in enumerate(wgc.players):
        ttk.Label(frm, text=("Player",i+1,":")).grid(column=0, row=i+1)
        ttk.Label(frm, text=(player)).grid(column=1, row=i+1)
        maxRowlen = maxRowlen+1

ttk.Button(frm, text="Roll Dice", command=runScript()).grid(column=0, row=maxRowlen)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=maxRowlen)
root.mainloop()