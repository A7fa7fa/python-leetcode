from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        # not legal
        if len(mat) * len(mat[0]) != r * c:
            return mat

        asList = []
        for row in mat:
            asList.extend(row)
        print(asList)
        
        result = []

        for rowIdx in range(r):

            newRow = asList[rowIdx*c: (rowIdx*c)+c]
            print(newRow)
            result.append(newRow)
        
        return result



        