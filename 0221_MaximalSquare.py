class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # similar to 1227 CountSquareSubmatriceswithAllOnes
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
        return max_len**2
