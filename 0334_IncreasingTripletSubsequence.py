class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, big = float('inf'), float('inf')
        for x in nums:
            if x <= small:
                small = x
            elif x <= big: # x > small
                big = x
            else:
                return True
        return False
