# Third-party imports:
from random import randint

# local imports:
from settings import *
import creatures

# Translations:


class Dice():
    def __init__(self, faces):
        '''Generate a x faces dice'''
        self.faces = int(faces)
        log('dice D{} created'.format(faces))
    def roll(self) -> int:
        face = randint(1, self.faces)
        log('dice rolled (Face: {}/{})'.format(face, self.faces))
        return face

class Creature():
    def __init__(self):
        self.stats = creatures.base
    def add_stats(self, stats):
        self.stats.update(dict(stats))
    def set_name(self, name):
        self.stats['name'] = str(name).title()
    def attack(creature, skill = None):
        pass

# Tests:
player = Creature()
print()
print(player, '\n')
print('TIPO:', type(player.stats), '\n')
player.set_name('Leandro')
print('NOME:', player.stats['name'], '\n')
print('LINGUAGEM:', LANGUAGE, 'LINGUAGENS:', LANGUAGES, 'Diretório:', LANGUAGE_DIR)

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
