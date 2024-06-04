from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)

    m = Maze(10, 10, 12, 15, 50, 50, win)
    m._break_entrance_and_exit()
    win.wait_for_close()


main()
