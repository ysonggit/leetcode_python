class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        height_diffs = []
        n = len(heights)
        heapq.heapify(height_diffs)
        for i in range(0, n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(height_diffs, diff)
                if len(height_diffs) > ladders: # ladders first
                    bricks -= heapq.heappop(height_diffs)
                    if bricks < 0:
                        return i
        return n - 1
