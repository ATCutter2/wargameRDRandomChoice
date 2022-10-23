
import fractions
import numpy as np
import random
import pandas as pd
import math
#Changable Variables
#playercount = 2
#enableCoalitions = 1
#END Changable Variables


#Load Maps

def loadMaps() :
    maps  = pd.read_csv('WargameRDMaps.csv',delimiter=";",index_col=0)

def rollmap(playercount=2):
    maps = maps[maps["Players per Side"] >= (math.floor(playercount/2))]        
    map = random.choice(maps)
    return map
    
#Load Countries
colummnamesFactionlist = []
specialisation = []
force = []
factions = []
def loadCountries():
    factions= pd.read_csv('Factionlist.csv',delimiter=";",index_col=0)
    specialisations = factions.columns[2:]
    for sp in specialisations:
        
    
  #      reader = csv.reader(infile,delimiter=';')
  #      line_count = 0
  #      for i,rows in enumerate(reader): 
  #          if i == 0:
  #              colummnamesFactionlist.extend(rows[:])
  #              for spec in range(3,len(rows)):
  #                  specialisation.append(rows[spec])    
  #              continue
  #          else:
  #              force.append({"faction":rows[0],
  #                            "isCoalition":rows[1],
  #                            "Coalition":rows[2],
  #                            "specialisation":rows[3:]})
  #  for f in force:
  #      if f["faction"] not in factions:
  #          factions.append(f["faction"])

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