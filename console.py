class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1
    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.display()
        while True:
            row, col = self.current_player.get_move()
            if self.board.is_valid_move(row, col):
                self.board.make_move(row, col, self.current_player.symbol)
                self.board.display()
                if self.board.is_winner(self.current_player.symbol):
                    print(f"{self.current_player.name} wins!")
                    break
                elif self.board.is_full():
                    print("The game is a tie!")
                    break
                else:
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            else:
                print("Invalid move. Try again.")
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
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def get_move(self):
        row = int(input(f"{self.name}, enter row number (0-2): "))
        col = int(input(f"{self.name}, enter column number (0-2): "))
        return row, col
    
game = TicTacToe()
game.play()