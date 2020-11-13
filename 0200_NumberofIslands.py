class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            m, n = len(grid), len(grid[0])
            if i >= m or i < 0 or j >= n or j < 0:
                return
            if grid[i][j] =='0':
                return
            grid[i][j] = '0'
            for d in [(0,1),(1,0),(0,-1), (-1,0)]:
                dfs(grid, i+d[0], j+d[1])
                
        islands = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    islands += 1
        return islands