#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()
