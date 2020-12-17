class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        self.res = n
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                roots[py] = px
                self.res -= 1
                
        for x, y in edges:
            union(x, y)
            
        return self.res
