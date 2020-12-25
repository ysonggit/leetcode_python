class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res =[None] * (m * n)
        '''
        If out of bottom border (row >= m) then row = m - 1; col += 2; change walk direction.
        if out of right border (col >= n) then col = n - 1; row += 2; change walk direction.
        if out of top border (row < 0) then row = 0; change walk direction.
        if out of left border (col < 0) then col = 0; change walk direction.
        '''
        r, c = 0, 0
        d = 1
        for i in range(m * n):
            res[i] = matrix[r][c]
            r -= d
            c += d
            if r == m:
                r = m - 1
                c += 2
                d = -d
            elif c == n:
                c = n - 1
                r += 2
                d = -d
            elif r < 0:
                r = 0
                d = -d
            elif c < 0: 
                c = 0
                d = -d
        return res
