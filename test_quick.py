import unittest
from quicksort import *
import random


class MergeTestCase(unittest.TestCase):
    '''Tests for quicksort.py'''

    def make_list(self):
        random_list = []
        for i in range(50):
            random_list.append(random.randrange(100))
        return random_list

    def test_sort(self):
        for i in range(50):
            l = self.make_list()
            l2 = l[:]
            self.assertTrue(quicksort(l) == sorted(l2))
        for i in range(50):
            l = self.make_list()
            l2 = l[:]
            quicksort_inplace(l)
            self.assertTrue(l == sorted(l2))

    def test_empty(self):
        self.assertTrue(quicksort([]) == [])
        self.assertTrue(quicksort([1]) == [1])
        self.assertTrue(quicksort_inplace([]) == [])
        self.assertTrue(quicksort_inplace([1]) == [1])
