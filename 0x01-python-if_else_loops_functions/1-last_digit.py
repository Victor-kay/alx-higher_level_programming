#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of", end=" ")
print("{}".format(number), end=" ")
print("is", end=" ")

last_digit = abs(number) % 10

print(last_digit, end=" ")

if number < 0:
    last_digit *= -1

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
