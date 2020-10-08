#!/usr/bin/python3
"""Write a class Student that defines a student by:"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """ Inicialitation
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for i, j in json.items():
            setattr(self, i, j)
