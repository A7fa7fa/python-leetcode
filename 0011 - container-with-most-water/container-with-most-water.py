from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		
		def volume(height, i1, i2):
			return min(height[i1], height[i2]) * (i2 - i1)
			
				
		left = 0
		right = len(height) - 1
		res = 0
		
		while left < right:
			
			res = max(res, volume(height, left, right))
			
			if height[left] > height[right]:
				# move right pointer until higher is found
				temp = right
				while temp > left and height[temp] <= height[right]:
					temp -= 1
				
				right = temp
			else:                
				# move left pointer until higher is found
				temp = left
				while temp < right and height[temp] <= height[left]:
					temp += 1
				left = temp
		
		return res          
			
		
		
		