class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque([(0,0)])
        # fill the shortest distance from origin into cells
        grid[0][0] = 1
        dist = 0
        while queue:     
            cur_x, cur_y = queue.popleft()
            dist = grid[cur_x][cur_y]
            if cur_x == n-1 and cur_y == n-1:
                return dist
            for dx, dy in [[0,1], [1,0], [1,1], [-1,0],[0,-1],[1,-1],[-1,1],[-1,-1]]:
                x, y = cur_x + dx, cur_y + dy
                if x >= n or y >= n or x < 0 or y < 0:
                    continue
                if grid[x][y] != 0:
                    continue
                grid[x][y] = dist + 1
                queue.append((x, y))
        return -1
