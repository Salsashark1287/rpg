from classes import *

ITEM_DICT = {
    # Weapons: name, gold_value, atk_modifier, dmg_modifier, to_hit_stat, lvl_req
    "Bronze Sword": Weapon("Bronze Sword", 50, 2, 4, "str", 1),
    "Iron Dagger": Weapon("Iron Dagger", 40, 1, 3, "dex", 1),
    "Hunting Bow": Weapon("Hunting Bow", 65, 2, 5, "dex", 1),
    "Wooden Staff": Weapon("Wooden Staff", 30, 1, 2, "int", 1),
    "Iron Mace": Weapon("Iron Mace", 90, 3, 5, "str", 2),
    "Steel Longsword": Weapon("Steel Longsword", 150, 4, 7, "str", 3),
    "Recurve Bow": Weapon("Recurve Bow", 130, 3, 6, "dex", 3),
    "Apprentice Wand": Weapon("Apprentice Wand", 110, 2, 4, "int", 2),
    
    # Shields: name, gold_value, def_modifier
    "Wooden Shield": Shield("Wooden Shield", 25, 2),
    "Iron Shield": Shield("Iron Shield", 75, 4),
    "Hide Bracer": Shield("Hide Bracer", 20, 1),
    "Leather Armband": Shield("Leather Armband", 20, 1),
    "Bronze Circlet": Shield("Bronze Circlet", 45, 1, 2),
    
    # Armor: name, gold_value, def_modifier, hp_modifier
    "Woolen Tunic": Armor("Woolen Tunic", 20, 1, 0),
    "Leather Vest": Armor("Leather Vest", 60, 3, 5),
    "Linen Robe": Armor("Linen Robe", 25, 1, 0),
    "Woolen Cape": Armor("Woolen Cape", 25, 1, 0),
    "Padded Armor": Armor("Padded Armor", 40, 2, 0),
    "Iron Cuirass": Armor("Iron Cuirass", 200, 6, 10),
    "Hardened Leather": Armor("Hardened Leather", 120, 4, 8),
    
    # Potions: name, gold_value, stat_to_boost, amount, perm_boost
    "Minor Healing Potion": Potion("Minor Healing Potion", 15, "hp", 10, False),
    "Major Healing Potion": Potion("Major Healing Potion", 50, "hp", 25, False),
    "Elixir of Growth": Potion("Elixir of Growth", 100, "max_hp", 5, True),
    "Draught of Vitality": Potion("Draught of Vitality", 250, "max_hp", 15, True),
    "Essence of Strength": Potion("Essence of Strength", 150, "str", 2, False),
    "Intellect Brew": Potion("Intellect Brew", 150, "int", 2, False),
    "Nimble Draught": Potion("Nimble Draught", 150, "dex", 2, False)
}

ENEMY_DICT = {
    # name, atk_pwr, def_pwr, hp, gold_value
    
    # Tier 1: Level 1-2 Fodder
    "Giant Rat": Monster("Giant Rat", 2, 1, 10, 5),
    "Slime": Monster("Slime", 1, 3, 15, 8),
    "Goblin": Monster("Goblin", 3, 2, 18, 12),
    
    # Tier 2: Mid-Game Threats
    "Bandit": Monster("Bandit", 5, 2, 25, 20),
    "Skeleton Warrior": Monster("Skeleton Warrior", 6, 4, 30, 25),
    "Orc Grunt": Monster("Orc Grunt", 8, 3, 45, 40),
    
    # Tier 3: Late-Game Heavy Hitters
    "Cave Troll": Monster("Cave Troll", 12, 6, 80, 75),
    "Gargoyle": Monster("Gargoyle", 10, 12, 70, 90),
    
    # Tier 4: Bosses
    "Vampire Lord": Monster("Vampire Lord", 18, 10, 150, 250),
    "Elder Dragon": Monster("Elder Dragon", 25, 15, 300, 500)
}