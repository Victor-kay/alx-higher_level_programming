#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak must be on the left side
            right = mid
        else:
            # Peak must be on the right side
            left = mid + 1

    return list_of_integers[left]
