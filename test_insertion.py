import unittest
from insertion import *
import random


class InsertionTestCase(unittest.TestCase):
    '''Tests for insertion.py'''

    def make_list(self):
        random_list = []
        for i in range(50):
            random_list.append(random.randrange(100))
        return random_list

    def test_sort(self):
        for i in range(50):
            l = self.make_list()
            self.assertTrue(insertion_sort(l) == sorted(l))

    def test_small(self):
        self.assertTrue(insertion_sort([]) == [])
        self.assertTrue(insertion_sort([1]) == [1])
