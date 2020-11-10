class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=ROZHWAmjcNI
        rows, cols = len(matrix), len(matrix[0])
        cnt = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == 1 and i>0 and j>0:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                cnt += matrix[i][j]
        return cnt
