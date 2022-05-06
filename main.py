import species, jobs

from random import randint

class Dice():
    def __init__(self, faces) -> int:
        '''Generate a x faces dice'''
        self.faces = int(faces)
    def roll(self):
        return randint(1, self.faces)

dado = Dice(6)
print(dado.roll())

class NPC():
    def __init__(self, specie, gender, name):
        '''Generate a character with: specie, gender, name'''
        self.specie = specie
        self.gender = gender
        self.name = name

class Character():
    def __init__(self, specie, gender, name) -> str:
        '''Generate a character with: specie, gender, name'''
        self.specie = specie
        self.gender = gender
        self.name = name
        self.job = None
        self.stats = None
    def take_damage(self):
        pass
    def attack(self, skill, target):
        '''Attack target with a skill'''
