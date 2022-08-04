def twoSum(self, numbers: list[int], target: int) -> list[int]:
	
	leftIndex = 0
	rightIndex = len(numbers) - 1
	
	while leftIndex < rightIndex:
		if numbers[leftIndex] + numbers[rightIndex] == target:
			# returning just index returns fails testcases
			# asked are the number of elements in array not index
			return [leftIndex + 1, rightIndex + 1]
		
		if numbers[leftIndex] + numbers[rightIndex] > target:
				rightIndex -= 1
		else:
			leftIndex += 1
		

	