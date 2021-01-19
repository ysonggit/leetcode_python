class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def lengthPalindromeSubseq(s, l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2 + lengthPalindromeSubseq(s, l+1, r-1)
            return max(lengthPalindromeSubseq(s, l+1, r), lengthPalindromeSubseq(s, l, r-1))
        
        return lengthPalindromeSubseq(s, 0, len(s)-1)
