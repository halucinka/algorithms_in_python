from unittest import TestCase

from algorithms_in_python.leetcode.maximum_product_subarray.main import Solution


class TestSolution(TestCase):
    def test_max_product(self):
        self.assertEqual(Solution().maxProduct([2, 3, -2, 4]), 6)
