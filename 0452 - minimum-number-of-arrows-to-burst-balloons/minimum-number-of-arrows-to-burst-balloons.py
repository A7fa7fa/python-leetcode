# Intuition:

# When looking at a ranges/intervals-related problem, it is always good to sort the array first.
# One thing I learned from Leetcode is to think about a problem backward somehow, in this case, either going from the right of the array to the left or , say, sorting the intervals based on the end value of each interval. (Obsessively don't forget to think about it in a normal way (forward))
# Let's sort the points using the end of each point
# when we try to shoot the first balloon(cover the first interval), we want to shoot as many other balloons as possible(cover as many different intervals as possible).
# The best thing to do would be to shoot at the balloon's end(right side) so that it can cover as many overlapped balloons as possible since they are sorted.
# Algorithm:

# Sort the points based on the end of each point.
# Initialize the curEnd as the end value of the first point. (Shotting the first balloon)
# For each point:
# if its start point is larger than the curEnd, add one more arrow, and update the curEnd to the new endpoint.

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res, curEnd = 1, points[0][1]
        for start, end in points:
            if start > curEnd:
                curEnd = end
                res += 1
        return res
