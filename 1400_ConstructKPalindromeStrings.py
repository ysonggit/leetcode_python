class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        odds = 0
        for c in freq:
            if freq[c]%2 == 1:
                odds += 1
        return odds <= k
