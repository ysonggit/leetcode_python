class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1
        alph = "abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        for c in alph:
            if c in s:
                i, j = s.index(c), s[::-1].index(c)
                max_len = max(max_len, (n-j-1)-i-1)
        return max_len