
class Board:
    def __init__(self):
        self.grid = [[" ", " ", " "] for _ in range(3)]
    def display(self):
        for row in self.grid:
            print("|".join(row))
    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == " "
    def make_move(self, row, col, symbol):
        self.grid[row][col] = symbol
    def is_full(self):
        for row in self.grid:
            if " " in row:
                return False
        return True
    def is_winner(self, symbol):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == symbol:
                return True
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == symbol:
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == symbol:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == symbol:
            return True
        return False