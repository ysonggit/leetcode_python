class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        nex = copy.copy(arr)
        while True:
            for i in range(1, n-1):
                if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
                    nex[i] += 1
                if arr[i-1] < nex[i] and arr[i+1] < nex[i]:
                    nex[i] -= 1
            if self.identical(arr, nex):
                break
            else:
                arr = copy.copy(nex)
        return arr
        
    def identical(self, a: List[int], b: List[int]) -> bool:
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True