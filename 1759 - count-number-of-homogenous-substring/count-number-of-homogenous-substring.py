class Solution:
    def countHomogenous(self, s: str) -> int:
        
        
        currentSequeValue = 0
        currentLength = 0
        total = 0
        prevChar = None

        for char in s:
            if char == prevChar:
                currentLength += 1
                currentSequeValue += currentLength
            else:
                total += currentSequeValue
                currentSequeValue = 1
                currentLength = 1
                prevChar = char

        total += currentSequeValue

        return total % (10**9+7)
        