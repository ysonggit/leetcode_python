class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        i, j = 0, len(A)-1
        while i < j:
            if A[i] + A[j] < K:
                S= max(S, A[i] + A[j])
                i += 1
            else:
                j -= 1
        return S
