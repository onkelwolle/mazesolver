from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_bottom_wall = False
    c1.draw(50, 50, 100, 100, "black")

    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(50, 101, 100, 151, "black")

    c1.draw_move(c2)
    win.wait_for_close()


main()
