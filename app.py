import random
from time import *



def stats():
    global health, strength, stamina, hunger, sleep
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
    hunger = min(100, hunger - random.randint(1,hunger))
    sleep = min(100, sleep - random.randint(1,sleep))

def ate_food():
    global hunger
    hunger = min(100, hunger + random.randint(1, hunger))

def slept():
    global sleep, stamina, strength
    sleep = min(100, sleep + random.randint(1,sleep))
    stamina = min(100, stamina + random.randint(1,stamina))
    strength = min(100, strength + random.randint(1,strength))


def work_out():
    global sleep, stamina, strength, hunger
    strength = min(100, strength + random.randint(1,strength))
    stamina = min(100, stamina - random.randint(1,stamina))
    sleep = min(100, sleep - random.randint(1,sleep))
    hunger = min(100, hunger - random.randint(1,hunger))

while health < 1:
    run_game = False

while run_game == True:
    print("hello Welcome to Island escape sim" \
    "your goal is to Escape the Island by beating enemies to get pass all" \
    "5 levels of the game! Once this is done youll officially have beat the game!")
    print("      ")
    print("here are your stats")
    print(stats)

