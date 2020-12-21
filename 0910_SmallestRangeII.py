class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        # Assuming there is a point, on the left of the point, 
        # all elements add K, on the right of the point, all elements substract K, check each possible point. 
        mx, mi = A[-1]-K, A[0]+K
        for i in range(len(A)-1):
            big = max(mx, A[i] + K)
            small = min(mi, A[i+1] - K)
            res = min(res, big - small)
        return res
