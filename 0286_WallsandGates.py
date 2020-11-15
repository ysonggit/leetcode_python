class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            x, y = q.popleft()
            dist = rooms[x][y] + 1
            for dx, dy in directions:
                i, j = x+dx, y+dy
                if 0<=i<m and 0<=j<n:
                    if rooms[i][j] == -1:
                        continue
                    if dist < rooms[i][j]:
                        rooms[i][j] = dist
                        q.append((i, j))
