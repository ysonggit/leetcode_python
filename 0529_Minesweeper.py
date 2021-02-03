class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def countMines(x, y):
            mines = 0
            for dx, dy in [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]:
                i, j = x + dx, y + dy
                if 0<= i < len(board) and 0<= j < len(board[0]):
                    if board[i][j]=='M':
                        mines += 1
            return mines
        
        queue = deque([(click[0], click[1])])
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        visited[click[0]][click[1]] = True
        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'M':
                board[x][y]= 'X'
                return board
            # count how many adjacent mines
            mines = countMines(x, y)
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]:
                    nx, ny = x + dx, y + dy
                    if 0<= nx < m and 0<= ny < n and not visited[nx][ny] and board[nx][ny]=='E':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        return board
