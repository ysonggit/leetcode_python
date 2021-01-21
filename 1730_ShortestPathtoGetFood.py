class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((0, i, j))
                    visited.add((i,j))
                    break
        while queue:
            #print(queue)
            step, i, j = queue.popleft()
            if grid[i][j] == '#':
                return step
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x, y = i+dx, j+dy
                if 0<= x <m and 0<= y< n and grid[x][y] != 'X' and (x, y) not in visited:
                    visited.add((x,y))
                    queue.append((step+1, x, y))
        return -1
