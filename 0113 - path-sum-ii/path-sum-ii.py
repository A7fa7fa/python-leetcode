# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
		
		
		def dfs(node, res, path):
			
			# visit
			if not node:
				return res
			
			path.append(node.val)
			
			if not node.left and not node.right:
				if sum(path) == targetSum:
					res.append(path[:])

			
			#traverseleft
			dfs(node.left, res, path)
			#traverseright
			dfs(node.right, res, path)
			#backtrack
			path.pop()
			
			
		res = list()
		path = list()
		
		dfs(root, res, path)
		
		return res

node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.left = TreeNode(7)
node.left.left.right = TreeNode(2)
node.right = TreeNode(8)
node.right.left = TreeNode(13)
node.right.right = TreeNode(4)
node.right.right.left = TreeNode(5)
node.right.right.right = TreeNode(1)

s = Solution()
print(s.pathSum(node, 22))