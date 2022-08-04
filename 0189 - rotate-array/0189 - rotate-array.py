def rotate(nums: list[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	
	if len(nums) == k or k == 0 or len(nums) == 1:
		return
	
	n = k
	if len(nums) < k:
		n =  k % len(nums)
	
	
	first = nums[: - n]
	second = nums[len(nums) - n:]
	print(first, second)
	for idx in range(len(nums)):
		if idx < len(second):
			nums[idx] = second[idx]
		else:
			nums[idx] = first[idx - len(second)]
		

def rotate(nums: list[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""

	d = len(nums)
	k = k % d
	if k < d / 2:
		for _ in range(k):
			nums.insert(0,nums.pop(-1))
	else:
		k = d - k
		for _ in range(k):
			nums.append(nums.pop(0))
