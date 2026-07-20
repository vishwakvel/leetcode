class UndergroundSystem:

    def __init__(self):
        self.checkins = {} # id to (start station, start time)
        self.routes = {} # (start station, end station) to (totaltime, count)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation, starttime = self.checkins[id]
        route = (startstation, stationName)

        if route not in self.routes:
            self.routes[route] = [0, 0]
        
        self.routes[route][0] += t - starttime
        self.routes[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime, count = self.routes[(startStation, endStation)]
        return totaltime/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
