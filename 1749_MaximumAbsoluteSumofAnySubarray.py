class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def maxSubarray(arr):
            globalMax, curSum = arr[0], arr[0]
            for i in range(1, len(arr)):
                curSum = max(curSum + arr[i], arr[i])
                globalMax = max(globalMax, curSum)
            return globalMax
        
        def minSubarray(arr):
            globalMin, curSum = arr[0], arr[0]
            for i in range(1, len(arr)):
                curSum = min(curSum + arr[i], arr[i])
                globalMin = min(globalMin, curSum)
            return globalMin
        
        return max(abs(maxSubarray(nums)), abs(minSubarray(nums)))
