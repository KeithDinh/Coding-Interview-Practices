class UndergroundSystem:
    # all travel times: {start: {dest: [times]}}
    # customers: {id: [start, time]}
    def __init__(self):
        self.customers = {}
        self.travelTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = [stationName, t]
        if stationName not in self.travelTimes.keys():
            self.travelTimes[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cs = self.customers
        tvt = self.travelTimes
        if id in cs.keys():
            startStation = cs[id][0]
            startTime = cs[id][1]
            if stationName not in tvt[startStation].keys():
                tvt[startStation][stationName] = [t - startTime]
            else:
                tvt[startStation][stationName].append(t-startTime)
                
            cs.pop(id)
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tvt = self.travelTimes
        return statistics.fmean(tvt[startStation][endStation]) if tvt[startStation][endStation] else None


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)