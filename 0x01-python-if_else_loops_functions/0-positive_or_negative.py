#!/usr/bin/python3
import random

if __name__ == "__main__":
    number = random.randint(-100, 100)

    print(number)
    if number > 0:
        print("is positive")
    elif number == 0:
        print("is zero")
    else:
        print("is negative")
