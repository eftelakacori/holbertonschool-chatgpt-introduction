#!/usr/bin/python3
def print_board(board):
    """
    Prints the current game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the current board.

    Parameters:
    board (list): A 3x3 list representing the game board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Checks if the board is full (no empty spaces).

    Parameters:
    board (list): A 3x3 list representing the game board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            # Get valid row and column input
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate the input range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be 0, 1, or 2. Try again.")
                continue

            # Check if the spot is already taken
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make the move
            board[row][col] = player

            # Check for a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Check for a draw
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")
        except IndexError:
            print("Invalid input. Row and column must be 0, 1, or 2. Try again.")

tic_tac_toe()
