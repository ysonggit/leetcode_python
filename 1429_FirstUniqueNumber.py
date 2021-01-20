class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniqueQueue = deque([])
        self.uniqueMap = {}
        for i in nums:
            self.add(i)
            
    def showFirstUnique(self) -> int:
        while self.uniqueQueue and not self.uniqueMap[self.uniqueQueue[0]]:
            self.uniqueQueue.popleft()
        if not self.uniqueQueue:
            return -1
        return self.uniqueQueue[0]

    def add(self, value: int) -> None:
        if value not in self.uniqueMap:
            self.uniqueMap[value] = True
            self.uniqueQueue.append(value)
        else:
            self.uniqueMap[value] = False
