class Solution:
	
	def isPalindrome(self, s) -> bool:
		
		start = 0
		end = len(s) - 1
		while start <= end:
			if s[start] == s[end]:
				start += 1
				end -= 1
			else:
				return False
		return True
	
	# slow
	def longestPalindrome(self, s: str) -> str:
		longest = ""
		
		for i in range(len(s), 0, -1):
			if i > len(longest):
				for j in range(len(s[:i])):
					temp = s[j:i]
					if len(temp) > len(longest) and self.isPalindrome(temp):             
						longest = temp
			
		return longest
			
	
	# fast
	def longestPalindrome2(self, s: str) -> str:
		if len(s) <= 1:
			return s
		if len(s) == 2 and s[0] == s[1]:
			return s
		if s == s[::-1]:
			return s
		
		longest =  ""
		for i in range(len(s)):
			lPtr, rPtr = i, i
			
			while lPtr >= 0 and rPtr < len(s) and s[lPtr] == s[rPtr]:
				
				if  rPtr + 1 - lPtr > len(longest):
					longest = s[lPtr: rPtr + 1]
				lPtr -= 1
				rPtr += 1
			
			
			lPtr, rPtr = i, i+1
			while lPtr >= 0 and rPtr < len(s) and s[lPtr] == s[rPtr]:
				
				if  rPtr + 1 - lPtr > len(longest):
					longest = s[lPtr: rPtr + 1]
				lPtr -= 1
				rPtr += 1

			
		return longest
			