def longestCommonPrefix(strs: list[str]) -> str:
	
	res = ""
	
	# if strs is empty common prefix is ""
	if len(strs) == 0:
		return res
	
	# find smallest string
	minLen = min([len(s) for s in strs])
	
	# for char in smalles string
	# check every other string
	# if found reduce found by one
	# if not found in all. found is higher than null
	# if found add char to res
	# else return res
	for i in range(minLen):
		
		char = strs[0][i]
		found = len(strs)
		
		for s in strs:
			if s[i] == char:
				found -= 1
		
		if found == 0:
			res += char
		else:
			return res
	
	# if nothing found just return ""
	return res
			
		