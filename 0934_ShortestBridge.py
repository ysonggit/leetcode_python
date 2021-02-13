class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # [[0,1,0],
        #  [0,0,0],
        #  [0,0,1]]
        # first run dfs change 1s to 2s 
        def dfs(i, j):
            if not (0<= i < len(A) and 0<= j < len(A[0])):
                return
            if A[i][j] in [0, 2]:
                return
            if A[i][j] == 1:
                A[i][j] = 2
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        m, n = len(A), len(A[0])
        found = False
        for i in range(m):
            if not found:
                for j in range(n):
                    if A[i][j] == 1:
                        dfs(i,j)
                        found = True
                        break
                    
        coast1, coast2 = set(), set()
        def findCoast(i, j, border):
            if (i,j) in border:
                return
            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                x, y = i + dx, j + dy
                if 0<= x < len(A) and 0 <= y < len(A[0]) and A[x][y]== 0:
                    border.add((i, j))
                    
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    findCoast(i, j, coast1)
                elif A[i][j] == 2:
                    findCoast(i, j, coast2)
        
        minManhattanDist = float('inf')
        for i, j in coast1:
            for x, y in coast2:
                minManhattanDist = min(minManhattanDist, abs(i-x)+ abs(j-y))
        return minManhattanDist -1 
