class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        root = None
        for k in graph:
            if len(graph[k]) == 1:
                root = k
                break
        res = []
        visited = set()
        def dfs(cur):
            if cur in visited:
                return
            res.append(cur)
            visited.add(cur)
            for nex in graph[cur]:
                if nex not in visited:
                    dfs(nex)  
        dfs(root)
        return res
