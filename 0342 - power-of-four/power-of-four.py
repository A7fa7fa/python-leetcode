class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        if n == 1:
            return True
        
        if n % 4 != 0:
            return False
        
        init = 1
        while init < n:
            init *= 4
            
            if init == n:
                return True
        
        return False
        
        