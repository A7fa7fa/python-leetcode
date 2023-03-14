from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        paths = list()

        def dfs(path: list, node: TreeNode) -> None:

            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append(int("".join(path)))
            if node.left:
                dfs(path, node.left)
            if node.right:
                dfs(path, node.right)
            path.pop()

        dfs([], root)
        return sum(paths)
