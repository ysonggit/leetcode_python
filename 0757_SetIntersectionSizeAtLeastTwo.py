class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort the intervals by right bound asc, then by left bound desc
        # [1, 3] [2,100], [90,100] --> [1,3],[90,100],[2,100] -> [2,3,99,100]
        # assume no interval like [1,1]
        intervals.sort(key=lambda x: (x[1], -x[0]))
        minset = [intervals[0][1]-1, intervals[0][1]] # closest 2 nums to the next interval 
        # can represent using just 2 variables, use arr for debugging
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            if left <= minset[-2] and right >= minset[-1]:
                continue
            if minset[-1]>= left:
                minset.append(right)
            if minset[-1] < right-1:
                minset.append(right-1)
                minset.append(right)
        return len(minset)