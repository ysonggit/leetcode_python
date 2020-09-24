class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        cnt = 0
        for i in arr:
            if i+1 in s:
                cnt+=1
        return cnt