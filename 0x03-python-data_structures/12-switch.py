#!/usr/bin/python3

def switch(a, b):
    """Switch the values of a and b."""
    a, b = b, a
    return a, b

a = 10
b = 20
a, b = switch(a, b)
print("a =", a)
print("b =", b)
