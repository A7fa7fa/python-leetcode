import collections


class UndergroundSystem:

    def __init__(self):
        self.checkedInCustomers = dict()
        self.fares = collections.defaultdict(list)

    def __getFareName(self, startStation: str, endStation: str) -> str:
        return f'{startStation}~{endStation}'

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedInCustomers[id] = (t, stationName,)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, startStation = self.checkedInCustomers[id]
        self.fares[self.__getFareName(
            startStation, stationName)].append(t-startTime)
        del self.checkedInCustomers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        fare = self.__getFareName(startStation, endStation)
        return sum(self.fares[fare]) / len(self.fares[fare])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
