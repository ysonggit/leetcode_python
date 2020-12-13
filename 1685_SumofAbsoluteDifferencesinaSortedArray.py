class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # nums[i] - nums[0] + nums[i] - nums[1] + ... + nums[i] - nums[i-1] + nums[i+1] - nums[i] + nums[i+2] - nums[i] + ... + nums[n-1] - nums[i]
        # = i * nums[i] - sum(nums[0:i]) - (n-i-1)* nums[i] + sum(nums[i+1:n])
        # = nums[i] * (n-1) + sum(nums[i+1:n]) - sum(nums[0:i])
        n = len(nums)
        res = [0] * n
        prefixSum, suffixSum = [0] * n, [0] * n
        prefixSum[0], suffixSum[n-1] = nums[0], nums[n-1]
        for i in range(1, n):
            prefixSum[i] = nums[i] + prefixSum[i-1]
            suffixSum[n-i-1] = nums[n-1-i] + suffixSum[n-i]
        for i in range(n):
            if i == 0:
                res[i] = abs(i * nums[i]) + abs(suffixSum[i+1] - (n-i-1)* nums[i]) 
            elif i == n-1:
                res[i] = abs(i * nums[i]  - prefixSum[i-1]) + abs(0 - (n-i-1)* nums[i]) 
            else:
                res[i] = abs(i * nums[i]  - prefixSum[i-1]) + abs(suffixSum[i+1] - (n-i-1)* nums[i]) 
        return res
