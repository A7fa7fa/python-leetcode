class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        leftFlip = 0
        rightFlip = s.count("0")

        result = leftFlip + rightFlip

        for idx in range(len(s)):
            if s[idx] == "0":
                rightFlip -= 1
            else:
                leftFlip += 1

            result = min(leftFlip + rightFlip, result)
        return result
