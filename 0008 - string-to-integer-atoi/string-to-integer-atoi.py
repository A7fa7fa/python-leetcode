class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        firstDigit = False
        res = ""
        
        for char in s:
            if char.isdigit():
                firstDigit = True
            
            if firstDigit == False:
                if char == " ":
                    continue  
                elif char == "-" or char == "+":
                    res += char
                    firstDigit = True
                else:
                    return 0
            else:
                if char.isdigit():
                    res += char
                else:
                    break
                    
        if len(s) == 0:
            return 0
        if res == "+" or res == "-" or res == "":
            return 0
        
        res = max(int(res), -2**31)
        res = min(int(res), 2**31-1)

        return res
            
            
                