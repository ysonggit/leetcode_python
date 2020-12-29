class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0.0
        lastFinish = 0
        waiting = 0
        for start, cost in customers:
            lastFinish += cost
            waiting += max(lastFinish - start, cost)
            #print(max(lastFinish - start, cost))
            lastFinish = max(lastFinish, start+cost)
        return waiting/len(customers)
