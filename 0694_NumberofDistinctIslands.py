class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        def encodeIsland(i, j, path, d):
            m, n = len(grid), len(grid[0])
            if i <0 or j <0 or i == m or j ==n:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            path.append(d)
            encodeIsland(i+1, j, path, 'd')
            encodeIsland(i, j+1, path, 'r')
            encodeIsland(i-1, j, path, 'u')
            encodeIsland(i, j-1, path, 'l')
            path.append("$") # end symbol $
        res = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    encodeIsland(i, j, path, "^") # start symbol ^
                    #print("".join(path))
                    res.add("".join(path))
        return len(res)
