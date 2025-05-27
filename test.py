import unittest
from lab7 import boyer_moore_search

class TestBoyerMooreReverseSearch(unittest.TestCase):

    def test_single_match(self):
        self.assertEqual(boyer_moore_search("ABCD", "BC"), [1])

    def test_multiple_matches(self):
        self.assertEqual(boyer_moore_search("ABCABCABC", "ABC"), [0, 3, 6])

    def test_no_match(self):
        self.assertEqual(boyer_moore_search("ABCDEFG", "XYZ"), [])

    def test_full_match(self):
        self.assertEqual(boyer_moore_search("HELLO", "HELLO"), [0])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("HELLO", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "HELLO"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(boyer_moore_search("HI", "HELLO"), [])

    def test_overlapping_matches(self):
        self.assertEqual(boyer_moore_search("AAAAA", "AAA"), [0, 1, 2])

if __name__ == "__main__":
    unittest.main()
