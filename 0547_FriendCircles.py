class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                uf[py] = px
        
        for i, row in enumerate(M):
            for j, cell in enumerate(row):
                if i != j and cell == 1:
                    union(i, j)
                    
        circles = defaultdict(set)
        for i in range(len(M)):
            root = find(i)
            circles[root] |= set([i])
            
        return len(circles)
