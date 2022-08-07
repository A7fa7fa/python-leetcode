def lengthOfLongestSubstring(s: str) -> int:
	
	# key is char: value is position of char in currentStr 
	charIndexMap = dict()
	longestStr = ""
	currentStr = ""

	for char in s:
		# if character is not in current string
		# add char to character index with position in currentStr
		# add char to current string
		# if current str is longer than longest update longest str 
		if char not in charIndexMap:
			charIndexMap[char] = len(currentStr)
			currentStr += char
			if len(currentStr) > len(longestStr):
				longestStr = currentStr
		else:
			# remove chars from current string including char
			removedChars = currentStr[:charIndexMap[char] + 1]
			# update current str up from char
			currentStr = currentStr[charIndexMap[char] + 1:]
			# remove all chars removed from current string in index
			for c in removedChars:
				del charIndexMap[c]
			# update new position of chars in index  
			for key, value in charIndexMap.items():
				charIndexMap[key] = value - len(removedChars)
			# add new char to index
			charIndexMap[char] = len(currentStr)
			# add new char to current str
			currentStr += char
	
	return len(longestStr)


res = lengthOfLongestSubstring(" ")
print(res)
res = lengthOfLongestSubstring("1234")
print(res)
res = lengthOfLongestSubstring("1231")
print(res)
res = lengthOfLongestSubstring("1111")
print(res)
res = lengthOfLongestSubstring("dvdf")
print(res)


def lengthOfLongestSubstring(s: str) -> int:
	
	maxRep = 0
	curStr =  ""
	
	
	foundChar = dict()
	
	for char in s:
		
		
		if char not in foundChar:            
			foundChar[char] = len(curStr)
			curStr += char 
			maxRep = max(maxRep, len(curStr))

		else:
			maxRep = max(maxRep, len(curStr))
			remove = curStr[:foundChar[char] + 1]
			curStr = curStr[foundChar[char] + 1:]
			for c in remove:
				del foundChar[c]
			
			for key, value in foundChar.items():
				foundChar[key] = value - len(remove)
				
			foundChar[char] = len(curStr)
			curStr += char
				
	
	return maxRep
