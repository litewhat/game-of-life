import random
from cell import Cell

c = Cell((1, 1))
neighbours_should_be = [(0, 0),
                        (0, 1),
                        (0, 2),
                        (1, 0),
                        (1, 2),
                        (2, 0),
                        (2, 1),
                        (2, 2)]
assert c.get_neighbours() == neighbours_should_be, 'Wrong!'


def test_create_colony():
    colony = []
    _bools = (True, False)
    for x in range(10):
        for y in range(10):
            alive = random.choice(_bools)
            colony.append(Cell((x, y), colony, alive))
    return colony

cells = test_create_colony()
man = cells[0].manager
assert man == cells[1].manager
nog = man.get_neighbours_of_group()
