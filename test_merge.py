import unittest
from mergesort import *
import random


class MergeTestCase(unittest.TestCase):
    '''Tests for mergesort.py'''

    def make_list(self):
        random_list = []
        for i in range(50):
            random_list.append(random.randrange(100))
        return random_list

    def test_sort(self):
        for i in range(50):
            l = self.make_list()
            l2 = l[:]
            self.assertTrue(mergesort(l) == sorted(l2))
        for i in range(50):
            l = self.make_list()
            l2 = l[:]
            self.assertTrue(mergesort_inplace(l) == sorted(l2))

    def test_empty(self):
        self.assertTrue(mergesort([]) == [])
        self.assertTrue(mergesort([1]) == [1])
        self.assertTrue(mergesort_inplace([]) == [])
        self.assertTrue(mergesort_inplace([1]) == [1])
