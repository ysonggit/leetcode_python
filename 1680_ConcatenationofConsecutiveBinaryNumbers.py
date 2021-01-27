class Solution:
    def concatenatedBinary(self, n: int) -> int:
        length = 0
        res = 0
        for i in range(1, n+1):
            if i & (i-1) == 0:
                # even number, binary length increases by 1, so shift left by (curlength + 1) bits           
                length += 1
            res = ((res<<length) | i )% (10**9+7)
        return res
