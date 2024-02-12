class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)

        result = []
        for key, value in count.items():
            if value > (len(nums) / 3):
                result.append(key)
        return result