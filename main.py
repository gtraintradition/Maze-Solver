from window import Window, Line, Point



def main():
    win = Window(800, 600)

    point_1 = Point(100, 100)
    point_12 = Point(150, 200)
    point_2 = Point(400, 300)
    point_21 = Point(550, 600)
    point_3 = Point(400, 400)
    point_31 = Point(800, 400)

    line_1 = Line(point_1, point_12)
    line_2 = Line(point_2, point_21)
    line_3 = Line(point_3, point_31)

    win.draw_line(line_1, "red")
    win.draw_line(line_2, "blue")
    win.draw_line(line_3, "green")

    win.wait_for_close()


if __name__ == "__main__":
    main()
