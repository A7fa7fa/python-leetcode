import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        even = len(board) % 2 == 0
        # expand matrix into list
        boardList = list()
        boardList.append(0)
        for i in range(len(board) - 1, -1, -1):
            if even:
                if (i + 1) % 2 == 0:
                    boardList.extend(board[i])
                else:
                    boardList.extend(board[i][::-1])
            else:
                if (i + 1) % 2 == 0:
                    boardList.extend(board[i][::-1])
                else:
                    boardList.extend(board[i])

        # bfs list
        que = collections.deque()
        que.append(1)
        visited = set()
        steps = -1
        finishCell = len(board) * len(board)

        while que:
            # count steps
            steps += 1
            nextSteps = len(que)

            for _ in range(nextSteps):
                position = que.popleft()
                # if not visited before
                if position in visited:
                    continue
                visited.add(position)

                # if positiion is last tile return amount of steps taken
                if position == finishCell:
                    return steps

                # every field has 1-6 choices/nodes
                for nexPosition in range(position + 1, min(position + 6, finishCell) + 1):
                    # if node is -1 add step to que
                    if boardList[nexPosition] == -1:
                        if nexPosition not in visited:
                            que.append(nexPosition)
                        # visited.add(nexPosition)
                    # if node is not -1 follow to ladder/snake
                    else:
                        if boardList[nexPosition] not in visited:
                            que.append(boardList[nexPosition])
                        # visited.add(boardList[nexPosition])
        return -1


s = Solution()
board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
res = s.snakesAndLadders(board)
print(res)
