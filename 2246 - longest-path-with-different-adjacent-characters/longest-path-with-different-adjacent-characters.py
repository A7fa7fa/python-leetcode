from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        # build tree
        tree = [[] for _ in range(len(parent))]
        for idx, par in enumerate(parent):
            if par != -1:
                tree[par].append(idx)

        def dfs(node: int, maxP: List[str]) -> str:

            childPaths = []
            for child in tree[node]:
                # find path for every subnode
                path = dfs(child, maxP)
                # if path + lable self is different path is valid childpath
                if path[-1] != str(s[node]):
                    childPaths.append(path)

            # if there is no valid childpath just return self lable
            if len(childPaths) == 0:
                return str(s[node])

            # else sort childpath by length to get the two longest pathes
            childPaths.sort(key=len, reverse=True)
            # set longest path
            maxP[0] = max([childPaths[0] + str(s[node]), maxP[0]], key=len)

            # if there are at least two childs
            # combine them and set as global max if longer
            if len(childPaths) > 1:
                tempPath = childPaths[0] + str(s[node]) + childPaths[1][::-1]
                maxP[0] = max([tempPath, maxP[0]], key=len)
            # return longest path + self lable
            return childPaths[0] + str(s[node])

        maxPath = [""]
        return max(len(dfs(0, maxPath)), len(maxPath[0]))
