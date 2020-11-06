class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1,  max(nums)
        while lo < hi:
            mid = (hi + lo)//2
            arr = [int(math.ceil(y/mid)) for y in nums]
            if sum(arr) > threshold:
                lo = mid + 1 
            else:
                hi = mid      
        return hi
