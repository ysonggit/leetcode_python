class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips_at_odd, chips_at_even = 0, 0
        for p in position:
            if p % 2 == 0:
                chips_at_even += 1
            else:
                chips_at_odd += 1
        return min(chips_at_odd, chips_at_even)
