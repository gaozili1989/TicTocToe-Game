class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def get_move(self):
        row = int(input(f"{self.name}, enter row number (0-2): "))
        col = int(input(f"{self.name}, enter column number (0-2): "))
        return row, col