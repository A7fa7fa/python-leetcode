# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
    
        
        def dfs(node, currDepth):
            if not node:
                return
            

            
            if currDepth == depth - 1:
                tempL = node.left
                tempR = node.right
                node.left = TreeNode(val=val, left=tempL)
                node.right = TreeNode(val=val, right=tempR)
                return
            
            currDepth += 1
            dfs(node.left, currDepth)
            dfs(node.right, currDepth)
            currDepth -= 1
                
                
        if depth == 1:
            return TreeNode(val=val, left=root)
        
        
        dfs(root, 1)
        return root