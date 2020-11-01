class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n < 2:
            return True
        intervals.sort(key=lambda x: x[0])
        for i in range(1, n):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
