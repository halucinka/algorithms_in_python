from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        positive = nums[0]
        negative = nums[0]
        result = nums[0]
        for i in range(1, n):
            c = nums[i]
            temp_positive = max(c, positive * c, negative * c)
            negative = min(c, positive * c, negative * c)
            positive = temp_positive
            result = max(positive, result)
        return result