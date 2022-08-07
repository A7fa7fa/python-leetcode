class Solution:
    def searchRange(nums: list[int], target: int) -> list[int]:
        
        
        start = 0
        end = len(nums) - 1
        
        res = [end, -1]
        
        foundLeft = False
        foundRight = False
        
        while start <= end:
            
            mid = (start + end) // 2
            
            
			# found target
            if nums[mid] == target:
				# new left boundary is min from mid and prev found
                res[0] = min(mid, res[0])
				# new right boundary is max from mid and prev found
                res[1] = max(mid, res[1])
    
                if not foundLeft: #left bpundary was not found
					# left boundary found if mid is at 0 or mid -1 is smaller than mid
                    if mid == 0 or nums[mid] > nums[mid - 1]:
                        foundLeft = True
                        start = res[0] # to find right side set new start to left boundary
                        end = len(nums) - 1 # set end to end of list
                    else: # left bpoundary not found so move left
                        end = mid - 1
                        
                elif not foundRight:
					# right boundary found if mid is most right element or mid + 1 is bigger than target
                    if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                        foundRight = True
                    else: # right boundary not found so move right
                        start = mid + 1
                    
                
            
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            
            if foundLeft and foundRight:
                break
        
        if not foundLeft and not foundRight:
            return [-1, -1]
                
        return res