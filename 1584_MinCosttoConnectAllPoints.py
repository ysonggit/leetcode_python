class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 0
        dists = [math.inf] * n
        cur = 0
        visited = set()
        res = 0
        for i in range(n-1):
            xi, yi = points[cur]
            visited.add(cur)
            for j, (xj, yj) in enumerate(points):
                if j in visited: 
                    continue
                dists[j] = min(dists[j], abs(xi-xj) + abs(yi-yj))
            cur = dists.index(min(dists))
            res += dists[cur]
            dists[cur] = math.inf
        return res
