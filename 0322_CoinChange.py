class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # D[j] here represents the fewest number of coins to make up amount (j) using coins[0],coins[1],...,coins[i]
        # D[j] = min(D[j], D[j-coin]+1) for in each coin value 
        '''
        coins = [1,2,5], amount = 11
        dp: 0 1 2 3 4 5 6 7 8 9 10 11
            0 1 1 2 2 1 2 2 3 3  2  3 
        '''
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)
        if dp[amount] == math.inf:
            return -1
        return dp[amount]
