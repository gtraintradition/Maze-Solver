from window import Line, Point


class Cell:

    def __init__(self, window, left=True, right=True, top=True, bottom=True):

        self._win = window       
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.visited = False

        # x1y1 is top-left, x2y2 is bottom-right
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self.__center = None


    def draw(self, x1, y1, x2, y2, fill_color="black"):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.__center = Point(x1 + (x2 - x1)/2, y1 + (y2 - y1)/2)


        if self._win == None:
            raise Exception(f"No window set for {self}.")


        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        left_fill_color = fill_color 
        if not self.has_left_wall:
            left_fill_color = "white"
        self._win.draw_line(line, left_fill_color)
        
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        right_fill_color = fill_color 
        if not self.has_right_wall:
            right_fill_color = "white"
        self._win.draw_line(line, right_fill_color)

        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        top_fill_color = fill_color  
        if not self.has_top_wall:
            top_fill_color = "white"
        self._win.draw_line(line, top_fill_color)       
        
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        bottom_fill_color = fill_color  
        if not self.has_bottom_wall:
            bottom_fill_color = "white"
        self._win.draw_line(line, bottom_fill_color)


    # debug method to check if the center is at the right place
    def draw_center(self):
        line = Line(self.__center, Point(self.__center.x + 1, self.__center.y +1))
        self._win.draw_line(line, "red")


    def draw_move(self, to_cell, undo=False):
        line = Line(self.__center, to_cell.__center)
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        self._win.draw_line(line, fill_color)


