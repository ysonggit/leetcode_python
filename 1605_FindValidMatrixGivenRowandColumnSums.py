class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        i, j = 0, 0
        while i < rows and j < cols:
            res[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
            if rowSum[i] == 0:
                i+= 1
            if colSum[j] == 0:
                j+= 1
        return res
