class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def vowelCounts(t):
            return len(list(filter(lambda c: c in "aeiouAEIOU", t)))
        n = len(s)
        return vowelCounts(s[:n//2], ) == vowelCounts(s[n//2:])
