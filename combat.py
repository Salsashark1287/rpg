from classes import *
from dictionaries import *
import copy
import random
import os


def combat(player, monsters):
    print(f"Watch out {player.name}! A battle begins.\n")
    while player.current_hp > 0 and any([monster.current_hp > 0 for monster in monsters]):
        print(f"=================== COMBAT ===================\n{player.name} {player.current_hp}/{player.max_hp}\n----------------------------------------------")
        for monster in monsters:
            if monster.current_hp > 0:
                print(f"{monster.name}-HP:{monster.current_hp}")
        #Select Action
        action = input("Choose your action:(Type the number)\n[1] Attack\n[2] Use Item\n[3] Run\n")
        os.system('clear')
        if action == "1":
            while True:
                live_monsters = []
                for index, monster in enumerate(monsters):
                    if monster.current_hp > 0:
                        print(f"[{index}]{monster.name}-HP:{monster.current_hp}")
                        live_monsters.append(monster)
                if len(live_monsters) == 1:
                    target_enemy = live_monsters[0]
                    break
                else:
                    target_string = input("Which enemy do you choose to attack?\n")
                    os.system('clear')
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
                        if target_enemy.current_hp == 0:
                            print("That enemy is already dead\n")
                            continue
                        break
            attack_mod = max(0, ((player.stats[player.equipped_weapon.to_hit_stat] + (player.buffs[player.equipped_weapon.to_hit_stat]) - 10) // 2))
            if attack_mod + random.randint(1,20) + player.equipped_weapon.hit_mod > target_enemy.dex + random.randint(1,20):
                player_damage = attack_mod
                for i in range(player.equipped_weapon.attack_power):
                    player_damage += random.randint(1,4)
                player_damage = max(1, player_damage - target_enemy.def_pwr)
                print(f"You deal {player_damage} to the {target_enemy.name}\n")
                target_enemy.current_hp = max(0, target_enemy.current_hp - player_damage)
                if target_enemy.current_hp == 0:
                    print(f"The {target_enemy.name} dies\n")
                    player.current_exp += target_enemy.exp
                    print(f"You gain {target_enemy.exp} experience.\n")
                    if player.current_exp >= player.exp_to_level:
                        player.level_up()
            else:
                print(f"Your attack misses the {target_enemy.name}\n")


        elif action == "2":
            potions = [item for item in player.inventory if isinstance(item, Potion)]
            if len(potions) == 0:
                print("No potions in inventory\n")
                continue
            for index, potion in enumerate(potions):
                print(f"[{index}] {potion.name}")
            while len(potions) > 0:
                potion_string = input("Which potion would you like to use?\n")
                os.system('clear')
                try: 
                    potion = int(potion_string)
                except ValueError:
                    continue
                if potion < 0 or potion > len(potions) - 1 :
                    print("Invalid selection\n")
                else:
                    player.drink_potion(potions[potion])
                    break

        elif action == "3":
            player_run = player.stats["dex"] + player.buffs["dex"] + random.randint(1,20)
            if all(player_run > monster.dex for monster in monsters if monster.hp > 0):
                print("You manage to run away!\n")
                return

        else:
            continue
        
        player_dex_modifier = max(0, (player.stats["dex"] + player.buffs["dex"] - 10) // 2)
        for monster in monsters: 
            if monster.current_hp > 0:
                if monster.dex + random.randint(1,20) >  player_dex_modifier + random.randint(1,20) + player.equipped_shield.def_modifier:
                    monster_damage = 0
                    for i in range(monster.atk_pwr):
                        monster_damage += random.randint(1,4)
                    monster_damage = max(1, monster_damage - player.equipped_armor.def_modifier)
                    player.current_hp -= monster_damage
                    print(f"The {monster.name} attacks and does {monster_damage} damage to you\n")
                else:
                    print(f"The {monster.name} tries to attack, but misses\n")
    if player.current_hp == 0:
        print("Your adventure has come to an end. Farewell Hero!")
        return
    if all(monster.current_hp == 0 for monster in monsters):
        print("Victory. All monsters have been slain")
        gold = 0
        for monster in monsters:
            gold += monster.gold_value
        player.wallet += gold
        print(f"You recieve {gold}gp\n")
        return


            


