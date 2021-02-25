class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        n = len(nums)
        start, end = -1, n
        for i in range(n):
            if nums[i] != sortedNums[i]:
                if start < 0:
                    start = i
                else:
                    break
        for i in range(n-1, -1, -1):
            if nums[i] != sortedNums[i]:
                if end == n:
                    end = i
                else:
                    break
        if start < 0 or end == n:
            return 0
        return end - start + 1
