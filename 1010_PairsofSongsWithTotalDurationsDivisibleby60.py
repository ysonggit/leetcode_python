class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # variation of two sum problem
        cache = defaultdict(int)
        res = 0
        for t in time:
            res += cache[(60-t%60)%60]
            cache[t%60] += 1

        return res
