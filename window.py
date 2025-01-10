from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill="both", expand=1)
        self.__is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.width = width
        self.height = height
        self.center = Point(width /2, height/2)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()


    def close(self):
        self.__is_running = False


    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(Point):
    
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)



