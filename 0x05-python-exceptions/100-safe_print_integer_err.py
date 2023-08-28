#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Print an integer and handle errors.

    Args:
        value: The value to be printed.

    Returns:
        True if the value is an integer and has been correctly printed, False otherwise.
    """
    try:
        value_as_int = int(value)
        print("{:d}".format(value_as_int))
        return True
    except ValueError:
        print("Exception: Invalid input. Value is not an integer.", file=sys.stderr)
        return False
