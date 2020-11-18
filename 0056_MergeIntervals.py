class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, n):
            pre = res[-1]
            l, r = intervals[i]
            if pre[1] < l:
                res.append(intervals[i])
            else:
                if pre[1] >= l:
                    res[-1][1] = max(pre[1], r)
        return res
