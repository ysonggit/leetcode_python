class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # construct graph in adjacency list    
        graph = defaultdict(list)
        for edge in connections:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        res = []
        idx = [None] * n # idx 
        low_idx = [None] * n # low-index
        visited = [False] * n
        self.dfs(graph, res, 0, None, idx, low_idx, visited, 0)
        return res
    
    def dfs(self, graph, res, cur, parent, idx, low_idx, visited, timestamp):
            '''
            For each node
                1. iterate neighbours
                2. update lowest idx/rank by comparing current's idx with all neighbors' indices
                3. if any neighbor's lowest idx is greater than current's idx, then this is a critical connetion
                Fact: if in SCC, current's idx is always >= any neighbor's idx
            '''
            if visited[cur]:
                return 
            visited[cur] = True
            idx[cur] = low_idx[cur] = timestamp 
            for nb in graph[cur]:
                if nb == parent:
                    continue          
                self.dfs(graph, res, nb, cur,idx, low_idx, visited, timestamp+1)
                low_idx[cur] = min(low_idx[cur], low_idx[nb])
                # idx[cur] >= low_idx[nb] in a SCC
                if idx[cur] < low_idx[nb]:
                    res.append([cur, nb])