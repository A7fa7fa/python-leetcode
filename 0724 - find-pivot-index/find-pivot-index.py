def pivotIndex( nums: list[int]) -> int:
	
	leftSum = 0
	rightSum = sum(nums)

	for idx, num in enumerate(nums):
		leftSum += num
		if leftSum == rightSum:
			return idx
		rightSum -= num
	
	return -1

print(pivotIndex([1,7,3,6,5,6])) #3
print(pivotIndex([-1,-1,-1,-1,-1,0])) #2
print(pivotIndex([-1,-1,-1,-1,0,1])) #1
print(pivotIndex([1,2,3])) #-1
print(pivotIndex([2,1,-1])) #0
print(pivotIndex([-1,-1,-1,1,1,1])) #-1

