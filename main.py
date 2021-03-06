import species, jobs, items, story

from random import randint
from time import sleep
import sys, os

def log(message):
    '''Game log'''
    message = str(message).replace('_', ' ').title()
    print(message)

def read_sentence(text, seconds = 0.2, clear_time = 3):
    print('')
    for character in text:
        print(character, end = '')
        sys.stdout.flush()
        sleep(seconds)
    if text in list(story.questions):
        print('')
        answers = story.questions[text]
        n = 0
        for answer in answers:
            n += 0
            print(n, ' -> ', answer)
        number = input('\nEnter a number: ')
        return answers[number - 1]
    sleep(clear_time)
    os.system('cls')

class Dice():
    def __init__(self, faces):
        '''Generate a x faces dice'''
        self.faces = int(faces)
        log('dice D{} created'.format(faces))
    def roll(self) -> int:
        face = randint(1, self.faces)
        log('dice rolled (Face: {}/{})'.format(face, self.faces))
        return face

class Character():
    def __init__(self, specie, gender, name):
        '''Generate a character with: specie, gender, name'''
        self.specie = specie
        self.gender = gender
        self.name = name
        self.job = None
        self.stats = species.superiors.species[specie]
        self.gold = 0
        self.bag = []
        self.equipped = {
            'weapon' : None,
            'shield' : None,
            'helmet' : None,
            'armor' : None,
            'gloves' : None,
            'pants' : None,
            'boots' : None,
        }
        log('{} character {} created'.format(specie, self.name))
    def add_stats(self, stats):
        pass
    def remove_stats(self, stats):
        pass
    def set_job(self, job):
        '''Set Job'''
        pass
    def get_item(self, item_name):
        '''Get item'''
        item = items.items[item_name]
        if self.stats['max_cap'] - self.stats['cap'] > item['cap']:
            self.bag.append(item_name)
            self.stats['cap'] += item['cap']
            log('{} get {} (Cap: {}/{})'.format(self.name, item_name, self.stats['cap'], self.stats['max_cap']))
        else:
            log('{} is full'.format(self.name))
    def equip_item(self, item_name):
        pass
    def unequip_item(self, item_name):
        pass
    def damaged(self, damage):
        '''Lost damage'''
        if self.stats['life'] > damage:
            self.stats['life'] -= damage
            log('{} lost {} damage (Life: {}/{})'.format(self.name, damage, self.stats['life'], self.stats['max_life']))
        else:
            self.stats['life'] = 0
            log('{} died'.format(self.name))

class Story():
    def __init__(self):
        self.chapter = 1
        self.choices = []
        self.story = story.chapters

# Tests:
def test_combat():
    dice = Dice(20)
    sleep(1)
    player1 = Character('elf', 'm', 'legolas')
    sleep(1)

    while player1.stats['life'] > 0:
        damage = dice.roll()
        player1.damaged(damage)
        sleep(1)

def test_get_items():
    player1 = Character('elf', 'm', 'legolas')
    sleep(1)
    item1 = 'leather_armor'
    item1_stats = items.items[item1]

    while player1.stats['max_cap'] - player1.stats['cap'] > item1_stats['cap']:
        player1.get_item(item1)
        sleep(1)
    player1.get_item(item1)

def test_story():
    tale = Story()
    text_title = list(tale.story)[0]
    text = tale.story[text_title]
    read_sentence(text[0])
    read_sentence(text[1])
    read_sentence(text[2])
    print(read_sentence(text[3]))

#test_combat()
#test_get_items()
test_story()
