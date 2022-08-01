def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
	
	numCounts = {}    
	result = []
	
	if len(nums1) > len(nums2):
		nums1, nums2 = nums2, nums1
	
	for num in nums1:
		if str(num) in numCounts:
			numCounts[str(num)] += 1
		else:
			numCounts[str(num)] = 1                

			
	for num in nums2:
		if str(num) in numCounts:
			numCounts[str(num)] -= 1
			result.append(num)
			
			if numCounts[str(num)] == 0:
				del numCounts[str(num)]
				
		if not numCounts:
			break
	
	return result


intersect([1,2,2,1], [2,2])