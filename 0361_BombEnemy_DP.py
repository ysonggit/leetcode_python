class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_kills = 0
        rowkills = [0 for _ in range(rows)]
        colkills = [0 for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if j == 0 or grid[i][j-1] == 'W':
                    rowkills[i] = 0 # must reset!
                    k = j
                    while k < cols and grid[i][k] != 'W':
                        rowkills[i] += 1 if grid[i][k] == 'E' else 0
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    k = i
                    colkills[j] = 0 # must reset
                    while k < rows and grid[k][j] != 'W':
                        colkills[j] += 1 if grid[k][j] == 'E' else 0
                        k += 1
                
                if grid[i][j] == '0':
                    max_kills = max(rowkills[i] + colkills[j], max_kills)
        return max_kills
