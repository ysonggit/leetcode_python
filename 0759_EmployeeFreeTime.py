"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        '''
        1. expand the nested intervals and sort
        2. merge interval
        3. find the gap by excluding lower/upper ones
        '''
        intervals = []
        for emp in schedule:
            intervals += emp
        intervals.sort(key=lambda x: x.start)
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if merged[-1].end >= cur.start:
                merged[-1].end = max(cur.end, merged[-1].end)
            else:
                merged.append(cur)
        res = []
        # [1,3] [4,10]
        for i in range(len(merged)-1):
            if merged[i+1].start - merged[i].end > 0:
                gap = Interval(merged[i].end, merged[i+1].start)
                res.append(gap)
        return res
