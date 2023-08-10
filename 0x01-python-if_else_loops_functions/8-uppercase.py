#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase."""
    for c in s:
        print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")
    print("")
