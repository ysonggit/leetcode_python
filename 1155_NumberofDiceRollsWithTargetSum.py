class Solution:      
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/686109/Java-DP-Explanation-with-diagram
        # dp[i][j] = The number of ways we can roll i dice to get a target of j.
        # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j - 2] + ... + dp[i - 1][j - k] for k in 1 .. f 
        '''
        2 dice, with 5 faces [1, 2, 3, 4, 5], 
        target is 7. 
        | dice \ target  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
        |----------------|---|---|---|---|---|---|---|---|
        | 0              | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        | 1              | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
        | 2              | 0 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
        '''
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                for k in range(1, f+1):
                    if j-k >=0:
                        dp[i][j] += dp[i-1][j-k]
        return dp[d][target]%(10**9+7)
        
