class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        def dfs(cur, visited):
            i, j = cur    
            if visited[i][j]:
                return False
            if i == destination[0] and j==destination[1]:
                return True
            visited[i][j] = True
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x, y = i + dx, j + dy
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += dx
                    y += dy
                last_x, last_y = x - dx, y - dy
                if dfs((last_x, last_y), visited):
                    return True
            return False
        
        m, n = len(maze), len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        return dfs(start, visited)
