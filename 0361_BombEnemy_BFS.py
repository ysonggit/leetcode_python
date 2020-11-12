class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:

        def bfs(grid, x, y):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            enemies = 0
            for d in directions:
                dx, dy = x + d[0], y + d[1]
                while dx >= 0 and dx < rows and dy >=0 and dy < cols and grid[dx][dy] != "W":
                    if grid[dx][dy] == "E":
                        enemies += 1
                    dx += d[0]
                    dy += d[1]
            return enemies
        
        if not grid:
            return 0
        max_kills = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    kills = bfs(grid, i, j)
                    max_kills = max(max_kills, kills)
        return max_kills
