import random

class Player :
    def __init__(self, name, player_class, stats, starting_gear, level = 1):
        self.name = name
        self.level = level
        self.player_class = player_class
        self.stats = stats
        self.max_hp = max(10, (self.stats["con"] - 5) * 2)
        self.current_hp = self.max_hp
        self.inventory = starting_gear

class Warrior(Player):
    def __init__(self, name, player_class="Warrior", level=1):
        stats = {
        "str": random.randint(10, 16), 
        "dex": random.randint(5, 16), 
        "con": random.randint(8, 16), 
        "int": random.randint(3, 12), 
        "wis": random.randint(3, 12),
        "cha": random.randint(6, 16)
        }
        starting_gear = ["Bronze Sword", "Wooden Shield", "Woolen Tunic"]
        super().__init__(name, player_class, stats, starting_gear, level)

class Ranger(Player):
    def __init__(self, name, player_class="Ranger", level=1):
        stats = {
        "str": random.randint(8, 14), 
        "dex": random.randint(10, 16), 
        "con": random.randint(6, 14), 
        "int": random.randint(5, 12), 
        "wis": random.randint(5, 12),
        "cha": random.randint(8, 16)
        }
        starting_gear = ["Hunting Bow", "Hide Bracer", "Woolen Tunic"]
        super().__init__(name, player_class, stats, starting_gear, level)

class Mage(Player):
    def __init__(self, name, player_class="Mage", level=1):
        stats = {
        "str": random.randint(3, 10), 
        "dex": random.randint(5, 16), 
        "con": random.randint(4, 12), 
        "int": random.randint(8, 16), 
        "wis": random.randint(8, 16),
        "cha": random.randint(8, 16)
        }
        starting_gear = ["Wooden Staff", "Bronze Circlet", "Linen Robe"]
        super().__init__(name, player_class, stats, starting_gear, level)

class Thief(Player):
    def __init__(self, name, player_class="Thief", level=1):
        stats = {
        "str": random.randint(6, 14), 
        "dex": random.randint(8, 16), 
        "con": random.randint(6, 14), 
        "int": random.randint(8, 14), 
        "wis": random.randint(3, 12),
        "cha": random.randint(10, 16)
        }
        starting_gear = ["Iron Dagger", "Leather Armband", "Woolen Cape"]
        super().__init__(name, player_class, stats, starting_gear, level)


class Item :
    def __init__(self, name, gold_value, item_type):
        self.name = name
        self.item_type = item_type
        self.gold_value = gold_value

class Weapon(Item):
    def __init__(self, name, gold_value, atk_modifier, dmg_modifier, to_hit_stat, item_type = "Weapon"):
        super().__init__(name, gold_value, item_type)
        self.atk_modifier = atk_modifier
        self.dmg_modifier = dmg_modifier
        self.to_hit_stat = to_hit_stat

