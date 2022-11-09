
import numbers
import tkinter as tk
from tkinter import *
from tkinter import ttk
import wargameChoises as wgc

maxRowlen = 2

maps = wgc.loadMaps()
factions,specialisations = wgc.loadCountries()
constrictChoices = {"Coalitions"            : 1,
                    "Banned Specialisations":["Support"],
                    "Banned Countires"      :[],
                }


root = Tk()
root.title("Wargame RD Match roller")
frm = ttk.Frame(root, padding=10)
frm.grid()
playercountField = tk.IntVar() #TODO does not get updated?
def layoutInputs():
    ttk.Label(frm, text="Amount of Players").grid(column=0, row=0)
    entryPlayercountField = ttk.Entry(frm,textvariable=playercountField,text = "Players ?",width=5).grid(column=1, row=0)
    ttk.Label(frm, text=playercountField.get()).grid(column=2, row=0)
def layout(maxRowlength):
    ttk.Button(frm, text="Roll Dice", command=runScript).grid(column=0, row=maxRowlength)
    ttk.Button(frm, text="Quit",   command=root.destroy).grid(column=1, row=maxRowlength)    
def updateTTk(playercount,maxRowlength):
    constrictChoices.update({"Banned Specialisations": ["Support"]}) #Todo Make not static
    rowMap = 1
    ttk.Label(frm, text="Map").grid(column=0, row=rowMap)
    map = wgc.rollmap(maps,playercount=playercount)
    ttk.Label(frm, text=(map["Name"]+" | "+map["Type"])).grid(column=1, row=rowMap)
    
    rowPlayer = 3
    players=wgc.rollplayers(factions,specialisations,constrictChoices,playercount=playercount)
    print(players)
    for i,p in enumerate(players):
        ttk.Label(frm, text=("Player",i+1,":")).grid(                         column=0, row=i+rowPlayer)
        ttk.Label(frm, text=(p["Name"]+" | "+p["Side"]+" | "+p["Type"])).grid(column=1, row=i+rowPlayer)
        maxRowlength = maxRowlength+1
    maxRowlength = maxRowlength+2
    layout(maxRowlength=maxRowlength)
def runScript():
    playercount = playercountField.get()  
    print(playercount)
    for widget in frm.winfo_children():
        widget.destroy()
    #layoutInputs()
    updateTTk(playercount=2,maxRowlength=maxRowlen)
 
layout(maxRowlen)
root.mainloop()