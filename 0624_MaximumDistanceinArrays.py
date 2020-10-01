class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_dist = 0
        g_min, g_max = 10001, -10001
        for arr in arrays:
            l_min, l_max = arr[0], arr[-1]
            max_dist = max([max_dist, l_max - g_min, g_max - l_min])
            g_min, g_max = min(g_min, l_min), max(g_max, l_max)
        return max_dist