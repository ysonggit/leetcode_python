class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://leetcode.com/problems/coin-change-2/discuss/99212/Knapsack-problem-Java-solution-with-thinking-process-O(nm)-Time-and-O(m)-Space
        # dp[i][j] : the number of combinations to make up amount j by using the first i types of coin
        # 1. not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
        # 2. using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]

        m, n = len(coins), amount
        dp = [[]]*(m+1)
        for i in range(m+1):
            dp[i] = [0] * (n+1)
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]] if j >= coins[i-1] else dp[i-1][j]
            
        return dp[m][n]