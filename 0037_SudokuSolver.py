class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) > 0:
            self.dfs(board, 0, 0)
    
    def valid(self, board: List[List[str]], i: int, j: int, k: int) -> bool:
        if any(board[i][c]==k for c in range(9)): 
            return False
        if any(board[r][j]==k for r in range(9)):
            return False
        sub_i, sub_j = 3*(i//3), 3*(j//3)
        if any(board[r][c]==k for r in range(sub_i, sub_i+3) for c in range(sub_j, sub_j+3) ):
            return False
        return True
    
    def dfs(self, board: List[List[str]], i: int, j: int) -> bool:
        if j == 9:
            return self.dfs(board, i+1, 0)
        if i == 9:
            return True
        if board[i][j] != '.':
            return self.dfs(board, i, j+1)
        for k in range(1, 10):
            if self.valid(board, i, j, str(k)):
                board[i][j] = str(k)
                if self.dfs(board, i, j+1):
                    return True
        board[i][j] = '.'
        return False   