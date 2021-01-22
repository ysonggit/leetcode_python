class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False
        for i in range(m):
            if s[i] != t[i]:
                if m == n: # replace only happens when two same length strings
                    return s[i+1:] == t[i+1:]
                else:
                    # ab acb
                    return s[i:] == t[i+1:] # insert
        return False if m == n else True # corner case: s=""
