class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:  
        # dijkstra
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
                    
        pq = [(0, k)] # priority queue/heap
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nb, w in graph[node]:
                if nb not in dist:
                    heapq.heappush(pq, (d+w, nb))
        if len(dist) == n:
            return max(dist.values())
        return -1
