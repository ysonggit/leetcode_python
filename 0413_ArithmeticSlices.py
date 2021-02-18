class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) <3:
            return 0
        diff = A[1] - A[0]
        p = 0
        q = 1
        res = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff:
                q += 1
            else:
                k = q-p+1
                for j in range(3, k+1):
                    res += k+1 - j
                diff = A[i] - A[i-1]
                p = i-1
                q = i
        k = q-p+1
        for j in range(3, k+1):
            res += k+1 - j
        return res
