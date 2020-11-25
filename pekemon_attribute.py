# coding=UTF-8
'''A small test to calculate Pokemon attributes phase'''
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
        print('This attribute will take double damage from these attribute(s): ', self.defense_2x)
        print('This attribute will take half damage from these attribute(s): ', self.defense_05x)
        print('This attribute will immunity damage from these attribute(s): ', self.defense_00x)
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
        super(Normal_attribute, self).__init__()
        self.attack_2x = []
        self.attack_05x = ['Rock', 'Steel']
        self.attack_00x = ['Ghost']
        self.defense_2x = ['Fight']
        self.defense_05x = []
        self.defense_00x = ['Ghost']
    pass

class Fly_attribute(Pokemon_attribute):
    def __init__(self):
        super(Fly_attribute, self).__init__()
        self.attack_2x = ['Bug', 'Fight', 'Grass']
        self.attack_05x = ['Electric', 'Rock', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Electric', 'Rock', 'Steel']
        self.defense_05x = ['Bug', 'Fight', 'Grass']
        self.defense_00x = ['Ground']
    pass

class Fire_attribute(Pokemon_attribute):
    def __init__(self):
        super(Fire_attribute, self).__init__()
        self.attack_2x = ['Grass', 'Ice', 'Bug', 'Steel']
        self.attack_05x = ['Fire', 'Water', 'Rock', 'Dragon']
        self.attack_00x = []
        self.defense_2x = ['Ground', 'Water', 'Rock']
        self.defense_05x = ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']
        self.defense_00x = []
    pass

class Psychic_attribute(Pokemon_attribute):
    def __init__(self):
        super(Psychic_attribute, self).__init__()
        self.attack_2x = ['Poison', 'Fight']
        self.attack_05x = ['Psychic', 'Steel']
        self.attack_00x = ['Dark']
        self.defense_2x = ['Bug', 'Ghost', 'Dark']
        self.defense_05x = ['Fight', 'Psychic']
        self.defense_00x = []
    pass

class Water_attribute(Pokemon_attribute):
    def __init__(self):
        super(Water_attribute, self).__init__()
        self.attack_2x = ['Ground', 'Fire', 'Rock']
        self.attack_05x = ['Water', 'Grass', 'Dragon']
        self.attack_00x = []
        self.defense_2x = ['Electric', 'Grass']
        self.defense_05x = ['Fire', 'Water', 'Ice', 'Steel']
        self.defense_00x = []
        pass

class Bug_attribute(Pokemon_attribute):
    def __init__(self):
        super(Bug_attribute, self).__init__()
        self.attack_2x = ['Grass', 'Psychic', 'Dark']
        self.attack_05x = ['Poison', 'Fly', 'Fight', 'Fire', 'Ghost', 'Steel', 'Fairy']
        self.attack_00x = []
        self.defense_2x = ['Fly', 'Fire', 'Rock']
        self.defense_05x = ['Ground', 'Fight', 'Grass']
        self.defense_00x = []
    pass

class Electric_attribute(Pokemon_attribute):
    def __init__(self):
        super(Electric_attribute, self).__init__()
        self.attack_2x = ['Fly', 'Water']
        self.attack_05x = ['Electric', 'Grass', 'Dragon']
        self.attack_00x = ['Ground']
        self.defense_2x = ['Ground']
        self.defense_05x = ['Fly', 'Electric', 'Steel']
        self.defense_00x = []
    pass

class Rock_attribute(Pokemon_attribute):
    def __init__(self):
        super(Rock_attribute, self).__init__()
        self.attack_2x = ['Bug', 'Fly', 'Fire', 'Ice']
        self.attack_05x = ['Ground', 'Fight', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Ground', 'Fight', 'Water', 'Grass', 'Steel']
        self.defense_05x = ['Normal', 'Poison', 'Fly', 'Fire']
        self.defense_00x = []
    pass

class Grass_attribute(Pokemon_attribute):
    def __init__(self):
        super(Grass_attribute, self).__init__()
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
        self.attack_2x = ['Psychic', 'Ghost']
        self.attack_05x = ['Dark']
        self.attack_00x = ['Normal']
        self.defense_2x = ['Dark', 'Ghost']
        self.defense_05x = ['Bug', 'Poison']
        self.defense_00x = ['Normal', 'Fight']
    pass

class Ice_attribute(Pokemon_attribute):
    def __init__(self):
        super(Ice_attribute, self).__init__()
        self.attack_2x = ['Fly', 'Ground', 'Grass', 'Dragon']
        self.attack_05x = ['Fire', 'Water', 'Ice', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Fight', 'Fire', 'Rock', 'Steel']
        self.defense_05x = ['Ice']
        self.defense_00x = []
    pass

class Dragon_attribute(Pokemon_attribute):
    def __init__(self):
        super(Dragon_attribute, self).__init__()
        self.attack_2x = ['Dragon']
        self.attack_05x = ['Steel']
        self.attack_00x = ['Fairy']
        self.defense_2x = ['Dragon', 'Ice', 'Fairy']
        self.defense_05x = ['Fire', 'Water', 'Electric', 'Grass']
        self.defense_00x = []
    pass

class Fight_attribute(Pokemon_attribute):
    def __init__(self):
        super(Fight_attribute, self).__init__()
        self.attack_2x = ['Normal', 'Rock', 'Ice', 'Steel', 'Dark']
        self.attack_05x = ['Bug', 'Poison', 'Fly', 'Psychic', 'Fairy']
        self.attack_00x = ['Ghost']
        self.defense_2x = ['Fly', 'Psychic']
        self.defense_05x = ['Bug', 'Rock', 'Dark']
        self.defense_00x = []
    pass

class Dark_attribute(Pokemon_attribute):
    def __init__(self):
        super(Dark_attribute, self).__init__()
        self.attack_2x = ['Psychic', 'Ghost']
        self.attack_05x = ['Fight', 'Dark', 'Fairy']
        self.attack_00x = []
        self.defense_2x = ['Bug', 'Fight', 'Fairy']
        self.defense_05x = ['Ghost', 'Dark']
        self.defense_00x = ['Psychic']
    pass

class Poison_attribute(Pokemon_attribute):
    def __init__(self):
        super(Poison_attribute, self).__init__()
        self.attack_2x = ['Grass', 'Fairy']
        self.attack_05x = ['Poison', 'Ground', 'Rock', 'Ghost']
        self.attack_00x = ['Steel']
        self.defense_2x = ['Ground', 'Psychic']
        self.defense_05x = ['Bug', 'Poison', 'Fight', 'Grass', 'Fairy']
        self.defense_00x = []
    pass

class Steel_attribute(Pokemon_attribute):
    def __init__(self):
        super(Steel_attribute, self).__init__()
        self.attack_2x = ['Ice', 'Rock', 'Fairy']
        self.attack_05x = ['Water', 'Fire', 'Electric', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Ground', 'Fight', 'Fire']
        self.defense_05x = ['Normal', 'Bug', 'Fly', 'Grass', 'Ice', 'Rock', 'Psychic', 'Dragon', 'Steel', 'Fairy']
        self.defense_00x = ['Poison']
    pass

class Ground_attribute(Pokemon_attribute):
    def __init__(self):
        super(Ground_attribute, self).__init__()
        self.attack_2x = ['Poison', 'Fire', 'Electric', 'Rock', 'Steel']
        self.attack_05x = ['Bug', 'Grass']
        self.attack_00x = ['Fly']
        self.defense_2x = ['Water', 'Grass', 'Ice']
        self.defense_05x = ['Poison', 'Rock']
        self.defense_00x = ['Electric']
    pass

class Fairy_attribute(Pokemon_attribute):
    def __init__(self):
        super(Fairy_attribute, self).__init__()
        self.attack_2x = ['Fight', 'Dragon', 'Dark']
        self.attack_05x = ['Poison', 'Fire', 'Steel']
        self.attack_00x = []
        self.defense_2x = ['Poison', 'Steel']
        self.defense_05x = ['Bug', 'Fight', 'Dark']
        self.defense_00x = ['Dragon']
    pass


class Compound_attribute(Pokemon_attribute):
    def __init__(self):
        super(Compound_attribute, self).__init__()
        self.defense_4x_more = []
        self.defense_4x = []
        self.defense_025x = []
        self.defense_025x_less = []
    def defense_phase_show(self):
        print('This attribute will take more than quadruple damage from these attribute(s): ', self.defense_4x_more)
        print('This attribute will take quadruple damage from these attribute(s): ', self.defense_4x)
        print('This attribute will take double damage from these attribute(s): ', self.defense_2x)
        print('This attribute will take half damage from these attribute(s): ', self.defense_05x)
        print('This attribute will take quarter damage from these attribute(s): ', self.defense_025x)
        print('This attribute will take less than quarter damage from these attribute(s): ', self.defense_025x_less)
        print('This attribute will immunity damage from these attribute(s): ', self.defense_00x)
        pass
    pass


class pokemon(object):
    def __init__(self, attribute, egg_group):
        self.attribute = attribute
        self.egg_group = egg_group
        self.attribute_ture = []
        self.attribute_group = [Normal_attribute(), Fly_attribute(), Fire_attribute(), Psychic_attribute(), Water_attribute(),
                                Bug_attribute(), Electric_attribute(), Rock_attribute(), Grass_attribute(), Ghost_attribute(),
                                Ice_attribute(), Dragon_attribute(), Fight_attribute(), Dark_attribute(), Poison_attribute(),
                                Steel_attribute(), Ground_attribute(), Fairy_attribute()]
        self.edited_phase = Pokemon_attribute()
        self.attribute_group_key = ['Normal', 'Fly', 'Fire', 'Psychic', 'Water', 'Bug', 'Electric', 'Rock', 'Grass',
                                    'Ghost', 'Ice', 'Dragon', 'Fight', 'Dark', 'Poison', 'Steel', 'Ground', 'Fairy']
    def attribute_phase(self):
        if len(self.attribute)==1:
            print('This is a %s type Pokemon'%self.attribute)
            for i in range(len(self.attribute_group)):
                if self.attribute[0] == type(self.attribute_group[i]).__name__[0:len(self.attribute[0])]:
                    self.attribute_ture.append(self.attribute_group[i])
                    break
            for i in self.attribute_group_key:
                self.attribute_ture[0].phase_edit()
                self.edited_phase.attack_phase[i] *= self.attribute_ture[0].attack_phase[i]
                self.edited_phase.defense_phase[i] *= self.attribute_ture[0].defense_phase[i]
            self.edited_phase.attack_2x = self.attribute_ture[0].attack_2x
            self.edited_phase.attack_05x = self.attribute_ture[0].attack_05x
            self.edited_phase.attack_00x = self.attribute_ture[0].attack_00x
            self.edited_phase.defense_2x = self.attribute_ture[0].defense_2x
            self.edited_phase.defense_05x = self.attribute_ture[0].defense_05x
            self.edited_phase.defense_00x = self.attribute_ture[0].defense_00x
        elif len(self.attribute)!=1:
            print('This is a %s type Pokemon'%self.attribute)
            for j in range(len(self.attribute)):
                for i in range(len(self.attribute_group)):
                    if self.attribute[j] == type(self.attribute_group[i]).__name__[0:len(self.attribute[j])]:
                        self.attribute_ture.append(self.attribute_group[i])
            for i in range(len(self.attribute_ture)):
                self.attribute_ture[i].phase_edit()
                for j in self.attribute_group_key:
                    self.edited_phase.defense_phase[j] *= self.attribute_ture[i].defense_phase[j]
    pass

def pokemon_defense_judge(pokemon):
    pokemon.attribute_phase()
    pokemon_defense_phase = pokemon.edited_phase.defense_phase
    print(pokemon_defense_phase)
    # judge = 0
    # for i in pokemon_defense_phase.keys():
    #     if pokemon_defense_phase[i] == 0:
    #         judge += 6
    #     elif po
    return
# atk, defen = phase_relationship('aba')
# a = Water_attribute()
# print(a.attack_phase)
# a.phase_edit()
# print(a.attack_phase)
# a.attack_phase_show()

b = pokemon(['Normal', 'Fly', 'Fire', 'Psychic', 'Water', 'Bug', 'Electric', 'Rock',
                                    'Ghost', 'Dragon', 'Fight', 'Dark', 'Poison', 'Steel', 'Ground', 'Fairy'], 'fish')
# print(b.edited_phase.attack_phase.keys())
pokemon_defense_judge(b)
# print(type(b.attribute_group[0]).__name__)
# b.attribute_phase()
# print(b.edited_phase.attack_phase)
# print(b.edited_phase.defense_phase)
# b.edited_phase.attack_phase_show()
# b.edited_phase.defense_phase_show()
# print(len(b.attribute_ture), type(b.attribute_ture[1]))
# print(b.edited_phase.defense_phase)
# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# print(len(b.attribute_ture))
# b.attribute_ture[0].attack_phase_show()
# b.attribute_ture[0].phase_edit()
# print(b.attribute_ture[0].attack_phase)
# b.attribute_ture[1].attack_phase_show()
# print(b.attribute_ture[1].attack_phase)
# print(b.attribute_ture)
