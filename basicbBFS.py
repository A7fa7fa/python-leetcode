import collections
from typing import List


def numStopsToDestination(routes: List[List[int]], source: int, target: int) -> int:
    nodes = collections.defaultdict(set)

    for route in routes:
        if len(route) == 1:
            continue

        for i in range(0, len(route)-1):
            currStop = route[i]
            nextStop = route[i+1]
            nodes[currStop].add(nextStop)
        nodes[route[-1]].add(route[0])

    if source not in nodes or target not in nodes:
        return -1

    qu = collections.deque()
    
    qu.append(source)

    maxPath = 1
    visited = set()

    while qu:
        quLen = len(qu)

        while quLen > 0:
            quLen -= 1                
            nextStop = qu.popleft()
            if nextStop in visited:
                continue
            else:
                visited.add(nextStop)
            for neigh in nodes[nextStop]:
                qu.append(neigh)
                if neigh == target:
                    return maxPath
        maxPath += 1

    return -1
  

result = numStopsToDestination([[1,2,7],[3,6,7],[6,8,9,10]], 1, 10)
print("result = ", result)
result = numStopsToDestination([[1,2,7],[3,6,7],[6,8,9,10]], 1, 2)
print("result = ", result)
result = numStopsToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99]], 1, 99)
print("result = ", result)
result = numStopsToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99], [7,99]], 1, 99)
print("result = ", result)
result = numStopsToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99], [7,99]], 1, 1)
print("result = ", result)
result = numStopsToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99], [7,99]], 1, 2)
print("result = ", result)