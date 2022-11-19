from typing import List


class Solution:
    def __init__(self):
        self.n = 3
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.n = len(words[0])
        self.words = words
        results = []
        result = []
        self.buildPrefixDictionary(words)

        for word in words:
            square = [word]
            self.backtrack(1, square, results)
        return results

    def backtrack(self, step, square, results):
        if step == self.n:
            results.append(square[:])
            return

        prefix = ''.join(word[step] for word in square)

        if prefix in self.prefixDict:
            for word in self.prefixDict[prefix]:
                square.append(word)
                self.backtrack(step + 1, square, results)
                square.pop()

    def buildPrefixDictionary(self, words):
        self.prefixDict = {}
        for word in words:
            for i in range(1, self.n):
                self.prefixDict.setdefault(word[:i], set()).add(word)
