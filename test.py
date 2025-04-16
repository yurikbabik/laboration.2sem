import unittest
from lab5 import has_cycle

class TestCycleDetection(unittest.TestCase):
    def test_with_cycle(self):
        graph = {
            1: [2, 3],
            2: [1, 5, 6],
            3: [1],
            4: [1, 7, 8],
            5: [2, 9, 10],
            6: [2, 10],
            7: [4, 11],
            8: [4, 12],
            9: [5],
            10: [5, 6],
            11: [7],
            12: [8]
        }
        self.assertTrue(has_cycle(graph))

    def test_without_cycle(self):
        graph = {
            1: [2],
            2: [1, 3],
            3: [2]
        }
        self.assertFalse(has_cycle(graph))

    def test_empty_graph(self):
        self.assertFalse(has_cycle({}))

    def test_single_node(self):
        self.assertFalse(has_cycle({1: []}))

if __name__ == "__main__":
    unittest.main()
