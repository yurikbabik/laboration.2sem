import unittest
import os
from lab8 import minimum_fiber_length

class TestMinimumFiberLength(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_data.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def write_test_file(self, rows):
        with open(self.test_file, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(",".join(map(str, row)) + "\n")

    def test_connected_graph(self):
        data = [
            ["K1", "K2", 100],
            ["K2", "K3", 200],
            ["K1", "K3", 300]
        ]
        self.write_test_file(data)
        self.assertEqual(minimum_fiber_length(self.test_file), 300)

    def test_disconnected_graph(self):
        data = [
            ["K1", "K2", 100],
            ["K3", "K4", 200]
        ]
        self.write_test_file(data)
        self.assertEqual(minimum_fiber_length(self.test_file), -1)

    def test_single_connection(self):
        data = [
            ["K1", "K2", 100]
        ]
        self.write_test_file(data)
        self.assertEqual(minimum_fiber_length(self.test_file), 100)

if __name__ == "__main__":
    unittest.main()
