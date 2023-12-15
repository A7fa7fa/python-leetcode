
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        connections = dict()

        for fromDest, toDest in paths:
            connections[fromDest] = toDest

        start = paths[0][0]
        end = connections.get(start, None)

        while start != None:
            end = start
            start = connections.get(end, None)

        return end

    def destCity2(self, paths: List[List[str]]) -> str: #slower
        [starts, ends] = list(map(set, list(zip(*paths))))

        notBoth = starts ^ ends

        for stop in notBoth:
            if stop in ends:
                return stop



s = Solution()
paths = [["B","C"],["D","B"],["C","A"]]
res = s.destCity2(paths)
print(res)