import math
from re import A
from sympy import *
import random

WeatherList = ["Clear","Sandstorm","Hail","Fog","ShadowyAura","Rain","Sunny"]
PkmnName = input("Name of the Pokemon: ")
PkmnLevel = int(input("What is your Pokemon's Level: "))
UserPokemonType1 = input("Input Pokemon's First Type: ")
UserPokemonType2 = input("Input Pokemon's Second Type (type 'n' if none): ")
    
UserPokemonTypeList = [UserPokemonType1,UserPokemonType2]

MoveName = input("Name of move: ")
MoveType = input("Type of move: ")
Burn = 0
BurnStat = (input("Is your pokemon under BURN status? Y/N: "))
if BurnStat == 'Y' or 'y':
    Burn == 0.5
elif BurnStat == 'N' or 'n':
    Burn == 1
NoOfTargets = int(input("Number of enemies: "))
if NoOfTargets == 1:
    Targets = 1
elif NoOfTargets > 1:
    Targets = 0.5
WeatherType = input("Weather condition(Clear/Sunny/Rain/Sandstorm/Hail/Shadowy Aura/Fog): ")
Weather = 0
if WeatherType == "Sunny" and MoveType == "Fire":
        Weather = 1.5
elif WeatherType == "Sunny" and MoveType == "Water":
        Weather = 0.5
elif WeatherType == "Rain" and MoveType == "Water":
        Weather = 1.5
elif WeatherType == "Rain" and MoveType == "Fire":
        Weather = 0.5
elif any(WeatherType in s for s in WeatherList):
        Weather = 1
else:
    print("Weather Type Unknown! Result will be 0")
Badge = 1
Critical = 2
rendom = random.uniform(0.85,1.00)

if any(MoveType in s for s in UserPokemonTypeList):
    STAB = 1.5
else:
    STAB = 1
    
Type = 2
modifier = Targets * Weather * Badge * Critical * rendom * STAB * Type * Burn * Other
Damage = ((((((2*PkmnLevel)/5)+2)*(110)*(205/180))/50)+2) * modifier
print(round(Damage))
print(Weather)
print(Targets)
print(UserPokemonTypeList)
print(STAB)


