# Variable Stats:
def update_variable_stats(stats):
    '''Update variable stats'''
    stats['max_cap'] = stats['strength'] * 10
    stats['speed'] = 0 if (stats['max_cap'] < stats['cap']) else int(stats['max_speed'] * (100 - 100 * stats['cap'] / stats['max_cap']) / 100)

# Stats:
elf_stats = {
    'description' : 'No description',
    'life' : 100,
    'max_life' : 100,
    'energy' : 150,
    'max_energy' : 150,
    'strength' : 10,
    'cap' : 0,
    'max_speed' : 80,
}
update_variable_stats(elf_stats)
orc_stats = {
    'description' : 'No description',
    'life' : 150,
    'max_life' : 150,
    'energy' : 100,
    'max_energy' : 100,
    'strength' : 15,
    'cap' : 0,
    'max_speed' : 50,
}

# Species:
species = {
    'elf' : elf_stats,
    'orc' : orc_stats,
}

# Tests:
if __name__ == '__main__':
    print('ELFO ->     Capacidade: {}/{}     Velocidade: {}'.format(int(elf_stats['cap']), elf_stats['max_cap'], elf_stats['speed']))
    while elf_stats['max_cap'] > elf_stats['cap']:
        elf_stats['cap'] += 5
        update_variable_stats(elf_stats)
        print('ELFO ->     Capacidade: {}/{}     Velocidade: {}'.format(int(elf_stats['cap']), elf_stats['max_cap'], elf_stats['speed']))
