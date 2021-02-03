class Solution:
    def divideGrid(self, grid: List[List[int]]) -> List[List[List[int]]]:
        n = len(grid)
        if n == 1:
            return grid
        # 0 topLeft, 1 topRight, 2 bottomLeft, 3 bottomRight
        topLeft = [[0] * (n//2) for _ in range(n//2)]
        bottomLeft = [[0] * (n//2) for _ in range(n//2)]
        topRight = [[0] * (n//2) for _ in range(n//2)]
        bottomRight = [[0] * (n//2) for _ in range(n//2)]
        for i in range(n//2):
            for j in range(n//2):
                topLeft[i][j] = grid[i][j]
        for i in range(n//2):
            for j in range(n//2, n):
                topRight[i][j-n//2] = grid[i][j]
        for i in range(n//2, n):
            for j in range(n//2):
                bottomLeft[i-n//2][j] = grid[i][j]
        for i in range(n//2, n):
            for j in range(n//2, n):
                bottomRight[i-n//2][j-n//2] = grid[i][j]
        return [topLeft, topRight, bottomLeft, bottomRight]
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        n = len(grid)
        zeros, ones = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros+= 1
                else:
                    ones += 1
        if ones == n*n:
            # leaf node
            return Node(1, True)
        elif zeros == n*n:
            return Node(0, True)
        
        root = Node(1, False)
        subgrids = self.divideGrid(grid)
        root.topLeft = self.construct(subgrids[0])
        root.topRight = self.construct(subgrids[1])
        root.bottomLeft = self.construct(subgrids[2])
        root.bottomRight = self.construct(subgrids[3])
        return root
