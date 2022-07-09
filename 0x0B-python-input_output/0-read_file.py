#!/usr/bin/python3

"""
    this function reads files passed to it as arguments
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
