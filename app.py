class Human():
    def __init__(self, name):
        '''Create Human named by x'''
        self.isAlive = True
        self.name = name
        self.level = 1
        self.exp = 0
        self.expNextLevel = 1000
        self.life = 500
        self.maxLife = 500
        self.mana = 500
        self.maxMana = 500
        self.speed = 100
        self.accuracy = 0.5
        self.physicalAttack = 100
        self.physicalResistance = 50
        self.gold = 0
        self.bag = []
    def levelUp(self, levels = 1):
        '''Level up (1 level or x levels)'''
        self.level += levels
        self.expNextLevel = int(self.expNextLevel * 1.5 ** levels)
        self.maxLife += 100 * levels
        self.maxMana += 100 * levels

class Dwarf(Human):
    def __init__(self, name):
        super().__init__(name)
        '''Create Dwarf named by x'''

class Elf(Human):
    def __init__(self, name):
        super().__init__(name)
        '''Create Elf named by x'''

class Orc(Human):
    def __init__(self, name):
        super().__init__(name)
        '''Create Orc named by x'''

class Monster():
    def __init__(self):
        pass

class Player():
    def __init__(self, name):
        '''Create Player named by x'''
        self.name = name
        self.created = None
        self.lastSave = None
        self.team = []

class TurnBattle():
    def __init__(self, alliedTeam, enemyTeam, playerStart = True, isAmbush = False):
        self.turns = 1
        self.playerStart = playerStart
        self.isAmbush = isAmbush
        self.alliedTeam = self.sortFightersSpeed(alliedTeam)
        self.enemyTeam = self.sortFightersSpeed(enemyTeam)
    def sortFightersSpeed(fighters):
        '''Sort fighters by speed'''
        speeds = []
        for fighter in fighters:
            pass

# TESTs
player = Elf('Leandro')
player.levelUp()
print(player.name, player.level, player.expNextLevel, player.maxLife)
player.levelUp(2)
print(player.name, player.level, player.expNextLevel, player.maxLife)
