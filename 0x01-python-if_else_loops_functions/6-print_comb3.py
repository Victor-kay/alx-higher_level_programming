#!/usr/bin/python3
# 6-print_comb3.py

for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        print("{:d}{:d}".format(tens_digit, units_digit), end="")
        if tens_digit != 8 or units_digit != 9:
            print(", ", end="")
        else:
            print()
