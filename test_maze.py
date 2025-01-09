import unittest
from maze import Maze
from window import Window



class Tests(unittest.TestCase):

    def test_maze_offset2_greater_than_window(self):
        win = Window(0, 0)
        num_cols = 12
        num_rows = 10
        with self.assertRaises(Exception, msg="Expected Exception"):
            maze_1 = Maze(win, num_rows, num_cols)


    def test_maze_create_cells(self):
        win = Window(500, 500)
        num_cols = 5
        num_rows = 5
        maze_1 = Maze(win, num_rows, num_cols)
        self.assertEqual(len(maze_1.cells), num_cols)
        self.assertEqual(len(maze_1.cells[0]), num_rows)


    def test_break_entrance_and_exit(self):
        win = Window(500, 500)
        num_cols = 5
        num_rows = 5
        maze_1 = Maze(win, num_rows, num_cols)
        self.assertEqual(maze_1.cells[0][0].has_left_wall, False)     
        self.assertEqual(maze_1.cells[-1][-1].has_right_wall, False)     




if __name__ == "__main__":
    unittest.main()