
import numbers
import tkinter as tk
from tkinter import *
from tkinter import ttk
import wargameChoises as wgc

maxRowlen = 2

wgc.loadMaps()
wgc.loadCountries()



root = Tk()
root.title("Wargame RD Match roller")
frm = ttk.Frame(root, padding=10)
frm.grid()
playercountField = tk.IntVar() #TODO does not get updated?

def runScript():
    players = playercountField.get()  
    print(players)
    
def wgcStuff(players):
    if players < 2:
        players = 2
    wgc.rollmap(players)
    wgc.initializePlayers(players)
    wgc.addAllowedCountires()
    updateTTk()
    
def updateTTk():
    ttk.Label(frm, text="Map").grid(column=0, row=0)
    map = wgc.rollmap(2)
    ttk.Label(frm, text=(map["Name"],map["Size(Given)"],map["Type"])).grid(column=1, row=0)
    for i,player in enumerate(wgc.players):
        ttk.Label(frm, text=("Player",i+1,":")).grid(column=0, row=i+1)
        ttk.Label(frm, text=(player)).grid(column=1, row=i+1)
        maxRowlen = maxRowlen+1

ttk.Label(frm, text="Amount of Players").grid(column=0, row=0)
entryPlayercountField = ttk.Entry(frm,textvariable=playercountField,text = "Players ?",width=5).grid(column=1, row=0)
ttk.Label(frm, text=playercountField.get()).grid(column=2, row=0)


ttk.Button(frm, text="Roll Dice", command=runScript).grid(column=0, row=maxRowlen)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=maxRowlen)
root.mainloop()