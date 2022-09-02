class Solution:
            
    def uniquePaths(self, m: int, n: int) -> int:
        
        mat = [[0 for _ in range(n)] for _ in range(m)]
        mat[0][0] = 1
        
        for i in range(m):
            for j in range(n):                
                if i > 0:
                    mat[i][j] += mat[i-1][j]        
                if j > 0:
                    mat[i][j] += mat[i][j-1]
        

        return mat[m-1][n-1]             
