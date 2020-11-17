class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        pri_queue = [(0, start)] # min heap, sort by dist
        visited = {}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while pri_queue:
            dist, cur = heapq.heappop(pri_queue)
            visited[(cur[0], cur[1])] = dist
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return dist
            for dx, dy in directions:
                x, y, d = cur[0] + dx, cur[1] + dy, 0
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += dx
                    y += dy
                    d += 1
                stop = (x - dx, y - dy)
                if stop not in visited or dist + d < visited[stop]:
                    visited[stop] = dist + d
                    heapq.heappush(pri_queue, (dist + d, stop))
        return -1  
