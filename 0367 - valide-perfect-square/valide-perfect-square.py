def isPerfectSquare(num: int) -> bool:
	start = 0
	end = num
	
	while start <= end:
		
		middle = (start + end) // 2
		
		sqr = middle * middle
		
		if sqr == num:
			return True
		
		if sqr > num:
			end = middle - 1
		else:
			start = middle + 1
		
	return False

