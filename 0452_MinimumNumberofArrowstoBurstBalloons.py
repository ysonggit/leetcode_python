class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n
        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow_pos = points[0][1]
        for i in range(1, n):
            if arrow_pos >= points[i][0]:
                continue
            arrows += 1
            arrow_pos = points[i][1]
        return arrows