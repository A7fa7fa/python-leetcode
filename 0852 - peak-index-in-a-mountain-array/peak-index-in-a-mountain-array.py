def peakIndexInMountainArray(arr: list[int]) -> int:
	
	start = 0
	end = len(arr) - 1
	
	while start <= end:
		
		middle = (start + end) // 2
		
		# peak
		if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
			return middle
		
		# left side of mountain so move right
		if arr[middle - 1] < arr[middle + 1]:
			start = middle
		# right side of mountain so move left
		else:
			end = middle
			
	return -1
			
        


res = peakIndexInMountainArray([0,1,0])
print(res)
res = peakIndexInMountainArray([0,2,1,0])
print(res)
res = peakIndexInMountainArray([0,10,5,2])
print(res)

