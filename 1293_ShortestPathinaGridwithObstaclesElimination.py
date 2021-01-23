class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, 0)]) # row, col, obstacles
        eliminatedObs = [[m*n]*n for _ in range(m)] # eliminatedObs[i][j] = Smallest number of eliminated obstacles
        eliminatedObs[0][0] = 0
        while queue:
            step, i, j, obs = queue.popleft()
            if obs > k:
                continue
            if i == m-1 and j ==n-1:
                return step
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x, y = i+dx, j+dy
                if 0<= x < m and 0<=y <n:
                    nex_obs = obs + 1 if grid[x][y] == 1 else obs
                    if nex_obs < eliminatedObs[x][y]:
                        eliminatedObs[x][y] = nex_obs
                        queue.append((step+1, x, y, nex_obs))
        return -1
