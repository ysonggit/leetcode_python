import numpy as np
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        islands = defaultdict(list)
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, m, n, cnt):
            if not (0<= i < m and 0 <= j < n):
                return
            if grid[i][j] != 1:
                return
            grid[i][j] = cnt
            islands[cnt].append([i,j])
            dfs(i+1, j, m, n, cnt)
            dfs(i-1, j, m, n, cnt)
            dfs(i, j+1, m, n, cnt)
            dfs(i, j-1, m, n, cnt)
        
        def norm(vertices):
            # https://en.wikipedia.org/wiki/Dihedral_group
            # rotations (0, 90, 180, or 270 degrees) 
            r0 = [[1,0],
                  [0,1]]
            r1 = [[0,-1],
                  [1,0]]
            r2 = [[-1,0],
                  [0,-1]]
            r3 = [[0,1],
                  [-1,0]]
            # symmetries (left/right direction or up/down direction)
            s0 = [[1,0],
                  [0,-1]]
            s1 = [[0,1],
                  [1,0]]
            s2 = [[-1,0],
                  [0,1]]
            s3 = [[0,-1],
                  [-1,0]]
            mats = [r0, r1, r2, r3, s0, s1, s2, s3]
            islandShapes = []
            for mat in mats:
                points = []
                for p in vertices:
                    q = np.dot(p, mat).tolist()
                    points.append(q)
                points.sort()
                islandShapes.append(points)
            for shape in islandShapes:
                for i in range(1, len(vertices)):
                    shape[i] = np.subtract(shape[i], shape[0]).tolist()
                shape[0] = [0,0]
            islandShapes.sort()
            #print(islandShapes[0])
            return islandShapes[0]
        
        def encode(vertices):
            s = ""
            for v in vertices:
                s += "({},{})".format(v[0], v[1])
            return s
        
        cnt = 1
        normedShapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    dfs(i, j, m, n, cnt)
                    normed = norm(islands[cnt])
                    normedShapes.add(encode(normed))    
        return len(normedShapes)
