class Solution:
    def concatenatedBinary(self, n: int) -> int:
        resBi = ""
        
        for i in range(1, n+1):
            resBi += format(i, "b")
            
        resBi = int(resBi, 2)
        
        return resBi % (10**9 + 7)