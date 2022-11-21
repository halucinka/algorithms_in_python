from unittest import TestCase

from algorithms_in_python.binary_search_2.main import binary_search, binary_search_3ifs


class Test(TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)
        self.assertEqual(binary_search([1, 2, 4], 3), -1)

    def test_binary_search_3ifs(self):
        self.assertEqual(binary_search_3ifs([], 3), -1)
        self.assertEqual(binary_search_3ifs([1, 2], 3), -1)
        self.assertEqual(binary_search_3ifs([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_3ifs([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_3ifs([1, 2, 3, 4], 4), 3)
        self.assertEqual(binary_search_3ifs([1, 2, 4], 3), -1)
