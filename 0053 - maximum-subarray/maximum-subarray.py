def maxSubArray(nums: list[int]) -> int:
	# is it better to add the next value of nums to current value or start over from scretch
	# if current value is higher than max. max value = current value

	maxSum = nums[0]
	currentSum = nums[0]

	for i in range(1, len(nums)):

		if nums[i] > currentSum + nums[i]:
			currentSum = nums[i]

		else:
			currentSum += nums[i]
		
		maxSum = max(currentSum, maxSum)

	return maxSum



res = maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
print(res) #6

res1 = maxSubArray(nums=[1])
print(res1) #1

res2 = maxSubArray(nums=[5,4,-1,7,8])
print(res2) #23

res3 = maxSubArray(nums=[1,2,-1,-2,2,1,-2,1,4,-5,4])
print(res3)

res4 = maxSubArray(nums=[-2,-3,-1])
print(res4)
