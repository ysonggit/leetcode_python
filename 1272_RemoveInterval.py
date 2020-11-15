class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for a, b in intervals:
            if toBeRemoved[0] <= a and b <= toBeRemoved[1]:
                continue
            if a >= toBeRemoved[1] or b <= toBeRemoved[0]:
                res.append([a, b])
            if a < toBeRemoved[0] < b:
                res.append([a, toBeRemoved[0]])
                toBeRemoved[0] = b
            if a < toBeRemoved[1] < b:
                res.append([toBeRemoved[1], b]) 
                toBeRemoved[1] = a
        return res
