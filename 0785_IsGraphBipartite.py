class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colored = {}
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 'r'
                queue = deque([i])
                while queue:
                    cur = queue.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = 'b' if colored[cur] == 'r' else 'r'
                            queue.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True
