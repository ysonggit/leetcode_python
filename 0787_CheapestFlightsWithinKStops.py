class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        @functools.lru_cache(None)
        def minCost(cur, dest, restStops):
            if restStops < 0 and cur != dest:
                return -1
            if cur == dest:
                return 0
            cost = float('inf')
            for nex, nexCost in graph[cur]:
                restCost = minCost(nex, dest, restStops-1)
                if restCost > -1:
                    cost = min(cost, restCost + nexCost)
            return cost if cost != float('inf') else -1
        
        return minCost(src, dst, K)
