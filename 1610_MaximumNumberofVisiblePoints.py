import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:   
        overlaps = 0
        polars = []
        for p in points:
            if p[0]==location[0] and p[1] == location[1]:
                overlaps+=1
            else:
                polars.append(atan2(p[1]-location[1], p[0]-location[0])* 180/pi)
        polars.sort()
        polars += [x + 360 for x in polars]
        max_pts = 0
        i = 0
        for j in range(len(polars)):
            while polars[j] - polars[i] > angle:
                i+=1
            max_pts = max(max_pts, j-i+1)
        return max_pts+overlaps