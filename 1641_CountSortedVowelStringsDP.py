class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 6 for _ in range(n+1)]
        # dp[i][j] number of strings of lengh i, with j vowels
        # dp[1][j] = j
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for j in range(6):
            dp[1][j] = j
        for i in range(2, n+1):
            dp[i][1] = 1 # aa
            for j in range(2, 6):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n][5]
