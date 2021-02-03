class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        '''
        Kruskal’s Minimum Spanning Tree Algorithm 
        1.Sort edges to no-descresing order
        2.Pick the smallest edge that does not form a cycle
        3.Repeat until MST is formed and every node is connected.
        '''
        roots = [i for i in range(0, N+1)]
        self.connectedComponents = N
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
                
        connections.sort(key=lambda x: x[2])
        cost = 0
        for x, y, w in connections:
            px, py = find(x), find(y)
            if px != py:
                cost += w
                roots[py] = px
                self.connectedComponents -= 1
        if self.connectedComponents > 1:
            return -1
        return cost
