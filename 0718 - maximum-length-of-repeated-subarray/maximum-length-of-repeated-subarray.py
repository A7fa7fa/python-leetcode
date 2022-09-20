from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        # create matrix of size nums2 + 1 * nums1 + 1 and fill wiht 0
        # i move from the back of the list to te front and add the value before if it is a match
        # so it has to be one more - or i woul dhave to check every time if i+1 is out of bound
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        
        for i in range(len(nums1) - 1, -1, -1 ):
            for j in range(len(nums2) - 1, -1, -1 ):
                # if there is a match add 1 and add the value of the match before
                # if there was a match i know te length is one more
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        
        # find the longest subset
        return max([max(row) for row in memo])
                
                