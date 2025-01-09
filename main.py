from window import Window, Line, Point
from cell import Cell




def main():
    
    win = Window(800, 600)

    cell_1 = Cell(win, 20, 100, 100, 20, left=False)
    cell_2 = Cell(win, 20, 200, 100, 120, right=False)
    cell_3 = Cell(win, 20, 300, 100, 220, top=False)
    cell_4 = Cell(win, 20, 400, 100, 320, bottom=False)
    cell_5 = Cell(win, 20, 500, 100, 420, left=False, right=False, top=False)


    cell_1.draw("red")
    cell_2.draw("blue")
    cell_3.draw("green")
    cell_4.draw("purple")
    cell_5.draw("yellow")


    win.wait_for_close()


if __name__ == "__main__":
    main()
