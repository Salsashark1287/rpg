import random
import copy
import os
import time
import textwrap
from classes import *
from dictionaries import *
from combat import *


def main():
    os.system("echo -ne '\033[8;45;130t' ")
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
    info_box(hero)
    print("...zzz...")
    time.sleep(2)
    os.system('clear')
    info_box(hero)
    time.sleep(.4)
    print("...zzz...zzz...")
    time.sleep(2)
    os.system('clear')
    info_box(hero)
    time.sleep(.4)
    print("...zzz...zzz...zzz...")
    time.sleep(2)
    os.system('clear')
    info_box(hero)
    time.sleep(.4)
    print("...zzz...zzz...zzz...\033[3mhelp\033[0m...")
    time.sleep(2)
    os.system('clear')
    info_box(hero)
    time.sleep(.4)
    print("...zzz...zzz...zzz...\033[3mhelp\033[0m...\033[3mgoblins\033[0m...")
    time.sleep(2)
    os.system('clear')
    info_box(hero)
    time.sleep(.4)
    print("...zzz...zzz...zzz...\033[3mhelp\033[0m...\033[3mgoblins\033[0m...\033[3mHELLPPP!!!!\033[0m...\n")   
    time.sleep(2)
    os.system('clear')
    info_box(hero)
    time.sleep(.4)
    print(textwrap.fill(f"The first thing you register as your eyes snap open is the screaming. The next is the smell, smoke. Not the smell of cookfires, but the scent of burning thatch and timber. The *\033[3mding ding ding\033[0m* of the town bell cuts through the shouts outside your window. The words 'goblins' and 'attacking' pierce your foggy mind, and you sit straight up in bed, your breath catching in your throat. You jump to your feet, throwing on your {hero.equipped_armor.name} and {hero.equipped_shield.name}. You pick up your {hero.equipped_weapon.name}, and just as you do the door to your room bursts open and there stands a goblin, green skin stained with ash and a devious yellow smile at finding you here.", width=120))
    time.sleep(25)
    os.system('clear')
    combat(hero, monsters = [ENEMY_DICT["Goblin"]])

def info_box(hero):
    print(f"+++++++++++++++++++++++\n{hero.name}\n\nLevel {hero.level} {hero.player_class}\n\nSTR:{hero.stats["str"]}\nDEX:{hero.stats["dex"]}\nCON:{hero.stats["con"]}\nWIS:{hero.stats["wis"]}\n+++++++++++++++++++++++\n\n")



main()