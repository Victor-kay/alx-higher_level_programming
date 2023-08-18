#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./your_program_name.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        result = a + b
    elif sys.argv[2] == "-":
        result = a - b
    elif sys.argv[2] == "*":
        result = a * b
    elif sys.argv[2] == "/":
        if b == 0:
            print("Error: Division by zero.")
            sys.exit(1)
        result = a / b
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
