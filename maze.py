import time, random

from cell import Cell



class Maze():

    def __init__(self,
                win,
                num_rows,
                num_cols,
                seed=None,
                offset=50
                 ):

        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__win = win
        self.__sleep_time = 0.05
        if num_cols * num_rows >= 2500:
            self.__sleep_time = 0.01
        if num_cols * num_rows >= 1000:
            self.__sleep_time = 0.0001
        self.cells = []
        if seed:
            random.seed(seed)
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

        # For debug initially but chose to keep it
        maze_borders = Cell(self.__win)
        maze_borders.draw(self.maze_x1, self.maze_y1, self.maze_x2, self.maze_y2, "pink")

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()


    def _create_cells(self):
        for i in range(self.__num_cols):
            cells_to_add = []
            for j in range(self.__num_rows):
                cells_to_add.append(Cell(self.__win))
            self.cells.append(cells_to_add)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):        
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self.__win == None:
            print(f"cant draw cell[{i}][{j}] because \"self._win\" == None")
            return

        x1 = i * self.__cell_size + self.maze_x1
        x2 = x1 + self.__cell_size
        y1 = j * self.__cell_size + self.maze_y1
        y2 = y1 + self.__cell_size 

        self.cells[i][j].draw(x1, y1, x2, y2)

        self._animate()


    def _animate(self):
        if self.__win == None:
            print(f"cant animate because \"self._win\" == None")
            return
        self.__win.redraw()
        time.sleep(self.__sleep_time)


    def _break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self.cells[-1][-1].has_right_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)


    def _break_walls_r(self, i, j):
        if i < 0 or j < 0:
            raise Exception(f"i ({i}) or j ({j}) cant be lower than 0")
            
        self.cells[i][j].visited = True

        while True:
            can_visit = []

            # right
            if i < self.__num_cols - 1 and self.cells[i + 1][j].visited == False:
                can_visit.append((i + 1, j))
            # left
            if i > 0 and self.cells[i - 1][j].visited == False:
                can_visit.append((i - 1, j))
            # top
            if j > 0 and self.cells[i][j - 1].visited == False:
                can_visit.append((i, j - 1))
            # bottom
            if j < self.__num_rows - 1 and self.cells[i][j + 1].visited == False:
                can_visit.append((i, j + 1))

            if len(can_visit) == 0:
                self._draw_cell(i, j)
                return

            next_cell = random.choice(can_visit)

            # right
            if next_cell[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if next_cell[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # top
            if next_cell[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False
            # bottom
            if next_cell[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    
    def _reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):        
                self.cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            print("reached the end")
            return True

        # right
        if (i < self.__num_cols - 1 
            and self.cells[i + 1][j].visited == False
            and self.cells[i][j].has_right_wall == False 
            and self.cells[i + 1][j].has_left_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i + 1][j], undo=True)
        # left
        if (i > 0 
            and self.cells[i - 1][j].visited == False
            and self.cells[i][j].has_left_wall == False 
            and self.cells[i - 1][j].has_right_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i - 1][j], undo=True)
        # top
        if (j > 0 
            and self.cells[i][j - 1].visited == False
            and self.cells[i][j].has_top_wall == False 
            and self.cells[i][j - 1].has_bottom_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j - 1], undo=True)
        # bottom
        if (j < self.__num_rows - 1 
            and self.cells[i][j + 1].visited == False
            and self.cells[i][j].has_bottom_wall == False 
            and self.cells[i][j + 1].has_top_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j + 1], undo=True)

        return False
