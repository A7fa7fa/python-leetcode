class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 1:
            return True
        elif n % 3 > 0 or n < 0:
            return False
        
        while n >= 3:
            
            if n == 3:
                return True
            elif n % 3 > 0:
                return False
            else:
                n /= 3
            
        return False