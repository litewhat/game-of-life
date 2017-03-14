from cell import Cell
import unittest


class TestCellManager(unittest.TestCase):

    def setUp(self):
        self.colony = []
        for x in range(4):
            for y in range(4):
                self.colony.append(Cell((x, y), False))
        self.manager = self.colony[0].manager
        self.tested_cell = self.manager.get((1, 1))
        self.tested_cell.born()

    def test_neighbours(self):
        positions = [(0, 0), (0, 1), (0, 2), (1, 0),
                     (1, 2), (2, 0), (2, 1), (2, 2)]
        neighbours_should_be = [self.manager.get(position)
                                for position in positions]
        self.assertEqual(self.manager.get_neighbours(self.tested_cell),
                         neighbours_should_be)

    def test_living_cells(self):
        self.assertIn(self.tested_cell, self.manager.living_cells())

    def test_all_cells_have_the_same_manager(self):
        for cell in self.colony:
            self.assertEqual(self.manager, cell.manager)

    def test_significant_cells(self):
        positions = [(0, 0), (0, 1), (0, 2), (1, 0),
                     (1, 2), (2, 0), (2, 1), (2, 2),
                     (1, 1)]
        significant_cells = [self.manager.get(position)
                             for position in positions]
        tested_cells = self.manager.get_significant_cells()
        self.assertEqual(len(significant_cells), len(tested_cells))
        for cell in tested_cells:
            self.assertIn(cell, significant_cells)

    def test_living_neighbours(self):
        cell = self.manager.get((0, 0))
        cell.born()
        living_neigbours = self.manager.get_living_neighbours(self.tested_cell)
        self.assertEqual(1, len(living_neigbours))
        cell.die()

if __name__ == '__main__':
    unittest.main()
