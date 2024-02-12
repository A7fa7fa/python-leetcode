class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        color = {
            "W": 0,
            "B": 0
        }

        pointer = 0
        while pointer < k:
            color[blocks[pointer]] += 1
            pointer += 1

        minPaint = color["W"]

        while pointer < len(blocks):
            color[blocks[pointer - k]] -= 1
            color[blocks[pointer]] += 1
            minPaint = min(minPaint, color["W"])
            pointer += 1

        return minPaint


s = Solution()

s.minimumRecolors("WBBWWBBWBW", 7)