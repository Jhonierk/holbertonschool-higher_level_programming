#!/usr/bin/python3
"""Write a function that reads n lines
of a text file (UTF8) and prints it to stdout:"""


def read_lines(filename="", nb_lines=0):
    """Write a function that reads n lines
     a text file (UTF8) and prints it to stdout:"""

    """ Full content"""
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        lines = 0
        for line in f:
            lines += 1
        f.seek(0)
        if nb_lines >= lines:
            print(f.read(), end="")
            return
        else:
            n = 0
            while n < nb_lines:
                print(f.readline(), end="")
                n += 1
