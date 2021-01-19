class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # See Problem 516 for the basic DP logic
        # dp[i][j] represents the longest palin from s[i] to s[j] and the prev char
        # dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j] and no consecutive chars
        #           max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1])
        #  bbab
        #  1000       1000       1000      1223
        #  0100  -->  0100   --> 0113  --> 0113
        #  0010       0011       0011      0011
        #  0001       0001       0001      0001
        n = len(s)
        dp = [[(0, "")] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and dp[i+1][j-1][1] != s[i]:
                    dp[i][j] = (dp[i+1][j-1][0] + 2, s[i])
                else:
                    t = [dp[i+1][j], dp[i][j-1], dp[i+1][j-1]]
                    t.sort(key=lambda x: x[0])
                    dp[i][j] = t[2]
        return dp[0][n-1][0]
