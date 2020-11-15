 class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[-1] + arr[0]) *(1 + len(arr)) //2 - sum(arr) 
