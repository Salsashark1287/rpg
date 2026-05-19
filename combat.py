from classes import *
from dictionaries import *
import copy
import random


def combat(player, monsters):
    print(f"Watch out {player.name}! A battle begins.\n")
    while player.current_hp > 0 and any([monster.current_hp > 0 for monster in monsters]):
        print(f"=================== COMBAT ===================\n{player.name} {player.current_hp}/{player.max_hp}\n----------------------------------------------")
        for index, monster in enumerate(monsters):
            if monster.current_hp > 0:
                print(f"[{index}]{monster.name}-HP:{monster.current_hp}")
        #Select Action
        action = input("Choose your action:(Type the number)\n[1] Attack\n[2] Use Item\n[3] Run\n")
        if action == "1":
            while True:
                target_string = input("Which enemy do you choose to attack?\n")
                try:
                    target = int(target_string)
                except ValueError:
                    print("Invalid target. Must be a digit.\n")
                    continue
                
                if target > len(monsters) - 1:
                    print("There aren't that many enemies in this encounter hero!\n")
                elif target < 0:
                    print("Invalid target\n")
                else:
                    target_enemy = monsters[target]
                    break
        elif action == "2":
                potions = [item for item in player.inventory if isinstance(item, Potion)]
                for index, potion in enumerate(potions):
                    print(f"[{index}] {potion.name}")
                while True:
                    potion_string = input("Which potion would you like to use?\n")
                    try: 
                        potion = int(potion_string)
                    except ValueError:
                        print("Invalid selection. Must be a digit.\n")
                        continue
                    if potion < 0 or potion > len(potions) - 1 :
                        print("Invalid selection\n")
                    else:
                        player.drink_potion(potions[potion])
                        break

