import math
from re import A
from sympy import *
import random

a = (sqrt(8)).evalf()

Targets = 1
Weather = 1.5
Badge = 1
Critical = 2
rendom = random.uniform(0.85,1.00)
STAB = 1.5
Type = 2
modifier = Targets * Weather * Badge * Critical * rendom * STAB * Type
Damage = ((((((2*15)/5)+2)*(110)*(205/180))/50)+2) * modifier
print(round(Damage))




