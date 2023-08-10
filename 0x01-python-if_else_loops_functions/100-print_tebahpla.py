#!/usr/bin/python3
# 100-print_tebahpla.py

for char in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - char) % 2 == 0:
        print("{}".format(chr(char).lower()), end="")
    else:
        print("{}".format(chr(char).upper()), end="")
