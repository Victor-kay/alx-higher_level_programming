#!/usr/bin/python3
"""Solve the N queens problem."""


import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the left side of this row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """Solve the N queens problem."""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """Recursive function to find all solutions."""
    if col == n:
        # All queens are placed, print the solution
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0


def print_solution(board):
    """Print a solution in a specific format."""
    for row in board:
        print(" ".join(["Q" if col == 1 else "." for col in row]))
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
