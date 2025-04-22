import unittest
from lab6 import max_experience

class TestCareer(unittest.TestCase):
    def test_example_1(self):
        L = 4
        pyramid = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(max_experience(L, pyramid), 12)

    def test_example_2(self):
        L = 1
        pyramid = [
            [9999]
        ]
        self.assertEqual(max_experience(L, pyramid), 9999)

    def test_example_3(self):
        L = 5
        pyramid = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        self.assertEqual(max_experience(L, pyramid), 3)

    def test_all_zero(self):
        L = 3
        pyramid = [
            [0],
            [0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(max_experience(L, pyramid), 0)

    def test_max_path_on_edge(self):
        L = 3
        pyramid = [
            [1],
            [2, 1],
            [3, 1, 1]
        ]
        self.assertEqual(max_experience(L, pyramid), 6)

if __name__ == '__main__':
    unittest.main()
