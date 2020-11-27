class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[i][j]=true if the sum j can be formed by array elements in subset nums[0]..nums[i], otherwise false
        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total//2;
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[n][target]
