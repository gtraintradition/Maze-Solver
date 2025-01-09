from window import Window, Line, Point
from cell import Cell
from maze import Maze



def main():
    
    win = Window(800, 600)
    ######
 
    maze_1 = Maze(win, 10, 10)

    #maze_1._create_cells()

    ######
    win.wait_for_close()


if __name__ == "__main__":
    main()
