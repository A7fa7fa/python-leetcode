def moveZeroes(nums: list[int]) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""

	if len(nums) == 1:
		return
	

	counterZero = 0
	
	for i in range(len(nums)):
		# if num is zero increment counter
		if nums[i] == 0:
			counterZero += 1
		# elso move number to position minus amount of zeros encountered before
		else:
			nums[i - counterZero] = nums[i]
	
	for i in range(len(nums) - counterZero, len(nums)):
		# fill end of nums by amount of counterZero with 0
		nums[i] = 0
		
nums = [0,1,0]
moveZeroes(nums)
print(nums)
		
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

nums = [0]
moveZeroes(nums)
print(nums)

nums = [0, 1]
moveZeroes(nums)
print(nums)

nums = [1, 0]
moveZeroes(nums)
print(nums)
		
nums = [2, 1]
moveZeroes(nums)
print(nums)

nums = [-13009,0,-81471,93346,0,-71602,-18829,-45703,0,0,0,15246,0,51324,89825,0,70362,0,50913,0,47988,-87456,94441,0,0,77733,9338]
moveZeroes(nums)
print(nums)
		
		