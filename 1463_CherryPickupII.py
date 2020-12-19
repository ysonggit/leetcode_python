class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pos_cherry = {(0, cols-1): grid[0][0] + grid[0][cols-1]}
        # optimized storage: key is robots' cols (rob1_col, rob2_col) for each row
        # val is the max cherries picked by 2 robots 
        for x in range(1, rows):
            new_cherry = {}
            for (y1, y2), val in pos_cherry.items(): 
                robot1 = [i for i in [y1-1, y1, y1+1] if i >=0 and i < cols]
                robot2 = [i for i in [y2-1, y2, y2+1] if i >=0 and i < cols]
                for i in robot1:
                    for j in robot2:
                        new_val = val + grid[x][i] + grid[x][j] * (i != j)
                        if (i, j) not in new_cherry or new_val > new_cherry[(i, j)]:
                            new_cherry[(i,j)] = new_val
            pos_cherry = new_cherry
        return max(pos_cherry.values())
