from window import Line, Point


class Cell:

    def __init__(self, window, x1, y1, x2, y2, left=True, right=True, top=True, bottom=True):
        
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom

        # x1y1 (top-left) to x2y2 (bottom-right)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self.center = Point(x1 + (x2 - x1)/2, y1 + (y2 - y1)/2)

        self._win = window


    def draw(self, fill_color="black"):

        if self._win == None:
            raise Exception(f"No window set for {self}.")

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color)            
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, fill_color)


    # debug method to check if the center is at the right place
    def draw_center(self):
        line = Line(self.center, Point(self.center.x + 1, self.center.y +1))
        self._win.draw_line(line, "red")


    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        self._win.draw_line(line, fill_color)

