#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """The write_file function"""

    # Opening and reading the file
    with open(filename, 'r', encoding='UTF-8') as f:
        read_data = f.read()
        print(read_data, end='')
