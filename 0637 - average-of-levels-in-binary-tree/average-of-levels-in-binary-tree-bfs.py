import collections
from statistics import mean
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #BFS
        que = [] # first in first out breadth first search
        que = collections.deque()
        que.append(root)
        res = []

        while (que): #loof through every level
            qLen = len(que)
            temp = 0

            for _ in range(qLen): 
                # loop throug every element of current level and extract value. 
                # than add new child of every element to que
                # que wil stop before childs. because there are beyond qLen
                node:TreeNode = que.popleft()
                temp += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.append(temp/qLen)

        
        return res
        
        
        
        
                