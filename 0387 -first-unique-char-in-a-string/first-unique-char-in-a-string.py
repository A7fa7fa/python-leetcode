class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        found = Counter(s)
        
        for idx, char in enumerate(s):
            if found[char] == 1:
                return idx
            
        return -1