class MyCalendar:
    
    def __init__(self):
        self.booked = []
    
    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.booked, start)
        if i %2 == 1:
            return False
        j = bisect.bisect_left(self.booked, end)
        if i != j:
            return False
        self.booked[i:i] = [start, end]
        return True