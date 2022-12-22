from typing import List

class Solution:
	def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

		dislikeGraph = dict()

		for i in range(1, n+1):
			dislikeGraph[i] = set()

		# build dislikeGraph 
		for dislike in dislikes:
			dislikeGraph[dislike[0]].add(dislike[1])
			dislikeGraph[dislike[1]].add(dislike[0])

		# dfs
		def dfs(visited, person, color):
			if visited[person] == 0:
				visited[person] = color
				if person in dislikeGraph.keys():
					for dislike in dislikeGraph[person]:
						dfs(visited, dislike, color * -1)
				return
			elif visited[person] != color:
				visited[0] = -1

		visited = [0] * (n +1)
		color = -1
		for i in range(1, n+1):
			if visited[0] != 0:
				return False
			if visited[i] == 0:
				dfs(visited, i, color * -1)
		return True
		


		
s = Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
res = s.possibleBipartition(n=n, dislikes=dislikes)
print(True, res)

n = 3
dislikes = [[1,2],[1,3],[2,3]]
res = s.possibleBipartition(n=n, dislikes=dislikes)
print(False, res)

n = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
res = s.possibleBipartition(n=n, dislikes=dislikes)
print(False, res)