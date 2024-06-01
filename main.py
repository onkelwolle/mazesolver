from graphics import Window, Cell


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(5,5, 50, 50, "black")

    win.wait_for_close()


main()
