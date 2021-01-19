class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        self.maxLen = 1
        self.start = 0
        def expandFromCenter(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if self.maxLen < r - l -1 :
                self.start = l+1
                self.maxLen = r - l - 1

        for i in range(len(s)):
            len1 = expandFromCenter(i, i, s)
            len2 = expandFromCenter(i, i+1, s)
        return s[self.start:self.start+self.maxLen]
