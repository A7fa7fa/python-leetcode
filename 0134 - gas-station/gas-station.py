from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tank = 0
        i = 0
        startedIdx = -1
        possible = True
        circledOnce = False

        while i < len(gas):
            if startedIdx == i:
                return startedIdx
            
            if gas[i] + tank >= cost[i]:
                if startedIdx == -1:
                    startedIdx = i
                tank += gas[i]
                tank -= cost[i]
                i += 1
                possible = True
                if not circledOnce and i == len(gas):
                    i = 0
                    circledOnce = True
            else:
                tank = 0
                possible = False
                startedIdx = -1
                i += 1
                if circledOnce:
                    return startedIdx       
            

        
        return startedIdx
            


            
            
s = Solution()
gas =  [1,2,3,4,5]
cost = [3,4,5,1,2]
res = s.canCompleteCircuit(gas=gas, cost=cost)
print(res)

        
gas =  [2,3,4]
cost = [3,4,3]
res = s.canCompleteCircuit(gas=gas, cost=cost)
print(res)