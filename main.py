# playing with recursion limit for 100 * 100 maze
import sys

from window import Window
from maze import Maze




def main():
    sys.setrecursionlimit(10000)
    
    win = Window(800, 600)
    ######
 
    maze_1 = Maze(win, 10, 10, seed=0)



    ######
    win.wait_for_close()


if __name__ == "__main__":
    main()
