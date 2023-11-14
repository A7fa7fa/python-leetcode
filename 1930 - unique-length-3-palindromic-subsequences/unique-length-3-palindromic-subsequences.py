
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        OFFSET = 97
        DEFAULT_FIRST = len(s)+1
        DEFAULT_LAST = -1
        memo = [[DEFAULT_FIRST, DEFAULT_LAST] for _ in range(26)] # min, max, count

        result = 0

        for i, char in enumerate(s):
            pos = ord(char) - OFFSET
            memo[pos][0] = min(i, memo[pos][0])
            memo[pos][1] = max(i, memo[pos][1])

        for [first, last] in memo:
            if first == DEFAULT_FIRST:
                continue
            if last - first < 2:
                continue
            
            
            # get chars inbetween
            # optimze potential to check only every char (26) instead whole substring 
            unique = set(s[first+1:last])
            result += len(unique)

        return result