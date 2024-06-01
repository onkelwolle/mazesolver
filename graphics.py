from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.running = False


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, __canvas, fill_color):
        __canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win):
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_left_wall = True
        self.has_bottom_wall = True 
        self._win = win

    def draw(self, _x1, _y1, _x2, _y2, fill_color):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(_x1, _y1), Point(_x1, _y2)), fill_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(_x1, _y2), Point(_x2, _y2)), fill_color)
        if self.has_right_wall:
            self._win.draw_line(Line(Point(_x2, _y2), Point(_x2, _y1)), fill_color)
        if self.has_top_wall:
            self._win.draw_line(Line(Point(_x1, _y1), Point(_x2, _y1)), fill_color)
