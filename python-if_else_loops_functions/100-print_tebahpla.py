#!/usr/bin/python3
for i in range(90, 64, -1):
    print(chr(i % 2 * 32 + i), end='')
