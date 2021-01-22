class Cell(object):
    def __init__(self, i: int, j: int, val: int):
        self.val = val
        self.row = i
        self.col = j
        
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        pq = []
        visited = [[False] * n for _ in range(m)]
        for row in range(m):
            pq.append(Cell(row, 0, heightMap[row][0]))
            pq.append(Cell(row, n-1, heightMap[row][n-1]))
            visited[row][0], visited[row][n-1] = True, True
        for col in range(n):
            pq.append(Cell(0, col, heightMap[0][col]))
            pq.append(Cell(m-1, col, heightMap[m-1][col]))
            visited[0][col], visited[m-1][col] = True, True
        water = 0
        heapq.heapify(pq)
        while pq:
            cell = heapq.heappop(pq)
            i, j, h = cell.row, cell.col, cell.val
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    water += max(0, h - heightMap[x][y])
                    # for (x,y), pq keeps the highest boundary of it
                    heapq.heappush(pq, Cell(x, y, max(heightMap[x][y], h)))
                    visited[x][y] = True
        return water
