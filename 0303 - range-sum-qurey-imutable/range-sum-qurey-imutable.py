from typing import List


class NumArray:

    def __init__(self, nums: List[int]) -> None:
        self.sum = [0]
        for i in range(len(nums)):
            self.sum.append(nums[i]+self.sum[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right+1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
