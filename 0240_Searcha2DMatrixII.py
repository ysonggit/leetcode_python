class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        # search from lower left to upper right
        i, j = m-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            else:
                if matrix[i][j] > target:
                    i-= 1
                else:
                    j+= 1
        return False