class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] represents the longest palin from s[i] to s[j]
        # dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j]
        #           max(dp[i+1][j], dp[i][j-1])
        #  bbab
        #  1000       1000       1000      1223
        #  0100  -->  0100   --> 0113  --> 0113
        #  0010       0011       0011      0011
        #  0001       0001       0001      0001
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
