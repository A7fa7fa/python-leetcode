def strStr(haystack: str, needle: str) -> int:
	
	if len(needle) == 0:
		return 0
	
	
	idx  = 0
	needlePointer = 0
	firstIndex = None
	
	while idx < len(haystack):
		
		# char of haystack matches char of needle pointer
		# if it is first needle char set first index
		# if it is last needle char return first index
		# move idx
		# move needle pointer
		if haystack[idx] == needle[needlePointer]:
			if firstIndex == None:
				firstIndex = idx
				
			if needlePointer == len(needle) - 1:
				return firstIndex
			needlePointer += 1
			idx += 1
		
		# if prev found needle char but not work out. move to firstIndex + 1
		# else just move idx one
		# set needle pointer back to default
		# set first index back to default
		else:
			if needlePointer > 0:
				idx = firstIndex + 1
			else:
				idx += 1
			needlePointer = 0
			firstIndex = None

	# no match fount return -1
	return -1

haystack = "mississippi"
needle = "issip"
res = strStr(haystack, needle)
print(res)
