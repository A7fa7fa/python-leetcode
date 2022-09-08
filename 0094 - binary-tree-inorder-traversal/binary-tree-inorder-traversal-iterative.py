# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        
        visited = {}
        stack = [root]
        while stack != []:
            node = stack.pop()
            if visited.get(node) is None:
                visited[node] = 1
                if node.right: stack.append(node.right)
                stack.append(node)
                if node.left: stack.append(node.left)
            else:
                result.append(node.val)
        
        return result