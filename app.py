import random
from time import *

health = 100
strength = 100 
stamina = 100
hunger = 100
sleep = 100

class hero:
    def _init_(self,name):
        self.name = name
        self.health = health
        self.strength = strength
        self.stamina = stamina
        self.hunger = hunger
        self.sleep = sleep

def attacked(self):
    global health, strength, stamina, hunger, sleep
    self.health = min(100, health - random.randint(1,health))
    self.strength = min(100, strength - random.randint(1,strength))
    self.stamina = min(100, stamina - random.randint(1,stamina))
    self.hunger = min(100, hunger - random.randint(1,hunger))
    self.sleep = min(100, sleep - random.randint(1,sleep))

def ate_food(self):
    global hunger
    self.hunger = min(100, hunger + random.randint(1, hunger))

def slept(self):
    global sleep, stamina, strength
    self.sleep = min(100, sleep + random.randint(1,sleep))
    self.stamina = min(100, stamina + random.randint(1,stamina))
    self.strength = min(100, strength + random.randint(1,strength))

def work_out(self):
    global sleep, stamina, strength, hunger
    self.strength = min(100, strength + random.randint(1,strength))
    self.stamina = min(100, stamina - random.randint(1,stamina))
    self.sleep = min(100, sleep - random.randint(1,sleep))
    self.hunger = min(100, hunger - random.randint(1,hunger))

if health < 1:
    run_game = False
if health > 1:
    run_game = True


if run_game == True:
    print("      ")
    print("hello Welcome to Island escape sim" 
    "your goal is to Escape the Island by beating enemies to get pass all" 
    "5 levels of the game! Once this is done youll officially have beat the game!")
    print("      ")
    print("here are your stats")
    print("health:",health)
    print("stregth:", strength)
    print("stamina:", stamina )
    print("hunger:", hunger)
    print("sleep:", sleep)
    name = input("what name would you like to input for this run?")
    print(f"okay" ,name, "Welcome to your run")
    print("Level 1")
    print("__________________________________________")
    print("you come across a cave and enter in there are two paths" \
    " one says 'heaven' the other says 'hell which do you choose to enter? ")
    cave_choice = input("enter either 'danger' or 'heaven': ").strip().lower()

while cave_choice != "danger" and cave_choice != "heaven":
    print("not a valid entry try again")
    cave_choice = input("enter either 'danger' or 'heaven': ").strip().lower()

print(f"you chose the {cave_choice} path, you MIGHT be cooked gng")

if cave_choice == "danger":
    print("")
