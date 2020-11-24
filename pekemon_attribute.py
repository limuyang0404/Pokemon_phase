# coding=UTF-8
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from os import listdir
import random
from os.path import isfile, join, getsize
'''this function is made to get a Two-dimensional dimensions with mirrored edges'''
def phase_relationship(attribute):
    attack_phase = {'Normal':1, 'Fly':1, 'Fire':1, 'Psychic':1, 'Water':1, 'Bug':1, 'Electric':1, 'Rock':1,
                    'Grass':1, 'Ghost':1, 'Ice':1, 'Dragon':1, 'Fight':1, 'Dark':1, 'Poison':1, 'Steel':1, 'Ground':1, 'Fairy':1}
    defence_phase = {'Normal':1, 'Fly':1, 'Fire':1, 'Psychic':1, 'Water':1, 'Bug':1, 'Electric':1, 'Rock':1,
                    'Grass':1, 'Ghost':1, 'Ice':1, 'Dragon':1, 'Fight':1, 'Dark':1, 'Poison':1, 'Steel':1, 'Ground':1, 'Fairy':1}
    if attribute == 'Normal':
        attack_phase = {'Normal': 1, 'Fly': 1, 'Fire': 1, 'Psychic': 1, 'Water': 1, 'Bug': 1, 'Electric': 1,
                        'Rock': 0.5, 'Grass': 1, 'Ghost': 0, 'Ice': 1, 'Dragon': 1, 'Fight': 1, 'Dark': 1, 'Poison': 1,
                        'Steel': 0.5, 'Ground': 1, 'Fairy': 1}
        defence_phase = {'Normal': 1, 'Fly': 1, 'Fire': 1, 'Psychic': 1, 'Water': 1, 'Bug': 1, 'Electric': 1,
                         'Rock': 0.5, 'Grass': 1, 'Ghost': 0, 'Ice': 1, 'Dragon': 1, 'Fight': 1, 'Dark': 1, 'Poison': 1,
                         'Steel': 0.5, 'Ground': 1, 'Fairy': 1}
    elif attribute == 'Fly':
        attack_phase = {'Normal': 1, 'Fly': 1, 'Fire': 1, 'Psychic': 1, 'Water': 1, 'Bug': 1, 'Electric': 1,
                        'Rock': 0.5, 'Grass': 1, 'Ghost': 0, 'Ice': 1, 'Dragon': 1, 'Fight': 1, 'Dark': 1, 'Poison': 1,
                        'Steel': 0.5, 'Ground': 1, 'Fairy': 1}
        defence_phase = {'Normal': 1, 'Fly': 1, 'Fire': 1, 'Psychic': 1, 'Water': 1, 'Bug': 1, 'Electric': 1,
                        'Rock': 0.5, 'Grass': 1, 'Ghost': 0, 'Ice': 1, 'Dragon': 1, 'Fight': 1, 'Dark': 1, 'Poison': 1,
                        'Steel': 0.5, 'Ground': 1, 'Fairy': 1}

    return attack_phase, defence_phase

class Pokemon_attribute(object):
    def __init__(self):
        self.attack_phase = {'Normal': 1, 'Fly': 1, 'Fire': 1, 'Psychic': 1, 'Water': 1, 'Bug': 1, 'Electric': 1,
                        'Rock': 1, 'Grass': 1, 'Ghost': 1, 'Ice': 1, 'Dragon': 1, 'Fight': 1, 'Dark': 1, 'Poison': 1,
                        'Steel': 1, 'Ground': 1, 'Fairy': 1}
        self.defense_phase = {'Normal': 1, 'Fly': 1, 'Fire': 1, 'Psychic': 1, 'Water': 1, 'Bug': 1, 'Electric': 1,
                        'Rock': 1, 'Grass': 1, 'Ghost': 1, 'Ice': 1, 'Dragon': 1, 'Fight': 1, 'Dark': 1, 'Poison': 1,
                        'Steel': 1, 'Ground': 1, 'Fairy': 1}
        self.attack_2x = []
        self.attack_05x = []
        self.attack_00x = []
        self.defense_2x = []
        self.defense_05x = []
        self.defense_00x = []
        pass
    def attack_phase_show(self):
        print('This attribute will make double damage to these attribute(s): ', self.attack_2x)
        print('This attribute will make half damage to these attribute(s): ', self.attack_05x)
        print('This attribute will make zero damage to these attribute(s): ', self.attack_00x)
        pass
    def defense_phase_show(self):
        print('This attribute will take double damage to these attribute(s): ', self.defense_2x)
        print('This attribute will take half damage to these attribute(s): ', self.defense_05x)
        print('This attribute will take zero damage to these attribute(s): ', self.defense_00x)
        pass
    def phase_edit(self):
        for i in self.attack_2x:
            self.attack_phase[i] = 2
        for i in self.attack_05x:
            self.attack_phase[i] = 0.5
        for i in self.attack_00x:
            self.attack_phase[i] = 0
        for i in self.defense_2x:
            self.defense_phase[i] = 2
        for i in self.defense_05x:
            self.defense_phase[i] = 0.5
        for i in self.defense_00x:
            self.defense_phase[i] = 0
        return self.attack_phase, self.defense_phase
    pass

