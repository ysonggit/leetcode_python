class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def lengthGoodPalindrome(s, l, r, pre):
            if (l,r,pre) not in memo:
                if l >= r:
                    return 0
                if s[l] == s[r] and s[l] != pre:
                    return 2 + lengthGoodPalindrome(s, l+1, r-1, s[l])
                memo[(l,r, pre)] = max(lengthGoodPalindrome(s, l+1, r, pre), lengthGoodPalindrome(s, l, r-1, pre))
            return memo[(l,r, pre)]
    
        return lengthGoodPalindrome(s, 0, len(s)-1, "")
