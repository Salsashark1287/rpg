from classes import *
from dictionaries import *
import copy
import random


def combat(player, monsters):
    print(f"Watch out {player.name}! A battle begins.\n")
    while player.current_hp > 0 and any([monster.hp > 0 for monster in monsters]):
        