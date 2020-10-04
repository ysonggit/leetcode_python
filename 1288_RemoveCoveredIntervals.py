class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        merge = 0
        max_right = 0
        for cur in intervals:
            if cur[1] <= max_right:
                merge += 1
            else:
                max_right = cur[1]
        return len(intervals)-merge