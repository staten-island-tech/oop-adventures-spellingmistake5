import random
from time import *

health = 100
strength = 100 
stamina = 100
hunger = 100
sleep = 100

class hero:
    def __init__(self,name):
        self.name = name
        self.health = health
        self.strength = strength
        self.stamina = stamina
        self.hunger = hunger
        self.sleep = sleep

    def attacked(self):
        global health, strength, stamina, hunger, sleep
        self.health = max(100, health - random.randint(1,health))
        self.strength = max(100, strength - random.randint(1,strength))
        self.stamina = max(100, stamina - random.randint(1,stamina))
        self.hunger = max(100, hunger - random.randint(1,hunger))
        self.sleep = max(100, sleep - random.randint(1,sleep))

    def ate_food(self):
        global hunger
        self.hunger = max(100, hunger + random.randint(1, hunger))

    def slept(self):
        global sleep, stamina, strength
        self.sleep = max(100, sleep + random.randint(1,sleep))
        self.stamina = max(100, stamina + random.randint(1,stamina))
        self.strength = max(100, strength + random.randint(1,strength))

    def work_out(self):
        global sleep, stamina, strength, hunger
        self.strength = max(100, strength + random.randint(1,strength))
        self.stamina = max(100, stamina - random.randint(1,stamina))
        self.sleep = max(100, sleep - random.randint(1,sleep))
        self.hunger = max(100, hunger - random.randint(1,hunger))

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
    player = hero(name)
    print(f"okay" ,name, "Welcome to your run")
    print("Level 1")
    print("__________________________________________")
    print("you come across a cave and enter in there are two paths" \
    " one says 'heaven' the other says 'danger which do you choose to enter? ")
    cave_choice = input("enter either 'danger' or 'heaven': ").strip().lower()

while cave_choice != "danger" and cave_choice != "heaven":
    print("not a valid entry try again")
    cave_choice = input("enter either 'danger' or 'heaven': ").strip().lower()

print(f"you chose the {cave_choice} path, you MIGHT be cooked gng")

if cave_choice == "danger":
    print("You walk into a empty room and see a big red button and pushed it, causing you to  get shhot by a arrow")
    player.attacked()
    print("here are your stats")
    print("health:",health)
    print("stregth:", strength)
    print("stamina:", stamina )
    print("hunger:", hunger)
    print("sleep:", sleep)

elif cave_choice == "heaven":
    print("okay so you walk in a room and theres a door to the next level, with no consequences so you advanced!!!")
    print("here are your stats")
    print("health:",health)
    print("stregth:", strength)
    print("stamina:", stamina )
    print("hunger:", hunger)
    print("sleep:", sleep)

print("Level 2")
print("__________________________________________")
print("as you escape the cabve you walk around and suddenly get surounded by a" \
"group of monkeys their leader ")



