class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        checkSum = 1
        while checkSum <= n:
            if checkSum == n:
                return True
            checkSum = checkSum << 1
        return False