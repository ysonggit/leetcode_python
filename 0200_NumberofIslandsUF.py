class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2D union-find --> 1D array
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(m) for j in range(n))
        uf = [i for i in range(m*n)]
        
        def find(x):
            if uf[x] != x:
                return find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                uf[px] = py
                self.count -= 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    idx = i * n + j
                    if j < n-1 and grid[i][j+1] == '1':
                        union(idx, idx+1) # union when same row but adj cols are 1s
                    if i < m-1 and grid[i+1][j] == '1':
                        union(idx, idx+n) # union when same col but adj rows are 1s
        return self.count
