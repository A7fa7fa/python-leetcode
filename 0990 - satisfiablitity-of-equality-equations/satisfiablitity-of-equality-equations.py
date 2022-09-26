import collections
from typing import List


class Solution:

    def dfs(self, first, second, isEqual, visited):
        visited.add(first)
        for nei in isEqual[first]:
            if nei == second:
                return False            
            if nei not in visited:
                ans = self.dfs(nei, second, isEqual, visited)
                if ans == False:
                    return False
        return True

    def equationsPossible(self, equations: List[str]) -> bool:

        isEqual = collections.defaultdict(set)


        for equ in equations:          

            if equ[1] == "=":
                first = equ[0]
                second = equ[3]
                isEqual[first].add(second)
                isEqual[second].add(first)

        for equ in equations:

            if equ[1] == "!":

                first = equ[0]
                second = equ[3]
                if first == second:
                    return False

                if isEqual[first] and isEqual[second]:

                    ans = self.dfs(first, second, isEqual, set())

                    if ans == False:
                        return False

        return True