import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + self.cell_size_x * i
        y1 = self.y1 + self.cell_size_y * j
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2, "black")
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j].visited:
               to_visit.append((i - 1, j))

            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_cell_index = random.randrange(len(to_visit))
            next_cell = to_visit[next_cell_index]

            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, col, row):
        self._animate()
        self._cells[col][row].visited = True
        if col == self.num_cols - 1 and row == self.num_rows - 1:
            return True
        
        if col > 0 and not self._cells[col][row].has_left_wall and not self._cells[col - 1][row].visited:
            self._cells[col][row].draw_move(self._cells[col - 1][row])
            res = self._solve_r(col - 1, row)
            if res:
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col - 1][row], True)

        if col < self.num_cols and not self._cells[col][row].has_right_wall and not self._cells[col + 1][row].visited:
            self._cells[col][row].draw_move(self._cells[col + 1][row])
            res = self._solve_r(col + 1, row)
            if res:
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col + 1][row], True)


        if row > 0 and not self._cells[col][row].has_top_wall and not self._cells[col][row - 1].visited:
            self._cells[col][row].draw_move(self._cells[col][row - 1])
            res = self._solve_r(col, row - 1)
            if res:
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col][row - 1], True)

        if row < self.num_rows and not self._cells[col][row].has_bottom_wall and not self._cells[col][row + 1].visited:
            self._cells[col][row].draw_move(self._cells[col][row + 1])
            res = self._solve_r(col, row + 1)
            if res:
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col][row + 1], True)

        return False

        
