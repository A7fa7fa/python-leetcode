class Solution:
    def minSetSize(self, arr: List[int]) -> int:
               
        foundNums = Counter(arr)
        target = len(arr) // 2
        
        nums = sorted(list(foundNums.values()))
        
        result = 0
        removedElements = 0
        while removedElements < target:
            removedElements += nums.pop()
            result += 1
        
        return result