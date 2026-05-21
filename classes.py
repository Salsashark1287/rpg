import random


class Player :
    def __init__(self, name, player_class, stats, starting_gear, level = 1):
        from dictionaries import ITEM_DICT

        self.name = name
        self.level = level
        self.exp = 0
        self.player_class = player_class
        self.stats = stats
        self.max_hp_buff = 0
        self.equipped_weapon = ITEM_DICT[starting_gear[0]]
        self.equipped_armor = ITEM_DICT[starting_gear[2]]
        self.equipped_shield = ITEM_DICT[starting_gear[1]]
        self.current_hp = self.max_hp
        self.inventory = [ITEM_DICT[i] for i in starting_gear]
        self.wallet = 0
        self.buffs ={
            "str": 0,
            "dex": 0,
            "con": 0,
            "wis": 0
        }
    @property
    def max_hp(self):
        if self.equipped_armor != None:
            return max(12, self.stats["con"] * 2) + self.max_hp_buff + self.equipped_armor.hp_modifier
        return max(12, self.stats["con"] * 2) + self.max_hp_buff


    def drink_potion(self, potion):
        if potion.stat_to_boost == "hp":
            if self.current_hp + potion.amount < self.max_hp:
                print(f"You heal {potion.amount} hitpoints\n")
            else:
                print(f"You heal {self.max_hp - self.current_hp} hitpoints\n")
            self.current_hp = min(self.max_hp, self.current_hp + potion.amount)
        elif potion.stat_to_boost =="max_hp":
            self.max_hp_buff += potion.amount
            print(f"Your maximum hitpoints increase by {potion.amount}\n")
        else:
            self.stats[potion.stat_to_boost] += potion.amount
            print(f"Your {potion.stat_to_boost} increased by {potion.amount}\n")

        self.inventory.remove(potion)
    
    def equip(self, item):
        if item in self.inventory:
            if isinstance(item, Weapon):
                if item.lvl_req > self.level:
                    return print(self.name, "needs ", item.lvl_req - self.level, "more levels to wield this weapon.")
                else:
                    self.equipped_weapon = item
                    return self.equipped_weapon
            elif isinstance(item, Armor):
                self.equipped_armor = item
                return self.equipped_armor
            elif isinstance(item, Shield):
                self.equipped_shield = item
                return self.equipped_shield
            else:
                return print("Item is not equippable")

        return print("Item not found in inventory")

        

class Warrior(Player):
    def __init__(self, name, player_class="Warrior", level=1):
        stats = {
        "str": random.randint(12, 22), 
        "dex": random.randint(4, 14), 
        "con": random.randint(8, 18), 
        "wis": random.randint(1, 11)
        }
        starting_gear = ["Bronze Sword", "Wooden Shield", "Woolen Tunic"]
        super().__init__(name, player_class, stats, starting_gear, level)

class Ranger(Player):
    def __init__(self, name, player_class="Ranger", level=1):
        stats = {
        "str": random.randint(8, 18), 
        "dex": random.randint(12, 22), 
        "con": random.randint(4, 14), 
        "wis": random.randint(2, 12),
        }
        starting_gear = ["Hunting Bow", "Hide Bracer", "Woolen Tunic"]
        super().__init__(name, player_class, stats, starting_gear, level)

class Mage(Player):
    def __init__(self, name, player_class="Mage", level=1):
        stats = {
        "str": random.randint(1, 11), 
        "dex": random.randint(6, 16), 
        "con": random.randint(4, 14), 
        "wis": random.randint(12, 22),
        }
        starting_gear = ["Wooden Staff", "Bronze Circlet", "Linen Robe"]
        super().__init__(name, player_class, stats, starting_gear, level)

class Rogue(Player):
    def __init__(self, name, player_class="Rogue", level=1):
        stats = {
        "str": random.randint(4, 14), 
        "dex": random.randint(12, 22), 
        "con": random.randint(6, 16),  
        "wis": random.randint(6, 16),
        }
        starting_gear = ["Iron Dagger", "Leather Armband", "Woolen Cape"]
        super().__init__(name, player_class, stats, starting_gear, level)


class Item :
    def __init__(self, name, gold_value, item_type):
        self.name = name
        self.item_type = item_type
        self.gold_value = gold_value

class Weapon(Item):
    def __init__(self, name, gold_value, hit_mod, attack_power, to_hit_stat, lvl_req, item_type = "Weapon"):
        super().__init__(name, gold_value, item_type)
        self.hit_mod = hit_mod
        self.attack_power = attack_power
        self.to_hit_stat = to_hit_stat
        self.lvl_req = lvl_req

class Shield(Item):
    def __init__(self, name, gold_value, def_modifier, item_type = "Shield"):
        super().__init__(name, gold_value, item_type)
        self.def_modifier =  def_modifier

class Armor(Item):
    def __init__(self, name, gold_value, def_modifier, hp_modifier, item_type = "Armor"):
        super().__init__(name, gold_value, item_type)
        self.def_modifier = def_modifier
        self.hp_modifier = hp_modifier

class Potion(Item):
    def __init__(self, name, gold_value, stat_to_boost, amount, perm_boost, item_type = "Potion"):
        super().__init__(name, gold_value, item_type)
        self.stat_to_boost = stat_to_boost
        self.amount = amount
        self.perm_boost = perm_boost

class Monster:
    def __init__(self, name, atk_pwr, def_pwr, hp, dex, gold_value):
        self.name = name
        self.atk_pwr = atk_pwr
        self.def_pwr = def_pwr
        self.hp = hp
        self.current_hp = hp
        self.dex = dex
        self.gold_value = gold_value

