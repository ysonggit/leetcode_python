class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        if not deliciousness:
            return 0
        freq = defaultdict(int)
        res = 0
        for i in deliciousness:
            for k in range(22): # 2^21 >= 2^20 + 2^20
                res += freq[2**k - i]
            freq[i] += 1
        return res % (10**9 + 7)
