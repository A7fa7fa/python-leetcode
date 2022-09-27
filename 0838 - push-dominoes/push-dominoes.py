class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        memo = [[len(dominoes) + 1, len(dominoes) + 1] for _ in dominoes]
        
        lastR = len(dominoes) + 1
        i = 0
        while i < len(dominoes):
            if dominoes[i] == "R":
                memo[i][0] = 0
                lastR = 0
            elif dominoes[i] == "L":
                lastR = len(dominoes) + 1
            else:
                lastR += 1
                memo[i][0] = min(lastR, len(dominoes) + 1)
                
            i += 1
            
        lastL = len(dominoes) + 1
        for j in range(len(dominoes) - 1, -1, -1):
            if dominoes[j] == "L":
                memo[j][1] = 0
                lastL = 0            
            elif dominoes[j] == "R":
                lastL = len(dominoes) + 1
            else:
                lastL += 1
                memo[j][1] = min(lastL, len(dominoes) + 1)
                
        
        i = 0
        result = ""
        while i < len(dominoes):
            if memo[i][0] == len(dominoes) + 1 and memo[i][1] == len(dominoes) + 1:
                result += "."
            elif memo[i][0] == memo[i][1]:
                result += "."
            elif memo[i][0] < memo[i][1]:
                result += "R"
            else:
                result += "L"
            i += 1
        return result


# Faster. why? string reasignmnet and n*(n+m)
class Solution(object):
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return  dominoes.replace('xxx', 'R.L')              # <-- 3)