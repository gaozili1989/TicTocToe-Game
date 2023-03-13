from board import Board
from player import Player
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