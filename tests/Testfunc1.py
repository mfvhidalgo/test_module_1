# python -m tests.Testfunc1
import unittest

from src.mfvhfunc import func1

class Testfunc1(unittest.TestCase):

    def test_func1(self):
        self.assertEqual(func1(3),4)