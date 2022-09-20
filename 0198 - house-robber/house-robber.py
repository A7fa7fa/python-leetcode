from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [0 for _ in range(len(nums) + 3)]
                
        
        for i in range(len(nums) - 1, -1, -1):                
            memo[i] = max(memo[i + 2], memo[i + 3]) + nums[i]   
                
        return max(memo)