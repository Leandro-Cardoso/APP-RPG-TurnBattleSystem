from settings import *

# Translation:
def translate_creature(creature) -> list:
    creature += '> '
    file = open(LANGUAGE_DIR + 'creatures_description.txt', 'r')
    lines = file.readlines()
    for line in lines:
        if creature in line:
            creature_name = line.replace(creature, '')
            creature_description = lines[lines.index(line) + 1]
            return (creature_name, creature_description)

# Base:
base = {
    'name' : None,
    'bag' : [],
    'coins' : 0,
    'level' : 1,
    'exp' : 0,
    'full exp' : 1000,
    'cap' : 0,
}
# Superiors creatures:
elf = {
    'creature' : translate_creature('elf')[0],
    'creature description' : translate_creature('elf')[1],
    'hp' : 100,
    'full hp' : 100,
    'mp' : 150,
    'full mp' : 150,
}
orc = {
    'creature' : 'Orc',
    'creature description' : '',
    'hp' : 150,
    'full hp' : 150,
    'mp' : 100,
    'full mp' : 100,
}
human = {
    'creature' : 'Human',
    'creature description' : '',
    'hp' : 125,
    'full hp' : 125,
    'mp' : 125,
    'full mp' : 125,
}
dwarf = {
    'creature' : 'Dwarf',
    'creature description' : '',
    'hp' : 200,
    'full hp' : 200,
    'mp' : 50,
    'full mp' : 50,
}
# Lendary creatures:
# Dimensional creatures:
# Common creatures:
