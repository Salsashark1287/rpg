import random
import copy
import os
from classes import *
from dictionaries import *
from combat import *


def main():
    os.system('clear')
    hero_name = input("Greetings adventurer! Welcome to the mystical land of Castille. What is your name?\n")
    os.system('clear')
    hero_class = input (f"Tell me {hero_name} what kind of hero are you?\n\nAre you a Warrior, fighting the hordes off with your sword and shield?\n\nOr are you a Ranger, darting swiftly around the battlefield firing volleys of arrows at your enemies?\n\nOr are you a wise Mage, using your mind and the elements to cast spells at the evil you encounter?\n\nOr are you a Rogue, hiding in the shadows and waiting for the perfect moment to leap out with your dagger and strike?\n\nWhat will it be adventurer:\n\n[1]Warrior\n[2]Ranger\n[3]Mage\n[4]Rogue\n")
    os.system('clear')
    if hero_class == "1":
        hero = Warrior(hero_name)
    elif hero_class == "2":
        hero = Ranger(hero_name)
    elif hero_class == "3":
        hero = Mage(hero_name)
    elif hero_class == "4":
        hero = Rogue(hero_name)
    else:
        return(print("Class not found"))
    print(f"\n{hero.name}\n\nLevel {hero.level} {hero.player_class}\n\nSTR:{hero.stats["str"]}\nDEX:{hero.stats["dex"]}\nCON:{hero.stats["con"]}\nWIS:{hero.stats["wis"]}\n")
    #Combat Test
    print("Practice battle")
    enemies = [copy.deepcopy(ENEMY_DICT["Slime"]), copy.deepcopy(ENEMY_DICT["Slime"]), copy.deepcopy(ENEMY_DICT["Slime"])]
    hero.inventory.append(ITEM_DICT["Minor Healing Potion"])
    combat(hero, enemies)


main()