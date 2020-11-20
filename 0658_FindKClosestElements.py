class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k # trick, make sure the mid + k is always in range
        while lo < hi:
            mid = (hi + lo)>>1
            # sliding window A[mid] ~ A[mid + k]
            # check distance between x - A[mid] and A[mid + k] - x
            if x - arr[mid] > arr[mid+k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]