class Normal_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = []
        self.attack_05x = ['Rock', 'Steel']
        self.attack_00x = ['Ghost']
        self.defense_2x = ['Fight']
        self.defense_05x = []
        self.defense_00x = ['Ghost']
    pass

class Fly_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Bug', 'Fight', 'Grass']
        self.attack_05x = ['Electric', 'Rock', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Electric', 'Rock', 'Steel']
        self.defense_05x = ['Bug', 'Fight', 'Grass']
        self.defense_00x = ['Ground']
    pass

class Fire_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Grass', 'Ice', 'Bug', 'Steel']
        self.attack_05x = ['Fire', 'Water', 'Rock', 'Dragon']
        self.attack_00x = []
        self.defense_2x = ['Ground', 'Water', 'Rock']
        self.defense_05x = ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']
        self.defense_00x = []
    pass

class Psychic_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Poison', 'Fight']
        self.attack_05x = ['Psychic', 'Steel']
        self.attack_00x = ['Dark']
        self.defense_2x = ['Bug', 'Ghost', 'Dark']
        self.defense_05x = ['Fight', 'Psychic']
        self.defense_00x = []
    pass

class Water_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Ground', 'Fire', 'Rock']
        self.attack_05x = ['Water', 'Grass', 'Dragon']
        self.attack_00x = []
        self.defense_2x = ['Electric', 'Grass']
        self.defense_05x = ['Fire', 'Water', 'Ice', 'Steel']
        self.defense_00x = []
        pass

class Bug_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Grass', 'Psychic', 'Dark']
        self.attack_05x = ['Poison', 'Fly', 'Fight', 'Fire', 'Ghost', 'Steel', 'Fairy']
        self.attack_00x = []
        self.defense_2x = ['Fly', 'Fire', 'Rock']
        self.defense_05x = ['Ground', 'Fight', 'Grass']
        self.defense_00x = []
    pass

class Electric_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Fly', 'Water']
        self.attack_05x = ['Electric', 'Grass', 'Dragon']
        self.attack_00x = ['Ground']
        self.defense_2x = ['Ground']
        self.defense_05x = ['Fly', 'Electric', 'Steel']
        self.defense_00x = []
    pass

class Rock_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Bug', 'Fly', 'Fire', 'Ice']
        self.attack_05x = ['Ground', 'Fight', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Ground', 'Fight', 'Water', 'Grass', 'Steel']
        self.defense_05x = ['Normal', 'Poison', 'Fly', 'Fire']
        self.defense_00x = []
    pass

class Grass_attribute(Pokemon_attribute):
    def __init__(self):
        super().__init__()
        self.attack_2x = ['Ground', 'Water', 'Rock']
        self.attack_05x = ['Bug', 'Poison', 'Fly', 'Fire', 'Grass', 'Dragon', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Bug', 'Poison', 'Fly', 'Fire', 'Ice']
        self.defense_05x = ['Ground', 'Water', 'Electric', 'Grass']
        self.defense_00x = []
    pass

class Ghost_attribute(Pokemon_attribute):
    def __init__(self):
        super(Ghost_attribute, self).__init__()
class pokemon(object):
    def __init__(self, attribute):
        self.attribute = attribute

    # def phase(self, attack_attribute):
    #     for i
    pass

# atk, defen = phase_relationship('aba')
a = Normal_attribute()
print(a.attack_phase)
a.phase_edit()
print(a.attack_phase)
a.attack_phase_show()


# a = Pokemon_attribute()
# print(a.attack_phase)
# a.phase_edit()
# print(a.attack_phase)
# print(a.defense_phase)
# a.attack_phase_show()
# print()
































