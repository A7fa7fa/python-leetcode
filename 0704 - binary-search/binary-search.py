def search(nums: list[int], target: int) -> int:
    
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        middle = (end + start) // 2
        print(start, middle, end)

        if nums[middle] == target:
            return middle
        
        # if target is smaller ignore right half and ignore middle
        if target < nums[middle]:
            end = middle - 1
        # if target is bigger ignore left half but inclue middle
        else:
            start = middle + 1
    
    return -1


res = search(nums=[-1,0,3,5,9,12, 13,18, 20, 22 ,25,26], target=26)
print(res)