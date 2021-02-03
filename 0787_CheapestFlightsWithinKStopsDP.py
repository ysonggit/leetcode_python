class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        # dp[i][j] represents the minCost of reaching i from src in j stops
        dp = [[float('inf')] * (K+2) for _ in range(n)]
        dp[src][0] = 0
        for j in range(K+1):
            for i in range(n):
                if dp[i][j] != float('inf'):
                    for nex, nexCost in graph[i]:
                        dp[nex][j+1] = min(dp[nex][j+1], nexCost + dp[i][j])
        minCost = min(dp[dst])
        if minCost == float('inf'):
            return -1
        return minCost
