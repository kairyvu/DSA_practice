class UndergroundSystem:

    def __init__(self):
        self.hsmap = {} # (start, end): (avg, count)
        self.checkedIn = {} # customerId: (station, time)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        if id not in self.checkedIn:
            return

        startStation, startTime = self.checkedIn[id]
        del self.checkedIn[id]

        totalTime = t - startTime

        if (startStation, endStation) not in self.hsmap:
            self.hsmap[(startStation, endStation)] = (totalTime, 1)
            return
    
        currAvg, count = self.hsmap[(startStation, endStation)]
        newAvg = ((currAvg * count) + totalTime) / (count + 1)
        self.hsmap[(startStation, endStation)] = (newAvg, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.hsmap[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)