class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res =[]
        levels = defaultdict(list)
        '''
        level 0: [0,0]
        level 1: [0,1],[1,0]
        level 2: [2,0],[1,1],[0,2]
        '''
        for i in range(m):
            for j in range(n):
                levels[i+j].append(matrix[i][j])
        for l in range(len(levels)):
            if l % 2 == 0:
                res += levels[l][::-1]
            else:
                res += levels[l]
        return res
