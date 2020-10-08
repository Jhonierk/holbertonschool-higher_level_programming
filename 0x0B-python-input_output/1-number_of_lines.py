#!/usr/bin/python3

"""Write a function that returns the number of lines of a text file:"""


def number_of_lines(filename=""):
    """Write a function that returns the number of lines of a text file:"""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
