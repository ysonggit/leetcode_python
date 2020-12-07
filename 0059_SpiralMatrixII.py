class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]* n for _ in range(n)]
        r, c, dr, dc = 0, 0, 0, 1
        for i in range(1, n*n+1):
            res[r][c] = i
            if (not 0<= r+dr <n) or (not 0 <= c+dc <n) or res[r+dr][c+dc] != 0:
                dc, dr = -dr, dc # rotate clock-wise 
            r += dr
            c += dc
        return res
