from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)

    m = Maze(0, 0, 12, 15, 50, 50, win)
    m.solve()
    win.wait_for_close()


main()
