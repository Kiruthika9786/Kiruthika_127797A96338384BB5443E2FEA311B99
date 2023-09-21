inv = [
    'Gem',
    'Sword',
    'Shield',
    'Health potion'
]

indx = inv.index('Gem')
item = inv.pop(indx)
inv.append(item)

print(inv)
