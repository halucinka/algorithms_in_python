import unittest

from main import binary_search, find_index, binary_search_optimized


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)
        self.assertEqual(binary_search([1, 2, 4], 3), -1)

    def test_binary_search_optimized(self):
        self.assertEqual(binary_search_optimized([], 3), -1)
        self.assertEqual(binary_search_optimized([1, 2], 3), -1)
        self.assertEqual(binary_search_optimized([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_optimized([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_optimized([1, 2, 3, 4], 4), 3)
        self.assertEqual(binary_search_optimized([1, 2, 4], 3), -1)


    def test_find_index(self):
        self.assertEqual(find_index([], 3), 0)
        self.assertEqual(find_index([1, 2], 3), 2)
        self.assertEqual(find_index([1, 2, 3, 4], 3), 2)
        self.assertEqual(find_index([1, 2, 3, 4], 1), 0)
        self.assertEqual(find_index([1, 2, 3, 4], 4), 3)
        self.assertEqual(find_index([1, 2, 4], 3), 2)

if __name__ == '__main__':
    unittest.main()