from .armor import armor

items = {}
items.update(armor)

# Tests:
if __name__ == '__main__':
    for item in list(items):
        old_stats = str(items[item])
        remove_chars = "{'}"
        stats = ''.join(filter(lambda i: i not in remove_chars, old_stats))
        print(item, '->', stats)
