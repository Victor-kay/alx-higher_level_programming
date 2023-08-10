#!/usr/bin/python3
# 7-islower.py

def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False

# Test cases
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('7'))  # False
