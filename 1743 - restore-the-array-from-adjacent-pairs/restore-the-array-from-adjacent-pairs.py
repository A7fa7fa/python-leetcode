import collections
from typing import List


class Solution:


    def traverse(self, adj, nums, num) -> None:
        prev = None
        if nums:
            prev = nums[-1]
        nums.append(num)

        nextNum = adj.get(num).pop()
        if nextNum == prev:
            if len(adj[num]) == 0:
                return
            nextNum = adj.get(num, None).pop()
        del adj[num]

                
        self.traverse(adj, nums, nextNum)


    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adj = collections.defaultdict(list)


        for pair in adjacentPairs:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
        
        nums = []
        start = None

        for key in adj:
            if len(adj[key]) == 1:
                start = key
                break

        self.traverse(adj, nums, start)
        return nums

    def restoreArray2(self, adjacentPairs: List[List[int]]) -> List[int]:
        dict = collections.defaultdict(list)
        for x,y in adjacentPairs:
            dict[x].append(y)
            dict[y].append(x)
        
        start = 0
        for x in dict.keys():
            if len(dict[x]) == 1:
                start = x
                break
        
        seen = set()
        ans = []
        while start != None:
            ans.append(start)
            seen.add(start)
            adj = dict[start]

            for x in adj:
                if x not in seen:
                    start = x
                    break
                start = None
        return ans