import random
from classes import *
from dictionaries import *


def main():
    hero_name = input("Greetings adventurer! Welcome to the mystical land of Castille. What is your name?\n")
    hero_class = input (f"Tell me {hero_name} what kind of hero are you?\n Are you a Warrior, fighting the hordes off with your sword and shield?\n Or are you a Ranger, darting swiftly around the battlefield firing volleys of arrows at your enemies?\n Or are you a wise Mage, using your mind and the elements to cast spells at the evil you encounter?\n Or are you a Rogue, hiding in the shadows and waiting for the perfect moment to leap out with your dagger and strike?\n What will it be adventurer: Warrior, Ranger, Mage, or Rogue?\n")
    if hero_class.capitalize() == "Warrior":
        hero = Warrior(hero_name)
    elif hero_class.capitalize() == "Ranger":
        hero = Ranger(hero_name)
    elif hero_class.capitalize() == "Mage":
        hero = Mage(hero_name)
    elif hero_class.capitalize() == "Rogue":
        hero = Rogue(hero_name)
    else:
        return(print("Class not found"))
    print(f"Name:{hero.name}\n Level:{hero.level} {hero.player_class}\n STR:{hero.stats["str"]} DEX:{hero.stats["dex"]} CON:{hero.stats["con"]} INT:{hero.stats["int"]} WIS:{hero.stats["wis"]} CHA:{hero.stats["cha"]}")



main()