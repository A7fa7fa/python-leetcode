from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        actualSum = sum([i for i in nums if i % 2 == 0])
        result = []
        
        for qu in queries:
            if nums[qu[1]] % 2 == 0:
                actualSum -= nums[qu[1]]
                
            nums[qu[1]] += qu[0]            
            if nums[qu[1]] % 2 == 0:
                actualSum += nums[qu[1]]
            
            result.append(actualSum)
                
            
        return result