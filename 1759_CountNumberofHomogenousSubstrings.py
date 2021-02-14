class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        # split s to consecutive substr
        # 2 pointers
        start, i = 0, 0
        m = 10**9+7
        while i<len(s)-1:
            if s[i] != s[i+1]:
                # s[start:i] 
                k = i - start + 1
                for j in range(1, k+1):
                    res += (k+1-j)%m
                start = i+1
                # print(i, res)
            i += 1
        k = len(s) - 1 - start + 1
        for j in range(1, k+1):
            res += (k+1-j)%m
        return res % m
