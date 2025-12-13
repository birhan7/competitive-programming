class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.duration = defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkin[id]
        if f"{start}#{stationName}" in self.duration:
            self.duration[f"{start}#{stationName}"][0] += t - time
            self.duration[f"{start}#{stationName}"][1] += 1
        else:
            self.duration[f"{start}#{stationName}"].append(t - time)
            self.duration[f"{start}#{stationName}"].append(1)
        del self.checkin[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, size = self.duration[f"{startStation}#{endStation}"]
        return total / size
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)