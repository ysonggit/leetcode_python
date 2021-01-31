class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m <= 1:
            return 0
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    for k in range(j+1, n):
                        if grid[i][k] == 1:
                            res += dp[j][k]
                            dp[j][k]+= 1
        return res  
