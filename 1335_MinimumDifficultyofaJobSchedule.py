class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp[i][j]: min difficulty of finishing jobs [:i] and remaining j cuts
        #   [7,1, 7,1, 7, 1], d = 3
        #    0 1  2 3  4  5
        # 0  7 7  7 7  7  7
        # 1  x 8 14 8  14 8
        # 2  x x 15 15 15 15
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float('inf')] * n for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[0][i] = max(jobDifficulty[i], dp[0][i-1])
        for i in range(1, d):
            for j in range(i, n):
                localmax = jobDifficulty[j]
                for k in range(j, i-1, -1): # k in [i, j]
                    localmax = max(localmax, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] +localmax)
        #for r in dp:
        #    print(r)
        return dp[d-1][n-1]       
        
