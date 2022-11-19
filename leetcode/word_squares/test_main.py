from unittest import TestCase

from algorithms_in_python.leetcode.word_squares.main import Solution


class TestSolution(TestCase):
    def test_word_squares(self):
        actual = Solution().wordSquares(["area","lead","wall","lady","ball"])
        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0] ==["wall","area","lead","lady"] and actual[1] ==["ball","area","lead","lady"] or
                         actual[1] ==["wall","area","lead","lady"] and actual[0] ==["ball","area","lead","lady"], True)

