from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if max(nums) < 0:
            return max(nums)

        maxSum = nums[0]
        maxSlidingSum = nums[0]
        minSum = nums[0]
        minSlidingSum = nums[0]

        for idx in range(1, len(nums)):
            num = nums[idx]
            if maxSlidingSum + num >= num:
                maxSlidingSum += num
            else:
                maxSlidingSum = num
            maxSum = max(maxSum, maxSlidingSum)

            if minSlidingSum + num < num:
                minSlidingSum += num
            else:
                minSlidingSum = num
            minSum = min(minSum, minSlidingSum)

        return max(maxSum, sum(nums)-minSum)
