class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n
        for i in range(n-1, -1, -1):
            remain = min(k, 25)
            res[i] = chr(ord(res[i]) + remain)
            k -= remain
        return "".join(res)
