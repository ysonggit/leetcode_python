class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak_idx = arr.index(max(arr))
        n = len(arr)
        if peak_idx == 0 or peak_idx == n-1:
            return False
        for i in range(peak_idx, 0, -1):
            if arr[i] <= arr[i-1]:
                return False
        for i in range(peak_idx, n-1):
            if arr[i] <= arr[i+1]:
                return False
        return True
        
