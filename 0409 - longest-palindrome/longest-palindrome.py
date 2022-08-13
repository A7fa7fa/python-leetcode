def longestPalindrome(s: str) -> int:
	
	
	charCount = dict()
	
	for char in s:
		
		if char in charCount:
			charCount[char] += 1
		else:
			charCount[char] = 1
			
	length = 0
	foundOdd = False
	
	if len(charCount) == 1:
		return list(charCount.values())[0]
	
	for value in charCount.values():
		
		if value % 2 == 0:
			length += value
		else:
			length += value - 1
			foundOdd = True
			
	if foundOdd:
		return length + 1
	return length