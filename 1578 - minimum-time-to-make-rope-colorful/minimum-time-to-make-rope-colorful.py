from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        ptr = 0
        timeLeft = 0
        
        while ptr < len(colors):
            i = 1
            while ptr + i < len(colors)  and colors[ptr] == colors[ptr + i]:
                i += 1
            
            timeLeft += max(neededTime[ptr:ptr+i])
            ptr = ptr + i
        
        return sum(neededTime) - timeLeft
        