class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        n = len(A)
        cache = defaultdict(int)
        for a in A:
            for b in B:
                cache[a+b] += 1
        for c in C:
            for d in D:
                s = - (c + d)
                res += cache[s]
        return res
