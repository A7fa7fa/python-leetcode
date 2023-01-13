from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validColl = [[False for _ in range(9)] for _ in range(9)]
        validRows = [[False for _ in range(9)] for _ in range(9)]

        for rowIdx in range(9):
            for collIdx in range(9):
                if board[rowIdx][collIdx] != ".":
                    if validRows[rowIdx][int(board[rowIdx][collIdx])-1]:
                        return False
                    validRows[rowIdx][int(board[rowIdx][collIdx])-1] = True
                    if validColl[collIdx][int(board[rowIdx][collIdx])-1]:
                        return False
                    validColl[collIdx][int(board[rowIdx][collIdx])-1] = True

                if rowIdx % 3 == 0 and collIdx % 3 == 0:
                    validBlock = [False for _ in range(9)]
                    block = []
                    for i in range(3):
                        block.extend(board[rowIdx+i][collIdx:collIdx+3])
                    for num in block:
                        if num != ".":
                            if validBlock[int(num) - 1]:
                                return False
                            validBlock[int(num)-1] = True

        return True
