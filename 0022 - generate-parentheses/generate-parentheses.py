from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        pt = [n, n]  # open, close
        result = []
        cur = []

        def dfs(paren, current):
            if paren[0] == 0 and paren[1] == 0:
                result.append("".join(current))
                return
            # open
            if paren[0] > 0:
                current.append("(")
                paren[0] = paren[0] - 1
                dfs(paren, current)
                current.pop()
                paren[0] = paren[0] + 1
            # close
            if paren[0] < paren[1]:
                current.append(")")
                paren[1] = paren[1] - 1
                dfs(paren, current)
                current.pop()
                paren[1] = paren[1] + 1

        dfs(pt, cur)
        return result
