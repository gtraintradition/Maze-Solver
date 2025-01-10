from window import Window
from maze import Maze



def main():
    
    win = Window(800, 600)
    ######
 
    maze_1 = Maze(win, 10, 10, seed=0)



    ######
    win.wait_for_close()


if __name__ == "__main__":
    main()
