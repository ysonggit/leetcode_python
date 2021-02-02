class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # must travel distances: sum(dist_from_nuts_to_tree)
        # find the nut having min dist to squirrel
        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        minDist = float('inf')
        squirrelToNuts = [0] * len(nuts)
        treeToNuts = [0] * len(nuts)
        res = 0
        for i, nut in enumerate(nuts):
            squirrelToNuts[i] = dist(nut, squirrel)
            treeToNuts[i] = dist(nut, tree)
            res += treeToNuts[i] * 2
    
        for i, nut in enumerate(nuts):        
            minDist = min(minDist, res - treeToNuts[i] + squirrelToNuts[i])
        return minDist
