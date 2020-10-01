class MovingAverage:
    
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue= collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue)/len(self.queue)
