class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        for i in range(0, len(s)):
            start1, end1 = self.findLongestPalindromWithCenter(s, i, i)
            start2, end2 = self.findLongestPalindromWithCenter(s, i, i + 1)
            if end1 - start1 + 1 > end - start + 1:
                start, end = start1, end1
            if end2 - start2 + 1 > end - start + 1:
                start, end = start2, end2
        return s[start: end + 1]

    def findLongestPalindromWithCenter(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end - 1