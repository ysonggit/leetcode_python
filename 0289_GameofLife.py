class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lives = {}
        deads = {}
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    # check neighbors
                    lives[(i,j)] = 0
                    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1)]:
                        x, y = i + dx, j + dy
                        if 0<= x < m and 0<=y < n and board[x][y] == 1:
                            lives[(i,j)] += 1
                else:
                    deads[(i,j)] = 0
                    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1)]:
                        x, y = i + dx, j + dy
                        if 0<= x < m and 0<=y < n and board[x][y] == 1:
                            deads[(i,j)] += 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if 2 <= lives[(i,j)] <=3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if deads[(i,j)] == 3:
                        board[i][j] = 1
