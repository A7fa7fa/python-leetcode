from typing import List


class Graph:

    # could be dict of minheaps where values are (cost, toEdge) 
    graph: List[List[int]]
    size: int

    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.graph = [[0]*n for _ in range(n)]
        self.size = n
        for [fromEdge, toEdge, weight] in edges:
            self.__editWeight(fromEdge, toEdge, weight)

    def __editWeight(self, fromEdge, toEdge, weight) -> None:
        self.graph[fromEdge][toEdge] = weight

    def addEdges(self, edges: List[List[int]]) -> None:
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        self.__editWeight(*edge)

    def shortestPath(self, startNode: int, targetNode: int) -> int:
        # dijkstra

        # init all nodes with infinit 
        # this should be a min heap
        path = [float("inf") for i in range(self.size)]

        path[startNode] = 0
        unvisitedNodes = set([i for i in range(self.size)])
        
        currentNode = startNode
        currentPath = 0

        while currentNode >= 0:
            unvisitedNodes.discard(currentNode)
            currentPath = path[currentNode]
            for i in range(self.size):
                if self.graph[currentNode][i] != 0:
                    path[i] = min(path[i], currentPath + self.graph[currentNode][i])
            
            nextNode = -1
            minPath = float("inf")
            # this should be just a heappop
            for i in unvisitedNodes:
                if path[i] < minPath:
                    nextNode = i
                    minPath = path[i]

            currentNode = nextNode
        if path[targetNode] == float("inf"):
            return -1
        
        return path[targetNode]


n = 4
initEdges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
obj = Graph(n, initEdges)
param_2 = obj.shortestPath(3, 2)
param_2 = obj.shortestPath(0, 3)
obj.addEdge([1, 3, 4])
param_2 = obj.shortestPath(0, 3)

n = 13
initEdges = [[6,12,315086],[4,6,434499],[8,4,753794],[4,8,25425],[12,7,790970],[1,12,617809],[12,3,162762],[6,10,831419],[1,3,161356],[2,9,78885],[9,6,377317],[9,2,21891],[0,4,8226],[7,12,182349],[5,10,113773],[4,10,538290],[1,0,733504],[11,2,105677],[8,11,716157],[0,8,598757],[12,6,390446],[6,7,231085],[0,11,306911],[1,11,201790],[9,8,632445],[4,2,11198],[10,4,480988],[12,0,855344],[11,1,951787],[1,9,847441],[12,5,265162],[3,4,836015],[3,6,10355],[6,4,986910],[7,1,789806],[4,11,601682],[11,12,373853],[7,9,975447],[2,11,408606],[6,1,177887],[11,5,245495],[10,0,107270]]
obj = Graph(n, initEdges)

obj.addEdges([[6,5,962787],[3,10,6961]])

path = obj.shortestPath(*[12,6])
s = 173117
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[8,8])
s = 0
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[12,1])
s = 351004
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[8,9,763398],[5,9,787580],[5,6,5710],[3,8,2990],[2,12,580988],[1,5,749003]])

path = obj.shortestPath(*[3,10])
s = 6961
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[8,5,1999]])

path = obj.shortestPath(*[7,2])
s = 478766
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[8,7,711]])

path = obj.shortestPath(*[0,2])
s = 19424
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[10,8])
s = 140921
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[5,6])
s = 5710
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[9,4,490870]])

path = obj.shortestPath(*[2,5])
s = 597179
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[2,0,663],[7,5,518],[8,10,91]])

path = obj.shortestPath(*[10,2])
s = 126694
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[7,3,687804],[0,12,216563]])

path = obj.shortestPath(*[12,1])
s = 350578
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[1,8,91]])

path = obj.shortestPath(*[3,5])
s = 4219
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[5,3,382061]])
path = obj.shortestPath(*[11,1])

s = 324817
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[0,3,53]])

path = obj.shortestPath(*[8,12])
s = 183060
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[8,0,10],[12,2,3],[4,12,901278]])
path = obj.shortestPath(*[3,7])
s = 3701
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[3,7,2],[10,2,165121],[3,1,606436]])
path = obj.shortestPath(*[2,8])
s = 3706
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[10,11,937623]])
path = obj.shortestPath(*[12,5])
s = 1239
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[2,5,25648]])
path = obj.shortestPath(*[0,8])
s = 3043
print(f"{path==s} - path -> {s}", path)



obj.addEdges([[11,8,1],[4,7,1],[10,9,1],[5,12,613478]])
path = obj.shortestPath(*[11,4])
s = 8237
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[7,7])
s = 0
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[11,6,1]])
path = obj.shortestPath(*[9,4])
s = 30780
print(f"{path==s} - path -> {s}", path)


obj.addEdges([[2,1,1],[5,2,1]])
path = obj.shortestPath(*[11,7])
s = 66
print(f"{path==s} - path -> {s}", path)


obj.addEdges([[12,11,1],[6,8,709797]])
path = obj.shortestPath(*[10,4])
s = 30220
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[5,6])
s = 5710
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[7,6,1]])
path = obj.shortestPath(*[0,1])
s = 575
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[5,12])
s = 182507
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[5,1])
s = 2
print(f"{path==s} - path -> {s}", path)
path = obj.shortestPath(*[0,5])
s = 573
print(f"{path==s} - path -> {s}", path)

obj.addEdges([[10,8,1]])
