class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 2:
            return 0
        cost = 0
        # deque is wrong because the numbers must be sorted each iteration
        heapq.heapify(sticks) 
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            heapq.heappush(sticks, a+b)
            cost += a + b
        return cost
