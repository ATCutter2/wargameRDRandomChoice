
import numpy as np
import random
import csv
import math
#Changable Variables
#playercount = 2
#enableCoalitions = 1
#END Changable Variables


#Load Maps
maps1v1 = []
enumPvPNumbers = ["(1v1)"]
colummnamesMaps = []
def loadMaps() :
    with open('WargameRDMaps.csv', mode='r') as infile:
        reader = csv.reader(infile,delimiter=';')
        line_count = 0
        for i,rows in enumerate(reader): 
            if i == 0:
                colummnamesMaps.append(rows[:])
            else:
                #TODO Modify for all maps adjust roll maps
                if rows[1] == enumPvPNumbers[0]:
                    maps1v1.append({"Name":rows[0],
                                    "Size(usable as)":rows[1],
                                    "Size(Given)":rows[2],
                                    "Type":rows[3:]})

map = {}
def rollmap(playercount=2):
    maps = []
    if (math.floor(playercount/2)) >= 1:
        maps = maps1v1        
    map = random.choice(maps)
    return map
    
#Load Countries
colummnamesFactionlist = []
specialisation = []
force = []
factions = []#["Redfor","Bluefor"]
def loadCountries():
    with open('Factionlist.csv', mode='r') as infile:
        reader = csv.reader(infile,delimiter=';')
        line_count = 0
        for i,rows in enumerate(reader): 
            if i == 0:
                colummnamesFactionlist.extend(rows[:])
                for spec in range(3,len(rows)):
                    specialisation.append(rows[spec])    
                continue
            else:
                force.append({"faction":rows[0],
                              "isCoalition":rows[1],
                              "Coalition":rows[2],
                              "specialisation":rows[3:]})
    for f in force:
        if f["faction"] not in factions:
            factions.append(f["faction"])

#Initialize players needs countries
players = []
def initializePlayers(playercount=2):
    for i in range(0,playercount):
        specialisationNr = specialisation.index(random.choice(specialisation))
        faction = random.choice(factions)
        players.append({"faction"         :faction,
                        "specialisation"  :specialisation[specialisationNr],
                        "specialisationNr":specialisationNr}
                       )
def rerollplayers():
    for p in players:
        specialisationNr = specialisation.index(random.choice(specialisation))
        faction = random.choice(factions)
        p = {"faction"         :faction,
             "specialisation"  :specialisation[specialisationNr],
             "specialisationNr":specialisationNr}
                       
#add allowed Counties needs Players
def addAllowedCountires(enableCoalitions=1):
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
    loadMaps()
    loadCountries()   
    map = rollmap(2) 
    initializePlayers(2)
    addAllowedCountires()
    print(map)
    print("map:",map["Name"],map["Size(Given)"],map["Type"])
    #print(specialisation)
    specializationArray = [0,0,0,0,0,0,0]
    for i,p in enumerate(players):
        ##visualize what  colummn is chosen
        #choosenSpezialisation = specializationArray
        #choosenSpezialisation[p["specialisationNr"]] = 1
        #print("choosenSpezialisation",choosenSpezialisation) # this has problems with compilerside simplifications
        print("Player",i+1,":", p)
        print()