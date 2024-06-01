from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100, "black")

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200, "black")

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250, "black")

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500, "black")
    win.wait_for_close()


main()
