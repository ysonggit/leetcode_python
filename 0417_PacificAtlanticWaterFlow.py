class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
                
        def dfs(i, j, visited, m, n):
            if i >= m or j >=n or i <0 or j<0:
                return 
            if (i,j) in visited:
                return 
            visited.add((i, j))
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                x, y = i + dx, j + dy
                if 0<= x < m and 0<= y < n and matrix[x][y] >= matrix[i][j]:
                    dfs(x, y, visited, m, n)
                
        m, n = len(matrix), len(matrix[0])
        to_pacific, to_atlantic = set(), set()
        for row in range(m):
            dfs(row, 0, to_pacific, m, n)
            dfs(row, n-1, to_atlantic, m, n)
        
        for col in range(n):
            dfs(0, col, to_pacific, m, n)
            dfs(m-1, col, to_atlantic, m, n)

        return list(to_pacific & to_atlantic)
