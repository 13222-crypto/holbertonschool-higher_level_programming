#!/usr/bin/python3
"""
This module solves the N-queens puzzle using backtracking.
The N-queens puzzle is the challenge of placing N non-attacking queens
on an N x N chessboard.
"""
import sys


def init_board(n):
    """Initializes an empty board representation."""
    return []


def is_safe(board, row, col):
    """
    Checks if a queen can be safely placed at board[row][col].

    Args:
        board (list): Current queen positions as [row, col] pairs.
        row (int): Target row index.
        col (int): Target column index.

    Returns:
        bool: True if safe, False otherwise.
    """
    for q_row, q_col in board:
        if q_col == col:
            return False
        if abs(q_row - row) == abs(q_col - col):
            return False
    return True


def solve_nqueens(n, row, board):
    """
    Utilizes backtracking to find all safe configurations.

    Args:
        n (int): Size of the board.
        row (int): Current row being evaluated.
        board (list): Accumulator of current safe positions.
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board)
            board.pop()


def validate_input():
    """
    Validates command-line arguments.

    Returns:
        int: The validated board size N.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


if __name__ == "__main__":
    n_size = validate_input()
    current_board = init_board(n_size)
    solve_nqueens(n_size, 0, current_board)
