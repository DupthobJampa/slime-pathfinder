class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = []
        for row in range(rows):
            self.cells.append([0] * cols)

        self.start = None
        self.goal = None

    def set_start(self,row,col):
        if self.cells[row][col] == 3:
            return

        if self.start is not None:
            old_row, old_col = self.start
            self.cells[old_row][old_col] = 0

        self.start = (row, col)
        self.cells[row][col] = 2

    def set_goal(self,row,col):
        if self.cells[row][col] == 2:
            return

        if self.goal is not None:
            old_row, old_col = self.goal
            self.cells[old_row][old_col] = 0

        self.goal = (row, col)
        self.cells[row][col] = 3

    def add_wall(self, row, col):
        if self.cells[row][col] not in (2, 3):
            self.cells[row][col] = 1

    def erase(self, row, col):
        if self.cells[row][col] == 2:
            self.start = None
        elif self.cells[row][col] == 3:
            self.goal = None
        self.cells[row][col] = 0
