import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        countList = [(v, k) for k, v in count.items()]
        countList.sort(key=lambda x: x[0], reverse=True)
        res = []
        for v, k in countList:
            res.append(v*k)
        return "".join(res)