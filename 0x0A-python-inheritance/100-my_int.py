#!/usr/bin/python3
"""Write a class MyInt that inherits from int:"""


class MyInt(int):
    """Write a class MyInt that inherits from int:"""

    def __eq__(self, value):
        """ override"""
        return self.real != value

    def __ne__(self, value):
        """ override"""
        return self.real == value
