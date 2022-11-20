from unittest import TestCase

from algorithms_in_python.leetcode.longest_palindromic_substring.main import Solution


class TestSolution(TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(Solution().longestPalindrome("babad"), "bab")
