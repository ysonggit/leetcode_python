class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = min(nums), max(nums)
        '''
        Check if there exists a subarray length >= k and sum >= 0
        '''
        def averGTmid(nums, mid, k):
            s = 0
            # sum(a_0, ... a_k-1)/k >= mid
            # => sum(a_0-mid, .., a_k-1 - mid) >= 0
            for i in range(k):
                s += nums[i] - mid
            if s >= 0:
                return True
            prev, min_s = 0, 0
            for i in range(k, len(nums)):
                s += nums[i] - mid
                prev += nums[i-k] - mid
                min_s = min(min_s, prev)
                if s >= min_s:
                    # means average between min_s and s >= 0
                    return True
            return False
      
        while right - left > 0.00001:
            mid = (left + right)/2
            if averGTmid(nums, mid, k):
                left = mid
            else:
                right = mid
        return left
