from statistics import mean
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self, node, level, perLevel):
            if not node:
                return
            
            if level < len(perLevel):
                perLevel[level].append(node.val)
            else:
                perLevel.append([node.val])                                                    
            
            if node.left:
                self.traverse(node.left, level+1, perLevel)
            if node.right:
                self.traverse(node.right, level+1, perLevel)
            
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        level = 0
        perLevel = []
        
        self.traverse(root, level, perLevel)
        
        return [mean(lvl) for lvl in perLevel]
        
        
        
        
                
            