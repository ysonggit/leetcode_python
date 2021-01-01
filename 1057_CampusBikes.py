class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                distances.append((dist, i, j))
        distances.sort() # MN * O(logMN)
        res = [-1] * len(workers)
        taken = set()
        for dist, i, j in distances:
            if res[i] >= 0 or j in taken:
                continue
            res[i] = j
            taken.add(j)
        return res
