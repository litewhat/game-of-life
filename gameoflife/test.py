from cell import Cell
import time


def create_cells(initial_state, board_size):
    rows, columns = board_size
    colony = []
    for row in range(rows):
        for column in range(columns):
            c = Cell((row, column), False)
            colony.append(c)
            if (row, column) in initial_state:
                c.born()
    manager = colony[0].manager
    return manager


board_size = (20, 20)
initial_state = [(3, 3), (3, 4), (3, 5), (4, 3), (5, 4),
                 (7, 7), (7, 8), (7, 9), (8, 7), (9, 8)]
survive_when = (1, )
born_when = (1, )
iterations = 10

manager = create_cells(initial_state, board_size)
manager.rules = [survive_when, born_when]

states = []

while True:
    rows, columns = board_size
    for row in range(rows):
        for column in range(columns):
            cell = manager.get((row, column))
            if cell.is_alive:
                print('* ', end='')
            else:
                print('  ', end='')
        print()

    all_cells = manager.all()
    next_state = []
    for cell in all_cells:
        future = manager.future(cell)
        next_state.append((cell, future))

    for state in next_state:
        cell, cell_state = state
        if cell_state == 'will die':
            cell.die()
        elif cell_state == 'will born':
            cell.born()
    print('-------------------')
    states.append(next_state)
    time.sleep(1/4)
