class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = max(seats.index(1), seats[::-1].index(1)) # [0,0,1], [1,0,0]
        for seat, group in itertools.groupby(seats):
            if seat == 0:
                cur_dist = len(list(group))
                max_dist = max(int((cur_dist+1)/2), max_dist)
        return max_dist
