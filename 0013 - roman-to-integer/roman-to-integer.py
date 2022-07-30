class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "max": 99999,
        }        
        
        result = 0
        prevChar = "max"
        prevSum = 0
        
        for char in s:
            if trans[prevChar] > trans[char]:
                if prevSum > 0 :
                    result += prevSum
                    prevSum = 0
                prevSum += trans[char]
                prevChar = char
                continue

            if trans[prevChar] == trans[char]:
                prevSum += trans[char]            
                continue
            
            if trans[prevChar] < trans[char]:
                result += trans[char] - prevSum
                prevChar = char
                prevSum = 0

        
        result += prevSum                   
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))