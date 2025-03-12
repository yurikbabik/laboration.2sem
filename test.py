import unittest
from lab1_sem2 import monotonic

class TestMonotonic(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(monotonic([1,2,3,4,5]))
    def test_deceasing(self):
        self.assertTrue(monotonic([5,4,3,2,1,]))
    def test_non_monotonic (self):
        self.assertFalse(monotonic([1,2,2,3,2,4,]))
    def test_constant (self):
        self.assertTrue(monotonic([2,2,2,2]))
    def test_repeats (self):
        self.assertTrue(monotonic([1,2,2,2,3,4]))
if __name__ == "__main__":
    unittest.main()