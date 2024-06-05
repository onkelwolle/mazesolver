from graphics import Point, Line

class Cell:
    def __init__(self, win):
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_left_wall = True
        self.has_bottom_wall = True 
        self._win = win
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False

    def draw(self, _x1, _y1, _x2, _y2, fill_color):
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2

        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y2), Point(self._x2, self._y1)), fill_color)
        else:
            self._win.draw_line(Line(Point(self._x2, self._y2), Point(self._x2, self._y1)), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        if self._x1 == None or self._x2 == None or self._y1 == None or self._y2 == None:
            Exception("need to set top left and bottom right corners through draw method")
        self._win.draw_line(Line(Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)), fill_color)
