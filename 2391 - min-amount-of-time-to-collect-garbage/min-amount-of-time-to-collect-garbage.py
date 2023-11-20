from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        result = 0

        metalTemp = 0
        paperTemp = 0
        glasTemp = 0

        pos = 0

        for stops in garbage:
            for garbageType in stops:
                result += 1
                if garbageType == "M":
                    result += metalTemp
                    metalTemp = 0
                elif garbageType == "P":
                    result += paperTemp
                    paperTemp = 0
                elif garbageType == "G":
                    result += glasTemp
                    glasTemp = 0
            
            if pos < len(travel):
                metalTemp += travel[pos]
                paperTemp += travel[pos]
                glasTemp += travel[pos]
                pos += 1

        return result
        