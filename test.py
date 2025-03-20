import unittest
from lab2_sem2 import painting_time

class TestPaintingAlgorithm(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(painting_time(10, 5, [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]), 100)

    def test_single_painter(self):
        self.assertEqual(painting_time(1, 3, [5, 10, 15]), 90)

    def test_multiple_painters(self):
        self.assertEqual(painting_time(3, 2, [5, 10, 15]), 30)

    def test_empty_list(self):
        self.assertEqual(painting_time(2, 5, []), 0)

    def test_more_painters_than_shields(self):
        self.assertEqual(painting_time(5, 4, [5, 10]), 40)

if __name__ == "__main__":
    unittest.main()
