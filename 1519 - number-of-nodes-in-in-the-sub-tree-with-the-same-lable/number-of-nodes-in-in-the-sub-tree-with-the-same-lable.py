from collections import defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        result = [1] * n
        tree = defaultdict(list)
        visited = set()
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def dfs(nodeIdx):
            numberOfLables = defaultdict(int)
            numberOfLables[labels[nodeIdx]] = 1
            visited.add(nodeIdx)

            for child in tree[nodeIdx]:
                if child != nodeIdx and child not in visited:
                    sub = dfs(child)
                    for key, value in sub.items():
                        numberOfLables[key] += value

            result[nodeIdx] = numberOfLables[labels[nodeIdx]]
            return numberOfLables

        dfs(0)

        return result
