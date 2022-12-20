import collections
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        que = collections.deque([0])
        # que.append(0)

        visited = set({0})

        while que:
            qLength = len(que)
            for _ in range(qLength):
                key = que.popleft()
                visited.add(key)
                for room in rooms[key]:
                    if room not in visited:
                        que.append(room)
                    
        return len(visited) == len(rooms)

    # faster
    def canVisitAllRoomsDfs(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def dfs(node):
            for n in rooms[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(n)

        
        visited.add(0)
        dfs(0)

        return len(visited) == len(rooms)

s = Solution()
# rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
result = s.canVisitAllRooms(rooms=rooms)
print(result)