from graphics import Point, Line

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
