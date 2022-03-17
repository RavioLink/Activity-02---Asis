import math
from re import A
from sympy import *
import random

WeatherList = ["Clear","Sandstorm","Hail","Fog","ShadowyAura","Rain","Sunny"]
PkmnName = input("Name of the Pokemon: ")
PkmnLevel = int(input("What is your Pokemon's Level: "))
UserPokemonType1 = input("Input Pokemon's First Type: ")
UserPokemonType2 = input("Input Pokemon's Second Type (type 'n' if none): ")
ASpecial = int(input("Special Attack Stat: "))
EnemyPkmnName = input("Enemy Pokemon Name: ")
EnemyPkmnType1 = input("Enemy Pokemon Type 1: ")
EnemyPkmnType2 = input("Enemy Pokemon Type 2: ")
DDef = int(input("Special Defense of Enemy Pokemon: "))

PkmnTypeList = ["Fire","Ice","Water","Ground","Rock","Psychic","Ghost","Dark","Fairy","Steel","Grass","Fighting","Flying","Dragon","Bug","Poison","Electric","Normal"]
EnemyPkmnTypeList = [EnemyPkmnType1,EnemyPkmnType2]    
UserPokemonTypeList = [UserPokemonType1,UserPokemonType2]

MoveName = input("Name of move: ")
MoveType = input("Type of move: ")
Power = int(input("Power of attack: "))

BurnStat = input("Is your pokemon under BURN status? Y/N: ")
Burn = 0
if BurnStat == 'y' or BurnStat == 'Y':
    Burn = 0.5
elif BurnStat == 'n' or BurnStat == 'N':
    Burn = 1
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
    
Type = 0
if MoveType == "Fire" and (EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Bug" or EnemyPkmnType1 == "Steel"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Bug" or EnemyPkmnType2 == "Steel"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 1and (EnemyPkmnType2 == "Nullifier"):
        Type = 0
elif MoveType == "Fire" and (EnemyPkmnType1 == "Water" or EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Rock"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type = 0.25
elif MoveType == "Fire" and EnemyPkmnType1 == "Nullifier":
    Type = 0
elif MoveType not in PkmnTypeList:
    print("Invalid Type")

Other = 1
modifier = Targets * Weather * Badge * Critical * rendom * STAB * Type * Burn * Other
Damage = ((((((2*PkmnLevel)/5)+2)*(Power)*(ASpecial/DDef))/50)+2) * modifier
print(round(Damage))
print(Weather)
print(Targets)
print(UserPokemonTypeList)
print(STAB)
print(Type)
print(Burn)


