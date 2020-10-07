class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        x_vals = [p[0] for p in points]
        max_x, min_x = max(x_vals), min(x_vals)
        # no dup pts, so create a set
        pts_set = {(p[0], p[1]) for p in points}
        for p in points:
            if (max_x + min_x - p[0], p[1]) not in pts_set:
                return False
        return True