import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        busPerStop = collections.defaultdict(set)

        for busIdx in range(len(routes)):
            if len(routes[busIdx]) == 1:
                continue

            for i in range(len(routes[busIdx])):
                currStop = routes[busIdx][i]
                busPerStop[currStop].add(busIdx)

        if source not in busPerStop or target not in busPerStop:
            return -1

        busRides = collections.deque()
        
        visitedStop = set()
        visitedBus = set()
        numOfBus = 0

        for possibleStartBus in busPerStop[source]:
          busRides.append(possibleStartBus)

        while busRides:
            quLen = len(busRides)
            numOfBus += 1

            while quLen > 0:
                currBus = busRides.popleft()
                quLen -= 1                

                if currBus in visitedBus:
                    continue
                else:
                    visitedBus.add(currBus)

                nextPossibleBusses = set()
                for stop in routes[currBus]:
                    if stop == target:
                        return numOfBus
                    
                    if stop in visitedStop:
                        continue
                    else:
                        visitedStop.add(stop)

                    nextPossibleBusses.update(busPerStop[stop])
                
                for bus in nextPossibleBusses:
                    if bus not in visitedBus:  
                      busRides.append(bus)

        return -1
    

s = Solution()

result = s.numBusesToDestination([[1,2,7],[3,6,7],[6,8,9,10]], 1, 10)
print("result = ", result)
result = s.numBusesToDestination([[1,2,7],[3,6,7],[6,8,9,10]], 1, 2)
print("result = ", result)
result = s.numBusesToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99]], 1, 99)
print("result = ", result)
result = s.numBusesToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99], [7,99]], 1, 99)
print("result = ", result)
result = s.numBusesToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99], [7,99]], 1, 1)
print("result = ", result)
result = s.numBusesToDestination([[1,2,7],[3,6,7],[6,8,9,10],[10,11,99], [7,99]], 1, 2)
print("result = ", result)