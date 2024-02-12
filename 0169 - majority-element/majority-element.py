from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)

        for key, value in count.items():
            if value > (len(nums) / 2):
                return key

        # nums.sort()
        # return nums[len(nums)//2]


