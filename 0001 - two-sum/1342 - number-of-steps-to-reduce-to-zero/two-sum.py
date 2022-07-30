def twoSum(nums: list[int], target: int) -> list[int]:
	visitedNum = {}
	
	for idx, num in enumerate(nums):
		if target - num in visitedNum:
			return [idx, visitedNum[target - num]]
		else:
			visitedNum[num] = idx
        
			

res = twoSum(nums=[2,-7,11,15], target=4)
print(res)