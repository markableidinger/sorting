import unittest
from radix import *
import random


class RadixTestCase(unittest.TestCase):
    '''Tests for radix.py'''

    def make_list(self):
        random_list = []
        for i in range(50):
            random_list.append(random.randrange(1000000000000))
        return random_list

    def test_sort(self):
        for i in range(50):
            l = self.make_list()
            l2 = l[:]
            self.assertTrue(radix_sort(l) == sorted(l2))

    def test_small(self):
        self.assertTrue(radix_sort([]) == [])
        self.assertTrue(radix_sort([1]) == [1])
