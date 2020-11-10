class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor: # corner case
            return image
        queue = deque([(sr, sc)])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows, cols = len(image), len(image[0])
        while queue:
            r, c = queue.popleft()
            image[r][c] = newColor
            for d in directions:
                i, j = r+d[0], c+d[1] 
                if i >=0 and i < rows and j >=0 and j < cols and color == image[i][j]:
                    queue.append((i, j))
        return image
