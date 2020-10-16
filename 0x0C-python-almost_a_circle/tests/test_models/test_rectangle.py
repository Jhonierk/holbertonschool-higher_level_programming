#!/usr/bin/python3
"""Unittest for base.py"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """unnittest"""

    def setUp(self):
        """ Put stdout and set rectangles"""
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()
        self.g1 = Rectangle(10, 2)
        self.g2 = Rectangle(2, 10)
        self.g3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_excep(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_A(self):
        """Test id"""
        self.assertEqual(self.g1.id, 10)
        self.assertEqual(self.g2.id, 11)
        self.assertEqual(self.g3.id, 12)
        """ Test width"""
        self.assertEqual(self.g1.width, 10)
        self.assertEqual(self.g2.width, 2)
        self.assertEqual(self.g3.width, 10)
        """ Test height"""
        self.assertEqual(self.g1.height, 2)
        self.assertEqual(self.g2.height, 10)
        self.assertEqual(self.g3.height, 2)
        """ Test x"""
        self.assertEqual(self.g1.x, 0)
        self.assertEqual(self.g2.x, 0)
        self.assertEqual(self.g3.x, 0)
        """ Test y"""
        self.assertEqual(self.g1.y, 0)
        self.assertEqual(self.g2.y, 0)
        self.assertEqual(self.g3.y, 0)
        """ Test area"""
        self.assertEqual(self.g1.area(), 20)
        self.assertEqual(self.g2.area(), 20)
        self.assertEqual(self.g3.area(), 20)

    def test_B_someExecp(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = - 10
            self.g1.width = - 10
            self.g2.width = - 10
            self.g3.width = - 10

        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 2)
            r2.height = - 10
            self.g1.height = - 10
            self.g2.height = - 10
            self.g3.height = - 10

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 2)
            r3.x = - 10
            self.g1.x = - 10
            self.g2.x = - 10
            self.g3.x = - 10


if __name__ == "__main__":
    unittest.main()
