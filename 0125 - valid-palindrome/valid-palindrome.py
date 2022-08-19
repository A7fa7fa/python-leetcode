def isPalindrome(s: str) -> bool:
	
	
	norm = "".join([char.lower() for char in s if char.isalnum()])
			
	start = 0
	end = len(norm) -1
	while start < end:
		if norm[start] != norm[end]:
			return False
		start += 1
		end -= 1
	
	return True
