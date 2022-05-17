# Third-party imports:
from random import randint

# local imports:
import creatures

class Dice():
    def __init__(self, faces):
        '''Generate a x faces dice'''
        self.faces = int(faces)
    def roll(self) -> int:
        face = randint(1, self.faces)
        return face

class Creature():
    def __init__(self):
        self.stats = creatures.base
    def add_stats(self, stats):
        self.stats.update(dict(stats))
    def set_name(self, name):
        self.stats['name'] = str(name).title()
    def level_up(self, levels = 1):
        self.stats['full hp'] = int(self.stats['full hp'] / self.stats['level'] * (self.stats['level'] + levels))
        self.stats['full mp'] = int(self.stats['full mp'] / self.stats['level'] * (self.stats['level'] + levels))
        self.stats['level'] += int(levels)
        self.stats['full exp'] = int(self.stats['full exp'] * 1.5 ** levels)
    def win_exp(self, exp):
        self.stats['exp'] += int(exp)
        while self.stats['exp'] >= self.stats['full exp']:
            self.stats['exp'] -= self.stats['full exp']
            self.level_up()
    def attack(creature, skill = None):
        pass

# Tests:
player = Creature()
print()
player.set_name('Leandro')
print('NOME:', player.stats['name'])
player.add_stats(creatures.elf)
print('CRIATURA:', player.stats['creature'], '\n')

player.level_up()
print('LV:', player.stats['level'])
print('EXP: {}/{}'.format(player.stats['exp'], player.stats['full exp']))
print('HP:', player.stats['full hp'])
print('MP:', player.stats['full mp'])

player.win_exp(3850)
print('\nLV:', player.stats['level'])
print('EXP: {}/{}'.format(player.stats['exp'], player.stats['full exp']))
print('HP:', player.stats['full hp'])
print('MP:', player.stats['full mp'])
print()

# INTERFACE DINAMICA NA WEB <-- PARA FUTURO

# VERSÃO PT-BR E EN-US, COM SUPORTE A TRADUÇÕES
    # HORARIO UTC (Coordinated Universal Time) E LOCAL E DATA

# INTERFACE DE TERMINAL
    # TELA DE TEXTO COM TITULO DO CAPITULO FIXO
    # TELA DE MENU
    # TELA DE BATALHA POR TURNOS

# INICIO DA HISTORIA

# CRIAÇÃO DO PERSONAGEM
    # STATS BASICOS VER O FF-X E FF-X-2

# CONTINUAÇÃO DA HISTÓRIA (PREPARAÇÃO PARA PRIMEIRA BATALHA)

# BATALHA (1 vs 2)
    # CALCULOS DE DANO, EVASÃO E DEFESA

# CRIAR PROGRAMA PARA CRIAR MUSICA E SINTETIZAR
    # TEMA 8 E 16 BITS
