from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalNums = sum(nums)
        if min(nums) == 1:
            return 0
        totalActual = sum([i for i in range(len(nums)+1)])
        if totalNums == totalActual:
            return len(nums)
        return totalActual - totalNums
