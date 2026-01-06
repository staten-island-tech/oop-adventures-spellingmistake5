import random
from time import *





health = 100
strength = 100
stamina = 100
hunger = 100
sleep = 100

def attacked():
    global health, strength, stamina, hunger, sleep
    health = min(100, health - random.randint(1,health))
    strength = min(100, strength - random.randint(1,strength))
    stamina = min(100, stamina - random.randint(1,stamina))
    hunger = hunger - random.randint(1,hunger)
    sleep = sleep - random.randint(1,sleep)

def ate_food():
    global hunger
    hunger = min(100, hunger + random.randint(1, 20))