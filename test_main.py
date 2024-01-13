#!/usr/bin/python3
import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertRaises(TypeError, add, 5.6, 5)
