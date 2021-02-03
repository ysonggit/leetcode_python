class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 1
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x, y = i+dx, j+dy
                if 0<= x< len(grid) and 0<= y <len(grid[0]) and grid[x][y] == 0:
                    dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            # first col and last col
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n-1)
        for i in range(n):
            # first row and last row
            if grid[0][i] == 0:
                dfs(0, i)
            if grid[m-1][i] == 0:
                dfs(m-1, i)
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]==0:
                    dfs(i, j)
                    res += 1
        return res
