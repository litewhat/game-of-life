import random
from cell import Cell

colony = []
_bools = (True, False)
for x in range(10):
    for y in range(10):
        alive = random.choice(_bools)
        colony.append(Cell((x, y), colony, alive))

manager = colony[0].manager

for y in range(10):
    for x in range(10):
        c = manager.get((x, y))
        if c.is_alive:
            print('* ', end='')
        else:
            print('  ', end='')
    print('')
