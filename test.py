import unittest
from lab9 import max_wire_length

class TestMaxWireLength(unittest.TestCase):
    def test_case1(self):
        self.assertAlmostEqual(max_wire_length(2, [3, 3, 3]), 5.66, places=2)

    def test_case2(self):
        self.assertAlmostEqual(max_wire_length(100, [1, 1, 1, 1]), 300.00, places=2)

    def test_case3(self):
        self.assertAlmostEqual(max_wire_length(4, [100, 2, 100, 2, 100]), 396.32, places=2)

    def test_case4(self):
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91,
                   25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52,
                   87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        self.assertAlmostEqual(max_wire_length(4, heights), 2738.18, places=2)

if __name__ == '__main__':
    unittest.main()
