class CellManager(object):
    'Represent a group of cells.'
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
        living_cells = [cell for cell in self.cells if cell.is_alive]
        return living_cells

    def get_living_neighbours(self, cell):
        'Returns list of living neighbours.'
        living_neighbours = [cell
                             for cell in self.get_neighbours(cell)
                             if cell.is_alive]
        return living_neighbours

    def get_neighbours(self, cell):
        'Returns neighbours of particular cell.'
        x, y = cell.position
        neighbours = [(k, l)
                      for k in range(x - 1, x + 2)
                      for l in range(y - 1, y + 2)]
        neighbours.remove(cell.position)
        return [self.get(neighbour) for neighbour in neighbours]

    def get_neighbours_of_living_cells(self):
        'Returns list of neighbours of living cells.'
        cells = set()
        for cell in self.living_cells():
            for neighbour in self.get_neighbours(cell):
                if neighbour is not None:
                    cells.add(neighbour)
        return list(cells)

    def get_significant_cells(self):
        'Returns list of significant cells.'
        cells = set()
        for cell in self.living_cells():
            cells.add(cell)
            for neighbour in self.get_neighbours(cell):
                if neighbour is not None:
                    cells.add(neighbour)
        return list(cells)


class Cell(object):
    'Represents cell object.'
    manager = CellManager()

    def __init__(self, position, is_alive=True):
        self.position = position
        self.is_alive = is_alive
        self.manager.cells.append(self)

    def __repr__(self):
        x, y = self.position
        return '<{} pos: {}, {}>'.format(self.__class__.__name__, x, y)

    def born(self):
        self.is_alive = True

    def die(self):
        self.is_alive = False
