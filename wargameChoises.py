
import fractions
from multiprocessing.sharedctypes import Value
from secrets import choice
from xmlrpc.client import Boolean
import numpy as np
import random
import pandas as pd
import math
#Changable Variables
#constrictChoices = {"Coalitions"            : 1,
#                    "Banned Specialisations":[],
#                    "Banned Countires"      :[],
#                    }
#END Changable Variables

#Load Maps
def loadMaps() -> pd.DataFrame :
    maps =  pd.read_csv('WargameRDMaps.csv',delimiter=";",index_col=0)
    #maps.columns = maps.columns.str.strip() #Remove Trailing whitespaces
    return maps
def rollmapRaw(maps: pd.DataFrame, playercount=2) ->pd.DataFrame:
    validmaps = maps[maps["Players per Side"] >= (math.floor(playercount/2))]        
    map = validmaps.sample()
    return map
def rollmap(maps: pd.DataFrame, playercount=2):
    map = rollmapRaw(maps, playercount=playercount)
    return {"Name":map.index.values[0].strip(),
            "Type":map["Type"].values[0]
            }
#Load Countries
def loadCountries(filepath = 'Factionlist.csv'):
    factions= pd.read_csv(filepath,delimiter=";",index_col=0)
    specialisations = factions.columns[2:]
    return (factions,specialisations)

# functions for selection
def rollFaction(factions,specialisations):
    specialisation = random.choice(specialisations)
    faction        = factions.sample()
    return{"faction"         :faction,
           "specialisation"  :specialisation
          }
def validFaction(faction: pd.DataFrame,constrictChoices):
    eval = faction["faction"].iloc[:,0] not in constrictChoices["Banned Countires"] #Compare names in column Faction of csv
    #print(faction["specialisation"],constrictChoices["Banned Countires"],eval)
    return eval
def validSpecialisation(faction,constrictChoices):
    eval = not(any(x in faction["specialisation"]for x in constrictChoices["Banned Specialisations"]))
    #print(faction["specialisation"],constrictChoices["Banned Specialisations"],eval)
    return eval    
def selectRoll(factions:pd.DataFrame,specialisations:pd.DataFrame,constrictChoices):
    faction = factions[factions["is Coalition"] <= constrictChoices["Coalitions"]] #limit if coalitions not allowed
    #Make chance to get a side 50-50
    sides = faction.drop_duplicates("Side")
    side = sides.sample()
    side = side["Side"]
    
    choiceNotValid = True
    while choiceNotValid:
        faction   = rollFaction(factions,specialisations)                #Give a first suggestion
        
        vFactions = validFaction(faction,constrictChoices)               #is it a allowed country?
        vSpeciali = validSpecialisation(faction,constrictChoices)        #is it a allowed Specialisation?
        vSide     = (faction["faction"].values[0,0]) == (side.values[0]) #is the selected side?
        choiceNotValid = not(vFactions or vSpeciali or vSide)            #reroll if not within cirteria
        #print(choiceNotValid,vFactions,vSpeciali,vSide)
    return faction
def rollplayersRaw(factions,specialisations,constrictChoices,playercount=2):
    players = []
    for i in range(0,playercount):
        players.append(selectRoll(factions,specialisations,constrictChoices))
    return players
def rollplayers(factions,specialisations,constrictChoices,playercount=2):
    players = rollplayersRaw(factions,specialisations,constrictChoices,playercount=playercount)
    pl = []
    for p in players:
        #print(p["faction"],p["specialisation"])
        pl.append({ "Name":p["faction"].index.values[0].strip(),
                    "Side":p["faction"].values[0,0].strip(),
                    "Type":p["specialisation"].strip()
                    } )
    #print(pl)
    return pl                      

if __name__ == "__main__":
    constrictChoices = {"Coalitions"            : 1,
                        "Banned Specialisations":[""],
                        "Banned Countires"      :[],
                    }
    maps = loadMaps()
    factions,specialisations = loadCountries() 
    
    map = rollmap(maps,playercount=2) 
    constrictChoices.update({"Banned Specialisations": ["Support"]})
    players=rollplayers(factions,specialisations,constrictChoices,playercount=2)
    
    print(map["Name"],map["Type"],sep=" | ")
    for i,p in enumerate(players):
        print("Player",i+1,":",p["Name"],p["Side"],p["Type"])
