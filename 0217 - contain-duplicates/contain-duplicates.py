def containsDuplicate(self, nums: list[int]) -> bool:
    
    visited = set()
    
    for num in nums:
        if num in visited:
            return True
        visited.add(num)
    return False
    
# alternative:
# return len(nums) > len(set(nums))