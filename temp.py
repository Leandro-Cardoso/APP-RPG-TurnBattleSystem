from random import randint, shuffle

class Human():
    def __init__(self, name, gender):
        '''Create Human named by x'''
        self.description = ''
        self.isAlive = True
        self.name = name
        self.gender = gender
        self.level = 1
        self.exp = 0
        self.expNextLevel = 1000
        self.life = 100
        self.maxLife = 100
        self.mana = 100
        self.maxMana = 100
        self.speed = 5
        self.accuracy = 0.8
        self.physicalAttack = 10
        self.physicalResistance = 5
        self.magicAttack = 0
        self.magicResistance = 0
        self.gold = 0
        self.bag = []
    def levelUp(self, levels = 1):
        '''Level up (1 level or x levels)'''
        self.level += levels
        self.expNextLevel = int(self.expNextLevel * 1.5 ** levels)
        self.maxLife += 100 * levels
        self.maxMana += 100 * levels

class Dwarf(Human):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        '''Create Dwarf named by x'''
        self.description = 'Bem menor que um Humano normal, mas sua força compensa a altura. Se destaca por sua resistência física fora do normal, mas são lendos e não possuem muita capacidade mágica.'
        self.mana = 50
        self.maxMana = 50
        self.speed = 3
        self.accuracy = 0.6
        self.physicalAttack = 10
        self.physicalResistance = 7

class Elf(Human):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        '''Create Elf named by x'''
        self.description = ''
        self.life = 50
        self.maxLife = 50
        self.mana = 150
        self.maxMana = 150
        self.speed = 10
        self.accuracy = 1.0
        self.physicalResistance = 3
        self.magicResistance = 5

class Orc(Human):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        '''Create Orc named by x'''
        self.description = ''

class Monster():
    def __init__(self):
        self.description = ''

class Player():
    def __init__(self, name):
        '''Create Player named by x'''
        self.name = name
        self.created = None
        self.lastSave = None
        self.team = []

class TurnBattle():
    def __init__(self, alliedTeam, enemyTeam, playerStart = True, isAmbush = False):
        '''Create turn battle'''
        self.turns = 1
        self.playerStart = playerStart
        self.isAmbush = isAmbush
        self.alliedTeam = self.sortFightersSpeed(alliedTeam)
        self.enemyTeam = self.sortFightersSpeed(enemyTeam)
    def sortFightersSpeed(self, fighters):
        '''Sort fighters by speed'''
        # Shuffle fighters:
        shuffledIndices = list(range(len(fighters)))
        shuffle(shuffledIndices)
        shuffledFighters = []
        for i in shuffledIndices:
            shuffledFighters.append(fighters[i])
        # Get fighters speeds:
        speeds = []
        for i in range(0, len(shuffledFighters)):
            fighter = shuffledFighters[i]
            speeds.append(fighter.speed)
        # Sort fighters by speed:
        speeds = sorted(set(speeds), reverse = True)
        sortedFighters = []
        for speed in speeds:
            for fighter in shuffledFighters:
                if fighter.speed == speed:
                    sortedFighters.append(fighter)
        return sortedFighters

# TESTs
member1 = Human('Luna', 'f')
member2 = Dwarf('Pinga', 'm')
member3 = Elf('Legolas', 'm')
member4 = Orc('Grut', 'm')

player = Player('Leandro')
player.team = [member1, member2, member3, member4]
print(player.team)

battle = TurnBattle(player.team, player.team)
print(battle.alliedTeam)
