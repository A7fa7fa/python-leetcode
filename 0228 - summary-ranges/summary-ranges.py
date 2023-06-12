from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = list()

        foundRange = list()
        foundRange.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                foundRange.append(nums[i-1])
                result.append(foundRange[:])
                foundRange = list()
                foundRange.append(nums[i])
            elif i + 1 == len(nums):
                foundRange.append(nums[i])
                result.append(foundRange[:])

        if len(foundRange) == 1:
            result.append([foundRange[0], foundRange[0]])

        print(result)

        return [f"{start}->{end}" if start != end else f"{start}" for start, end in result]
