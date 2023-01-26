from typing import List


class Solution:
    def dfs(self, position: int, distance: list, steps: int) -> None:
        """
        Helper function to recursive traverse graph
        """
        if position == -1:  # no edge so end of path
            return
        steps += 1  # add one to step
        if distance[position] <= 0:  # no distance reocrded so not visited before
            distance[position] = steps  # save distance to list
            self.dfs(edges[position], distance, steps)  # follow edge

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        # keep track of distance from node1
        distanceNode1: list = [-1] * len(edges)
        # keep track of distance from node2
        distanceNode2: list = [-1] * len(edges)
        distanceNode1[node1] = 0
        distanceNode2[node2] = 0

        self.dfs(node1, distanceNode1, 0)
        self.dfs(node2, distanceNode2, 0)

        minIdx = -1
        maxDistance = float('inf')

        for node in range(len(edges)):
            isReachable = (distanceNode1[node] !=
                           -1 and distanceNode2[node] != -1)
            distance = max(distanceNode1[node], distanceNode2[node])
            if isReachable:
                if distance < maxDistance:
                    maxDistance = distance
                    minIdx = node
                elif distance == maxDistance:
                    minIdx = min(node, minIdx)

        return minIdx


s = Solution()
edges = [4, 3, 0, 5, 3, -1]
node1 = 4
node2 = 0
res = s.closestMeetingNode(edges, node1, node2)
print(res)
