class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        openBr = {"(", "[", "{" }
                             
        closeBr = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        for char in s:
            if not stack:
                stack.append(char)
            elif char in openBr:
                    stack.append(char)
            else:
                if closeBr.get(stack[-1], "-") != char:
                    return False
                stack.pop()

        if stack:
            return False

        return True