
# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        #bfs
        
        que = deque()
        que.append(root)
        
        result = []
        
        while que:
            
            qLen = len(que)
            res = []
            
            for _ in range(qLen):
                
                temp = que.popleft()
                res.append(temp.val)
                if temp.children:
                    for node in temp.children:
                        que.append(node)
            
            result.append(res)
            
            
                
        return result
