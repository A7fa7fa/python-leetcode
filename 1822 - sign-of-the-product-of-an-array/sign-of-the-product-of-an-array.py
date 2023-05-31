from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:

        negative = 0

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negative += 1

        if negative % 2 == 0:
            return 1
        return -1
