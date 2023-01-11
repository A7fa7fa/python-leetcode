from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        def dfs(graph: dict, visited: set, path: list, step: int) -> bool:

            # self has apple
            childs = hasApple[step]
            # add to visited so not visted as nei again
            visited.add(step)

            for nei in graph[step]:
                if nei != step and nei not in visited:
                    # extend path by nei
                    # if nei or nei of nei has at least one apple path is valid
                    # and so childs are set to true to mark visit as valid
                    # append step again because backtrack is an additional step
                    # else removed last step and visit next nei
                    path.append(nei)
                    res = dfs(graph, visited, path, nei)
                    if res:
                        childs = True
                        path.append(step)
                    else:
                        path.pop()
            # return true if self or at least one nei has apple
            # else false
            return childs

        # construct graph
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        path = list()
        dfs(graph, set(), path, 0)
        return len(path)


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]

s = Solution()
res = s.minTime(n, edges, hasApple)
print(res)
