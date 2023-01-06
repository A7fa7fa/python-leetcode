from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        
        icecreams = 0
        
        for cost in costs:
            
            if cost <= coins:
                icecreams += 1
                coins -= cost
                
            else:
                break
        return icecreams
        
        