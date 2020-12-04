class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        m = len(M)
        circles = 0
        visited = set()
        def dfs(cur):
            visited.add(cur)
            for nb in range(len(M)):
                if nb != cur and M[cur][nb] == 1 and nb not in visited:
                    dfs(nb)
                    
        for i in range(m):
            if i not in visited:
                dfs(i)
                circles += 1
        return circles
