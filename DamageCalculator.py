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
CritChoice = [1,2]
Critical = random.choice(CritChoice)
rendom = random.uniform(0.85,1.00)

if any(MoveType in s for s in UserPokemonTypeList):
    STAB = 1.5
else:
    STAB = 1
    
Type = 1
if MoveType == "Fire" and (EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Bug" or EnemyPkmnType1 == "Steel"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Bug" or EnemyPkmnType2 == "Steel"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Fire" and (EnemyPkmnType1 == "Water" or EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Rock"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Bug" or EnemyPkmnType2 == "Steel"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Fire" and EnemyPkmnType1 == "Nullifier":
    Type = 0


if MoveType == "Grass" and (EnemyPkmnType1 == "Water" or EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Rock"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Poison" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Bug"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Grass" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Poison" or EnemyPkmnType1 == "Flying" or EnemyPkmnType1 == "Bug"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Poison" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Bug"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Grass" and EnemyPkmnType1 == "Nullifier":
    Type = 0
    
if MoveType == "Rock" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Flying" or EnemyPkmnType1 == "Bug"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Bug"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Steel"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Rock" and (EnemyPkmnType1 == "Water" or EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Fight" or EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Steel"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Steel"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Bug"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Rock" and EnemyPkmnType1 == "Nullifier":
    Type = 0

if MoveType == "Ice" and (EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Flying" or EnemyPkmnType1 == "Dragon"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Dragon"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Rock" or EnemyPkmnType2 == "Steel"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Ice" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Fight" or EnemyPkmnType1 == "Rock" or EnemyPkmnType1 == "Steel"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Rock" or EnemyPkmnType2 == "Steel"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Dragon"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Ice" and EnemyPkmnType1 == "Nullifier":
    Type = 0
    
if MoveType == "Dragon" and (EnemyPkmnType1 == "Dragon"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Ice"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Dragon" and (EnemyPkmnType1 == "Ice"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Dragon" and EnemyPkmnType1 == "Nullifier":
    Type = 0

if MoveType == "Dark" and (EnemyPkmnType1 == "Psychic" or EnemyPkmnType1 == "Ghost"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Psychic" or EnemyPkmnType2 == "Ghost"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Bug"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Dark" and (EnemyPkmnType1 == "Fight" or EnemyPkmnType1 == "Bug"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Bug"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Psychic" or EnemyPkmnType2 == "Ghost"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Dark" and EnemyPkmnType1 == "Nullifier":
    Type = 0

if MoveType == "Psychic" and (EnemyPkmnType1 == "Fight" or EnemyPkmnType1 == "Poison"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Poison"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Bug" or EnemyPkmnType2 == "Ghost" or EnemyPkmnType2 == "Dark"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Psychic" and (EnemyPkmnType1 == "Bug" or EnemyPkmnType1 == "Ghost" or EnemyPkmnType1 == "Dark"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Bug" or EnemyPkmnType2 == "Ghost" or EnemyPkmnType2 == "Dark"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Poison"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
    elif Type == 0.5 and (EnemyPkmnType2 == "Dark" or EnemyPkmnType2 == "Steel"):
        Type = 0
elif MoveType == "Psychic" and (EnemyPkmnType1 == "Dark" or EnemyPkmnType1 == "Steel"):
    Type = 0

if MoveType == "Bug" and (EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Psychic" or EnemyPkmnType1 == "Dark"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Psychic" or EnemyPkmnType2 == "Dark"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Bug" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Flying" or EnemyPkmnType1 == "Rock"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Rock"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Psychic" or EnemyPkmnType2 == "Dark"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Bug" and EnemyPkmnType1 == "Nullifier":
    Type = 0
    
if MoveType == "Flying" and (EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Fight" or EnemyPkmnType1 == "Bug"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Bug"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Electric" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Flying" and (EnemyPkmnType1 == "Electric" or EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Rock"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Electric" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Rock"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Bug"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Flying" and EnemyPkmnType1 == "Nullifier":
    Type = 0

if MoveType == "Steel" and (EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Rock"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Rock"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Ground"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Steel" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Fight" or EnemyPkmnType1 == "Ground"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Fight" or EnemyPkmnType2 == "Ground"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Steel" and EnemyPkmnType1 == "Nullifier":
    Type = 0
    
if MoveType == "Fight" and (EnemyPkmnType1 == "Normal" or EnemyPkmnType1 == "Ice" or EnemyPkmnType1 == "Rock" or EnemyPkmnType1 == "Dark" or EnemyPkmnType1 == "Steel"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Normal" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Rock" or EnemyPkmnType2 == "Dark" or EnemyPkmnType2 == "Steel"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Psychic"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Fight" and (EnemyPkmnType1 == "Flying" or EnemyPkmnType1 == "Psychic"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Flying" or EnemyPkmnType2 == "Psychic"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Normal" or EnemyPkmnType2 == "Ice" or EnemyPkmnType2 == "Rock" or EnemyPkmnType2 == "Dark" or EnemyPkmnType2 == "Steel"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
    elif Type == 0.5 and (EnemyPkmnType2 == "Ghost"):
        Type = 0
elif MoveType == "Fight" and EnemyPkmnType1 == "Ghost":
    Type = 0
    
if MoveType == "Ground" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Electric" or EnemyPkmnType1 == "Poison" or EnemyPkmnType1 == "Rock" or EnemyPkmnType1 == "Steel"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Electric" or EnemyPkmnType2 == "Poison" or EnemyPkmnType2 == "Rock" or EnemyPkmnType2 == "Steel"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ice"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Ground" and (EnemyPkmnType1 == "Water" or EnemyPkmnType1 == "Grass" or EnemyPkmnType1 == "Ice"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Grass" or EnemyPkmnType2 == "Ice"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Electric" or EnemyPkmnType2 == "Poison" or EnemyPkmnType2 == "Rock" or EnemyPkmnType2 == "Steel"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
    elif Type == 0.5 and (EnemyPkmnType2 == "Flying"):
        Type = 0
elif MoveType == "Ground" and EnemyPkmnType1 == "Flying":
    Type = 0

if MoveType == "Ghost" and (EnemyPkmnType1 == "Psychic" or EnemyPkmnType1 == "Ghost"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Psychic" or EnemyPkmnType2 == "Ghost"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Dark"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Ghost" and (EnemyPkmnType1 == "Dark"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Ghost" or EnemyPkmnType2 == "Psychic"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
    elif Type == 0.5 and (EnemyPkmnType2 == "Normal"):
        Type = 0
elif MoveType == "Ghost" and EnemyPkmnType1 == "Normal":
    Type = 0

if MoveType == "Poison" and (EnemyPkmnType1 == "Grass"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Psychic"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Poison" and (EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Psychic"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Psychic"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Grass"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
    elif Type == 0.5 and (EnemyPkmnType2 == "Steel"):
        Type = 0
elif MoveType == "Poison" and EnemyPkmnType1 == "Steel":
    Type = 0

if MoveType == "Water" and (EnemyPkmnType1 == "Fire" or EnemyPkmnType1 == "Ground" or EnemyPkmnType1 == "Rock"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Electric" or EnemyPkmnType2 == "Grass"):
        Type = 1
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Water" and (EnemyPkmnType1 == "Electric" or EnemyPkmnType1 == "Grass"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Electric" or EnemyPkmnType2 == "Grass"):
        Type = 0.25
    elif Type == 0.5 and (EnemyPkmnType2 == "Fire" or EnemyPkmnType2 == "Ground" or EnemyPkmnType2 == "Rock"):
        Type = 1
    elif Type == 0.5 and (EnemyPkmnType2 == "n"):
        Type = 0.5
elif MoveType == "Water" and EnemyPkmnType1 == "Nullifier":
    Type = 0
    
if MoveType == "Electric" and (EnemyPkmnType1 == "Water" or EnemyPkmnType1 == "Flying"):
    Type = 2
    if Type == 2 and (EnemyPkmnType2 == "Water" or EnemyPkmnType2 == "Flying"):
        Type += 2
    elif Type == 2 and (EnemyPkmnType2 == "Ground"):
        Type = 0
    elif Type == 2 and (EnemyPkmnType2 == "n"):
        Type = 2
elif MoveType == "Electric" and (EnemyPkmnType1 == "Ground"):
    Type = 0
elif MoveType == "Electric" and EnemyPkmnType1 == "Ground":
    Type = 0
    
if MoveType == "Normal":
    Type = 1
elif MoveType == "Normal" and (EnemyPkmnType1 == "Fight"):
    Type = 0.5
    if Type == 0.5 and (EnemyPkmnType2 == "Ghost"):
        Type = 0
elif MoveType == "Normal" and EnemyPkmnType1 == "Ghost":
    Type = 0
    
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


