class CellManager(object):
    '''Represent a group of cells.'''

    cells = []

    def all(self):
        return self.cells

    def get(self, position):
        'Return cell which has given position.'
        for cell in self.cells:
            if cell.position == position:
                return cell
        else:
            return None

    def living_cells(self):
        'Returns list of living cells.'

        _cells = [cell for cell in self.cells if cell.is_alive]
        return _cells

    def get_neighbours_of_group(self, of_living=True):
        'Gets set of neighbours of given group of cells.'''

        if of_living:
            _neighbours = []
            for cell in self.cells:
                if cell.is_alive:
                    for neighbour in cell.get_neighbours():
                        _neighbours.append(neighbour)
            return [self.get(position)
                    for position in set(_neighbours)
                    if self.get(position) is not None]
        return {self.get(neighbour)
                for cell in self.cells
                for neighbour in cell.get_neighbours()
                if self.get(neighbour) is not None}


class Cell(object):
    '''Represents cell object.'''

    manager = CellManager()

    def __init__(self, position, colony=None, is_alive=True):
        self.position = position
        self.colony = colony
        self.is_alive = is_alive
        self.neighbours = None
        self.manager.cells.append(self)

    def born(self):
        self.is_alive = True

    def die(self):
        self.is_alive = False

    def get_neighbours(self):
        'Returns list of postions of its neighbours.'

        if self.neighbours is None:
            x, y = self.position
            self.neighbours = [(k, l)
                               for k in range(x - 1, x + 2)
                               for l in range(y - 1, y + 2)]
            self.neighbours.remove(self.position)
        return self.neighbours
