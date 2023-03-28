from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        for rowNum in range(len(grid)):
            for collNum in range(len(grid[0])):
                if rowNum == 0 and collNum == 0:
                    grid[rowNum][collNum] = grid[rowNum][collNum]
                elif rowNum == 0:
                    grid[rowNum][collNum] += grid[rowNum][collNum - 1]
                elif collNum == 0:
                    grid[rowNum][collNum] += grid[rowNum - 1][collNum]
                else:
                    grid[rowNum][collNum] += min(grid[rowNum - 1]
                                                 [collNum], grid[rowNum][collNum - 1])

        return grid[-1][-1]
