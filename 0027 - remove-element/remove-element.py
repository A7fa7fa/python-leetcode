from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for idx in range(len(nums)):
            
            if nums[idx] == val:
                nums[idx] == "_"
                count += 1
            else:
                nums[idx - count], nums[idx] = nums[idx], nums[idx - count]
                
        return len(nums) - count
            
        
        