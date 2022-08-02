def runningSum(nums: list[int]) -> list[int]:
	result = []
	for num in nums:
		if result:
			result.append(sum((num, result[-1])))
		else:
			result.append(num)
	
	return result

		

res = runningSum(nums=[1,2,3,4])
print(res)