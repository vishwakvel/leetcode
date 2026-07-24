class UndergroundSystem:
    # average time requires total time and number of customers
    # add to total time during checkout
    # every time checkout called is a new customer so that keeps track of # of customers

    def __init__(self):
        self.hashmap = {} # id to (start, time)
        self.routes = {} # (start, end) to (total time, count)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hashmap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.hashmap[id]
        if (start, stationName) not in self.routes:
            self.routes[(start, stationName)] = [0, 0]
        
        self.routes[(start, stationName)][0] += t - time
        self.routes[(start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.routes[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
