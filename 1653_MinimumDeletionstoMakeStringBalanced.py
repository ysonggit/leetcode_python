class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1) # d[i] = j minimal j deletions to make s[:i] valid 
        bcount_sofar = 0
        #    "aababbab"
        # dp 000011122
        for i, c in enumerate(s):
            if c == 'a':
                # either keep a while deleting B's (bcount_sofar)
                # or delete a
                dp[i+1] = min(dp[i]+1, bcount_sofar)
            else:
                dp[i+1] = dp[i]
                bcount_sofar += 1
        return dp[n]
