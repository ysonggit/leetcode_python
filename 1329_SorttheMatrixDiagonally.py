class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diag = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                diag[i-j].append(mat[i][j])
        
        for k in diag:
            diag[k].sort()
        
        res = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j]  = diag[i-j].pop(0)
                    
        return res
