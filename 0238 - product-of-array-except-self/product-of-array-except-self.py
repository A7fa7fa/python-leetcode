from collections import defaultdict
from typing import Counter, List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftProduct = [0] * len(nums)
        rightProduct = [0] * len(nums)
        leftProduct[0] = nums[0]
        rightProduct[-1] = nums[-1]

        # move from left to right and multiply it every step
        for i in range(1, len(nums)):
            leftProduct[i] = nums[i] * leftProduct[i - 1]

        # move from right to left and multiply it every step
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = nums[i] * rightProduct[i + 1]

        result = [0] * len(nums)
        result[0] = rightProduct[1]
        result[-1] = leftProduct[-2]

        # result at every index is the product on the leftside[i-1] * rightside[i+1]
        for i in range(1, len(result) - 1):
            result[i] = leftProduct[i-1] * rightProduct[i+1]

        return result


s = Solution()
nums = [-1, 1, 0, -3, 3]

res = s.productExceptSelf(nums=nums)
print(res)
