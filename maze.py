import time

from cell import Cell
from window import Point, Line


class Maze():

    def __init__(self,
                win,
                num_rows,
                num_cols,
                offset=50
                 ):

        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__win = win
        self.cells = []
        self.__offset = offset

        if offset * 2 > win.width or offset * 2 > win.height:
            raise Exception(f"offset * 2 ({self.__offset} * 2) cant be more than window width ({self.__win.width}) or height ({self.__win.height})")
        
        self.__max_width = win.width - self.__offset * 2
        self.__max_height = win.height - self.__offset * 2

        if num_cols > num_rows:
            self.__cell_size = self.__max_width / num_cols
        else:
            self.__cell_size = self.__max_height / num_rows

        self.__width = self.__cell_size * num_cols
        self.__height = self.__cell_size * num_rows

        self.maze_x1 = win.center.x - (self.__width / 2)
        self.maze_x2 = win.center.x + (self.__width / 2)
        self.maze_y1 = win.center.y - (self.__height / 2)
        self.maze_y2 = win.center.y + (self.__height / 2)

        # Debug
        print(self.maze_x1)
        print(self.maze_x2)
        print(self.maze_y1)
        print(self.maze_y2)
        print(f"cell size = {self.__cell_size}")

        # Debug
        maze_top = Line(Point(self.maze_x1, self.maze_y1), Point(self.maze_x2, self.maze_y1))
        maze_bottom = Line(Point(self.maze_x1, self.maze_y2), Point(self.maze_x2, self.maze_y2))
        maze_left = Line(Point(self.maze_x1, self.maze_y1), Point(self.maze_x1, self.maze_y2))
        maze_right = Line(Point(self.maze_x2, self.maze_y1), Point(self.maze_x2, self.maze_y2))
        #win.draw_line(maze_top, "pink")
        #win.draw_line(maze_bottom, "pink")
        #win.draw_line(maze_left, "pink")
        #win.draw_line(maze_right, "pink")
        maze_borders = Cell(self.__win)
        maze_borders.draw(self.maze_x1, self.maze_y1, self.maze_x2, self.maze_y2, "pink")

        self._create_cells()
        self._break_entrance_and_exit()


    def _create_cells(self):
        for i in range(self.__num_cols):
            cells_to_add = []
            for j in range(self.__num_rows):
                cells_to_add.append(Cell(self.__win))
                self._draw_cell(cells_to_add[-1], i, j)
            self.cells.append(cells_to_add)


    def _draw_cell(self, cell, i, j):
        if self.__win == None:
            print(f"cant draw cell[{i}][{j}] because \"self._win\" == None")
            return

        x1 = i * self.__cell_size + self.maze_x1
        x2 = x1 + self.__cell_size
        y1 = j * self.__cell_size + self.maze_y1
        y2 = y1 + self.__cell_size 

        cell.draw(x1, y1, x2, y2)

        self._animate()


    def _animate(self):
        if self.__win == None:
            print(f"cant animate because \"self._win\" == None")
            return
        self.__win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self._draw_cell(self.cells[0][0], 0, 0)
        self.cells[-1][-1].has_right_wall = False
        self._draw_cell(self.cells[-1][-1], self.__num_cols - 1, self.__num_rows - 1)