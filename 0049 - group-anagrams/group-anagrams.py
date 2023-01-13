from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # TLE!
        # result = []
        # visited = set()

        # for idx, word in enumerate(strs):
        #     if word not in visited:
        #         newGroup = [word]
        #         for i in range(idx+1, len(strs)):
        #             if len(word) == len(strs[i]) and Counter(word) == Counter(strs[i]):
        #                 newGroup.append(strs[i])
        #                 visited.add(strs[i])
        #         result.append(newGroup)
        # return result

        anagrams = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagrams[sortedWord].append(word)

        return anagrams.values()
