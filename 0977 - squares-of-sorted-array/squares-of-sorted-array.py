def sortedSquares(nums: list[int]) -> list[int]:
	resultNeg = []
	result = []
	
	pointer = 0
	while pointer < len(nums):
		squ = nums[pointer] * nums[pointer]
		if nums[pointer] < 0:
			resultNeg.append(squ)
			pointer += 1
		else:
			if len(resultNeg) > 0 and resultNeg[-1] < squ:
				result.append(resultNeg.pop())
			else:
				result.append(squ)
				pointer += 1
		
	if len(resultNeg) > 0:
		for i in range(len(resultNeg)):
			result.append(resultNeg.pop())
		
	return result