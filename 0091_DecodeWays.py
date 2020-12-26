class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = j there are j ways to decode s[:i]
        #      3 2 6
        # dp 1 1 1 2
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(2, n+1):
            decodeOne = s[i-1] > '0'
            decodeTwo = '10'<= s[i-2:i] <= '26'
            if decodeOne:
                dp[i] += dp[i-1]
            if decodeTwo:
                dp[i] += dp[i-2]
        return dp[n]
