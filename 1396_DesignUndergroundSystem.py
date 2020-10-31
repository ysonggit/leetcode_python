class UndergroundSystem:

    def __init__(self):
        self.usersIn = {}
        self.trips = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.usersIn[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, start = self.usersIn[id] 
        self.trips[(station, stationName)].append(t - start)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travelTimes = self.trips[(startStation, endStation)]
        return sum(travelTimes)/len(travelTimes)
