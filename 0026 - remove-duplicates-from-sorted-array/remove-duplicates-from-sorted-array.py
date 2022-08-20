def removeDuplicates(nums: list[int]) -> int:
	
	
	curr = None
	i = 0
	
	while i < len(nums):
		if curr != nums[i]:
			curr = nums[i]
		else:
			nums[i] = None
		i += 1
		
	countNones = 0
	i = 0
	while i < len(nums):
		if nums[i] is None:
			countNones += 1
		else:
			nums[i-countNones], nums[i] = nums[i], nums[i-countNones]
		i += 1
	
	return len(nums) - countNones