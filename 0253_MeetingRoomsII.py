class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        rooms = []
        intervals.sort(key=lambda x: x[0])
        for cur in intervals:
            if rooms and cur[0] >= rooms[0]:
                earliest_end_sameroom = cur[1]
                heapq.heapreplace(rooms, earliest_end_sameroom)
            else:
                heapq.heappush(rooms, cur[1])
        return len(rooms)