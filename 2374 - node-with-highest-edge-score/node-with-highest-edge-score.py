from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        
        edgeScore = [0 for _ in range(len(edges))]
        
        for idx, edge in enumerate(edges):
            edgeScore[edge] += idx
                
        heighestEdge = 0
        heighestScore = 0
        
        for idx, edge in enumerate(edgeScore):
            
            if edge > heighestScore :
                heighestScore = edge
                heighestEdge = idx
                
        return heighestEdge
                
        