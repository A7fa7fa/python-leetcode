from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = (Counter(nums))  # init
        frequencies = list(frequencies.items())  # transform
        frequencies.sort(key=lambda x: x[1], reverse=True)  # sort
        result = []
        for i in range(k):
            result.append(frequencies[i][0])
        return result
