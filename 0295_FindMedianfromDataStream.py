from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        A max-heap to store the smaller half of the input numbers
        A min-heap to store the larger half of the input numbers
        """
        self.minheap, self.maxheap = [], []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            if not self.maxheap:
                heappush(self.maxheap, -num)
            else:
                if num > self.minheap[0]: # num should belong to larger half
                    heappush(self.maxheap, -self.minheap[0])
                    heappop(self.minheap)
                    heappush(self.minheap, num)
                else:  # num belongs to the smaller half
                    heappush(self.maxheap, -num)
        else:
            if num > -self.maxheap[0]: # num belongs to the larger half
                heappush(self.minheap, num)
            else: # num belongs to the smaller half
                heappush(self.minheap, -self.maxheap[0])
                heappop(self.maxheap)
                heappush(self.maxheap, -num)
            
    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2.0
        return -self.maxheap[0]
