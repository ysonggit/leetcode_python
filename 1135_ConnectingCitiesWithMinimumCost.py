class Node:
    def __init__(self, id, edge):
        self.id = id
        self.edge = edge
    def __lt__(self, other):
        return self.edge < other.edge
        
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in connections:
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited = set()
        pq = [Node(1,0)]
        heapq.heapify(pq)
        cost = 0
        while pq:
            node = heapq.heappop(pq)
            if node.id in visited:
                continue
            visited.add(node.id)
            cost+= node.edge
            for nb in graph[node.id]:
                if nb[0] not in visited:
                    heapq.heappush(pq, Node(nb[0], nb[1]))
        if len(visited) < N:
            return -1
        return cost
