import unittest
from lab4 import Priority

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = Priority()
        self.pq.insert(1, 3)
        self.pq.insert(2, 5)
        self.pq.insert(3, 1)
        self.pq.insert(4, 4)

    def test_peek_max(self):
        self.assertEqual(self.pq.peek_max(), 2)

    def test_extract_max(self):
        max_value = self.pq.remove_max()
        self.assertEqual(max_value, 2)
        self.assertEqual(self.pq.peek_max(), 4)

    def test_insert_and_remove_all(self):
        rem = [self.pq.remove_max() for value in range(4)]
        self.assertListEqual(rem, [2, 4, 1, 3])
        self.assertIsNone(self.pq.peek_max())

if __name__ == '__main__':
    unittest.main()
