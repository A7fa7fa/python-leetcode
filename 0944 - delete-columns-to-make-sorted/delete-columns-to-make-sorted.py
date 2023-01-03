from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        rowLen = len(strs[0])
        deletedCol = set()

        for rowNumber in range(1, len(strs)):
            for i in range(rowLen):
                if i not in deletedCol and strs[rowNumber][i] < strs[rowNumber - 1][i]:
                    deletedCol.add(i)
        return len(deletedCol)

    # very fast
    def minDeletionSize2(self, strs: List[str]) -> int:
        c = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                c += 1
        return c
