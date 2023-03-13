from console import TicTacToe
def test_tic_tac_toe():
    # Test player 1 wins by getting three symbols in a row
    game = TicTacToe()
    game.board.grid = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
    game.current_player = game.player2
    assert game.board.is_winner(game.player1.symbol)
    assert not game.board.is_winner(game.player2.symbol)
    assert not game.board.is_full()

    # Test player 2 wins by getting three symbols in a column
    game = TicTacToe()
    game.board.grid = [["X", " ", "O"], ["X", " ", "O"], [" ", " ", "O"]]
    assert not game.board.is_winner(game.player1.symbol)
    assert game.board.is_winner(game.player2.symbol)
    assert not game.board.is_full()

    # Test player 1 wins by getting three symbols in a diagonal
    game = TicTacToe()
    game.board.grid = [["X", " ", "O"], [" ", "X", "O"], [" ", " ", "X"]]
    assert game.board.is_winner(game.player1.symbol)
    assert not game.board.is_winner(game.player2.symbol)
    assert not game.board.is_full()

    # Test game ends in a tie
    game = TicTacToe()
    game.board.grid = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", " "]]
    assert not game.board.is_winner(game.player1.symbol)
    assert not game.board.is_winner(game.player2.symbol)
    assert game.board.is_full()

    # Test player makes an invalid move
    game = TicTacToe()
    game.board.grid = [["X", " ", " "], [" ", "O", " "], [" ", " ", " "]]
    game.current_player = game.player2
    assert not game.board.is_valid_move(0, 0)
    assert game.board.is_valid_move(0, 1)
