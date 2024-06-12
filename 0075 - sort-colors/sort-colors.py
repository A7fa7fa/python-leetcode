class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        color_count = [0, 0, 0]

        for num in nums:
            color_count[num] += 1

        nums[:color_count[0]] = [0] * color_count[0]
        nums[color_count[0]:color_count[0]+color_count[1]] = [1] * color_count[1]
        nums[color_count[0]+color_count[1]:] = [2] * color_count[2]


