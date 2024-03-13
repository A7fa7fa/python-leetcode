class Solution:
    def pivotInteger(self, n: int) -> int:

        totalSum = sum([i for i in range(n+1)])

        currSum = 0

        for i in range(1, n+1):
            currSum += i
            if totalSum == currSum:
                return i
            totalSum -= i
        return -1
