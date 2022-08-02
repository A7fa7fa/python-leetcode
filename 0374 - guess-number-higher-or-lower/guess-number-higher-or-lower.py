
def guess(i: int) -> bool:
	n = 6
	if n == i: return 0
	if n < i: return -1
	return 1 



def guessNumber(n: int) -> int:
	
	start = 1
	end = n
	
	while start <= end:
		
		middle = (start + end) // 2
		
		guessResult = guess(middle)
		
		if guessResult == 0:
			return middle
		if guessResult == -1:
			end = middle - 1
		else:
			start = middle + 1
			
	return -1


res = guessNumber(10)
print(res)

