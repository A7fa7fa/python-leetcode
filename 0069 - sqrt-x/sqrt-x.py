from math import sqrt

def mySqrt(x: int) -> int:
	
	
	start = 0
	end = x
	
	while start <= end:
		
		middle = (start + end) // 2
		
		sqr = middle * middle
		
		if sqr == x:
			return middle
				
		if sqr > x:
			end = middle - 1
		else:
			start = middle + 1
	return end

for i in range(1000):
	res = mySqrt(i)
	sqr = sqrt(i)

	if int(sqr // 1) != res:
		print(res, sqr)
