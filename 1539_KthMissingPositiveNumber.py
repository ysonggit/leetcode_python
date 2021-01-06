class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        upper = max(arr)
        s = set(arr)
        for x in range(1, upper+1):
            if x not in s:
                k -= 1
                if k == 0:
                    return x
        return upper + k
