def searchInsert( nums: list[int], target: int) -> int:
    
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        middle = (start + end) // 2
        print(start, middle, end)
        
        if nums[middle] == target:
            return middle 
        
        elif nums[middle] > target:
            # move left
            end = middle - 1
        
        elif nums[middle] < target:
            # move right
            start = middle + 1
    
    return start

res= searchInsert(nums=[1,3,5,6], target=7)
print(res)

