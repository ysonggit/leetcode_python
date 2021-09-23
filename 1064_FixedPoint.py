class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        low, high = 0, len(arr)-1
        smallest = -1
        while low < high:
            mid = (low + high)//2
            if arr[mid] == mid:
                if smallest < 0 or mid < smallest:
                    smallest = mid
                    high = mid
            elif arr[mid] < mid:
                low = mid+1
            else:
                high = mid
        return smallest
