#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    # Extract the first two elements from each tuple or use 0 if not present
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Calculate the sum of corresponding elements and return the result as a tuple
    result = (a[0] + b[0], a[1] + b[1])
    return result
