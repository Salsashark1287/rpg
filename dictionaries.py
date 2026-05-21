from classes import *

ITEM_DICT = {
    # Weapons: name, gold_value, hit_mod, attack_power, to_hit_stat, lvl_req
    # TIER 1 Starter Gear (Hit Mods buffed from +1/+2 to +4/+5 to counter low starter stats)
    "Bronze Sword": Weapon("Bronze Sword", 50, 4, 4, "str", 1),
    "Iron Dagger": Weapon("Iron Dagger", 40, 5, 3, "dex", 1),
    "Hunting Bow": Weapon("Hunting Bow", 65, 4, 5, "dex", 1),
    "Wooden Staff": Weapon("Wooden Staff", 30, 5, 2, "wis", 1), # Buffed to +5 hit so Mages don't miss Slimes!
    
    # TIER 2 Mid-Game Gear (Added new choices and scaled hit/power)
    "Iron Mace": Weapon("Iron Mace", 90, 5, 5, "str", 2),
    "Apprentice Wand": Weapon("Apprentice Wand", 110, 6, 4, "wis", 2),
    "Spiked Club": Weapon("Spiked Club", 95, 4, 6, "str", 2),          # NEW: High power, lower accuracy alternative
    "Crossbow": Weapon("Crossbow", 125, 6, 5, "dex", 2),              # NEW: Reliable dex alternative
    
    # TIER 3 Late-Game Gear
    "Steel Longsword": Weapon("Steel Longsword", 150, 6, 7, "str", 3),
    "Recurve Bow": Weapon("Recurve Bow", 130, 7, 6, "dex", 3),
    "Archmage Staff": Weapon("Archmage Staff", 180, 8, 5, "wis", 3),   # NEW: High-tier Mage weapon
    "Serrated Dirk": Weapon("Serrated Dirk", 140, 8, 5, "dex", 3),     # NEW: High-accuracy Rogue upgrade
    
    
    # Shields / Off-hands: name, gold_value, def_modifier
    # (Fixed the Bronze Circlet constructor argument typo!)
    "Wooden Shield": Shield("Wooden Shield", 25, 2),
    "Iron Shield": Shield("Iron Shield", 75, 4),
    "Hide Bracer": Shield("Hide Bracer", 20, 1),
    "Leather Armband": Shield("Leather Armband", 20, 1),
    "Bronze Circlet": Shield("Bronze Circlet", 45, 2),                 # FIXED: Removed the extra argument crash
    "Steel Heater Shield": Shield("Steel Heater Shield", 120, 6),     # NEW: Heavy warrior shield
    "Buckler": Shield("Buckler", 50, 2),                               # NEW: Lightweight off-hand option
    
    
    # Armor: name, gold_value, def_modifier, hp_modifier
    "Woolen Tunic": Armor("Woolen Tunic", 20, 1, 0),
    "Linen Robe": Armor("Linen Robe", 25, 1, 0),
    "Woolen Cape": Armor("Woolen Cape", 25, 1, 0),
    "Padded Armor": Armor("Padded Armor", 40, 2, 2),                   # Buffed: Added minor HP bump
    "Leather Vest": Armor("Leather Vest", 60, 3, 5),
    "Hardened Leather": Armor("Hardened Leather", 120, 4, 8),
    "Iron Cuirass": Armor("Iron Cuirass", 200, 6, 12),                 # Buffed: Raised HP modifier
    "Chainmail Hauberk": Armor("Chainmail Hauberk", 160, 5, 10),       # NEW: Solid mid-to-late tier armor
    "Enchanted Robes": Armor("Enchanted Robes", 150, 2, 6),            # NEW: Caster-focused armor upgrade
    
    
    # Potions: name, gold_value, stat_to_boost, amount, perm_boost
    "Minor Healing Potion": Potion("Minor Healing Potion", 15, "hp", 10, False),
    "Major Healing Potion": Potion("Major Healing Potion", 50, "hp", 25, False),
    "Elixir of Growth": Potion("Elixir of Growth", 100, "max_hp", 5, True),
    "Draught of Vitality": Potion("Draught of Vitality", 250, "max_hp", 15, True),
    "Essence of Strength": Potion("Essence of Strength", 150, "str", 2, False),
    "Intellect Brew": Potion("Intellect Brew", 150, "wis", 2, False),
    "Nimble Draught": Potion("Nimble Draught", 150, "dex", 2, False)
}

ENEMY_DICT = {
    # name, atk_pwr, def_pwr, hp, dex, gold_value
    
    # Tier 1: Level 1-2 Fodder
    "Giant Rat": Monster("Giant Rat", 2, 1, 10, 1, 5),
    "Slime": Monster("Slime", 1, 3, 15, 3, 8),
    "Goblin": Monster("Goblin", 3, 2, 18, 7, 12),
    
    # Tier 2: Mid-Game Threats
    "Bandit": Monster("Bandit", 5, 2, 25, 10, 20),
    "Skeleton Warrior": Monster("Skeleton Warrior", 6, 4, 30, 15, 25),
    "Orc Grunt": Monster("Orc Grunt", 8, 3, 45, 25, 40),
    
    # Tier 3: Late-Game Heavy Hitters
    "Cave Troll": Monster("Cave Troll", 12, 6, 80, 30, 75),
    "Gargoyle": Monster("Gargoyle", 10, 12, 70, 35, 90),
    
    # Tier 4: Bosses
    "Vampire Lord": Monster("Vampire Lord", 18, 10, 150, 40, 250),
    "Elder Dragon": Monster("Elder Dragon", 25, 15, 300, 50, 500)
}