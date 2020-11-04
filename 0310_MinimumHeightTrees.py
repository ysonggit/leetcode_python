class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = defaultdict(list)
        for e in edges:
            n1, n2 = e
            graph[n1].append(n2)
            graph[n2].append(n1)
        leaves = deque([])
        for k in graph:
            if len(graph[k]) == 1:
                leaves.append(k)
        res = []
        while leaves:
            res = []
            num = len(leaves) 
            for _ in range(num):
                x = leaves.popleft()
                res.append(x)
                for nb in graph[x]:
                    graph[nb].remove(x)
                    graph[x].remove(nb)
                    if len(graph[nb]) == 1:
                        leaves.append(nb)
        return res
