from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for monster in range(len(dist)):
            dist[monster] = dist[monster]/speed[monster]
        
        dist.sort()

        for monster in range(len(dist)):
            if monster >= dist[monster]:
                return monster
        return len(dist)         
        