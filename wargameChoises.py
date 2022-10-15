
import numpy as np
import random
import csv
import math
#Changable Variables
playercount = 2
enableCoalitions = 1
#END Changable Variables

forces = ["Redfor","Bluefor"]
maps1v1Legacy= [
            "(1v1) Tropic Thunder            ",
            "(1v1) Mud Fight !               ",
            "(1v1) Nuclear Winter is Coming  ",
            "(1v1) Wonsan Harbour            ",
            "(1v1) Plunjing Valley           ",
            "(1v1) Death Row                 ",
            "(1v1) Paddy Field               ",
            "(1v1) Punchbowl                 ",
            "(1v1) Hell in a very small place",
            "(1v1) Strait to the Point       ",
            "(1v1 Mixed) Wonsan Harbour      ",
            "(2v2) Highway to Seoul          ",
            "(4v4) Cold War Z                ",
            "(4v4 Mixed) Smoke in the water  "
            ]

#Load Maps
maps1v1 = []
enumPvPNumbers = ["(1v1)"]
colummnamesMaps = []
with open('WargameRDMaps.csv', mode='r') as infile:
    reader = csv.reader(infile,delimiter=';')
    line_count = 0
    for i,rows in enumerate(reader): 
        if i == 0:
            colummnamesMaps.append(rows[:])
        else:
            if rows[1] == enumPvPNumbers[math.floor(playercount/2)-1]:
                maps1v1.append({"Name":rows[0],
                                "Size(usable as)":rows[1],
                                "Size(Given)":rows[2],
                                "Type":rows[3:]})

#Load Countries
colummnames = []
specialisation = []
force = []
with open('Factionlist.csv', mode='r') as infile:
    reader = csv.reader(infile,delimiter=';')
    line_count = 0
    for i,rows in enumerate(reader): 
        if i == 0:
            colummnames.append(rows[:])
            for spec in range(3,len(rows)):
                specialisation.append(rows[spec])    
            continue
        else:
            force.append({"faction":rows[0],
                          "isCoalition":rows[1],
                          "Coalition":rows[2],
                          "specialisation":rows[3:]})


#Initialize players
players = []
for i in range(0,playercount):
    specialisationNr = specialisation.index(random.choice(specialisation))
    faction = random.choice(forces)
    players.append({"faction":faction,
                    "specialisation":specialisation[specialisationNr],
                    "specialisationNr":specialisationNr}
                   )

#add allowed lands
for i,p in enumerate(players):
   #find allowed Countries
    elligiblefactions = []
    for forc in force:
        if forc["faction"] == p["faction"]:
            if forc["specialisation"][p["specialisationNr"]] == '1':
                elligiblefactions.append((forc["Coalition"],forc["specialisation"]))
    if len(elligiblefactions) >0 :
        p.update({"Coalition":random.choice(elligiblefactions)})
    else :
        print("error no elligible factions")
    #for e in elligiblefactions:
    #    print(" ",e)
    

if __name__ == "__main__":
    map = random.choice(maps1v1)
    print("map:",map["Name"],map["Size(Given)"],map["Type"])
    #print(specialisation)
    specializationArray = [0,0,0,0,0,0,0]
    for p in players:
        ##visualize what  colummn is chosen
        #choosenSpezialisation = specializationArray
        #choosenSpezialisation[p["specialisationNr"]] = 1
        #print("choosenSpezialisation",choosenSpezialisation) # this has problems with compilerside simplifications
        print("Player",i+1,":", p)
        print()