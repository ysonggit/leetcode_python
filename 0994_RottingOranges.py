class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        timer = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    i, j = x + dx, y+dy
                    if i >= 0 and j >=0 and i < m and j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        queue.append((i, j))
            if queue:
                timer += 1
        if fresh > 0:
            return -1
        return timer
