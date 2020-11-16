class Solution:
    def longestMountain(self, A: List[int]) -> int:
        peaks = []
        n = len(A)
        max_len = 0
        for i in range(1, n-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                cur_len = 1
                j = i 
                while 0 < j <= i and A[j-1] < A[j]:
                    cur_len += 1
                    j -= 1
                k = i 
                while i <= k < n-1 and A[k+1] < A[k]:
                    cur_len += 1
                    k += 1
                max_len = max(max_len, cur_len)
        return max_len
