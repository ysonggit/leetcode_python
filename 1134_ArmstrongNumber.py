class Solution:
    def isArmstrong(self, n: int) -> bool:
        m = n
        k = len(str(n))
        while m > 0:
            d = m%10
            m = (m - d)//10
            n -= d**k
        return n == 0
