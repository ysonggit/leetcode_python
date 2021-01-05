class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        prefixSum = [0] * (n+1)
        # at i, find index j such at prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        # 2 * prefixSum[i] <= prefixSum[j]
        # 2 * prefixSum[j] <= prefixSum[-1] + prefixSum[i]
        for i in range(1, n+1):
            prefixSum[i] = nums[i-1] + prefixSum[i-1]
        res = 0
        #           0 1 2 3 4  5  6  
        # prefixSum 0 1 3 5 7 12 12
        #               i   j  k  
        for i in range(1, n):
            j = bisect.bisect_left(prefixSum, 2*prefixSum[i])
            k = bisect.bisect_right(prefixSum, (prefixSum[-1] + prefixSum[i])//2 )
            res += max(0, min(n, k) - max(i+1, j))
        return res % (10**9 + 7)
