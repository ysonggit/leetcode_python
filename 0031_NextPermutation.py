class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # i - 1 is the 1st decreasing idx
        pivot = i - 1
        if pivot < 0:
            nums.reverse()
            return 
        j = i
        while j < n and nums[j] > nums[pivot]:
            j += 1
        nums[pivot], nums[j-1] = nums[j-1], nums[pivot]
        # reverse from i
        p, q = pivot+1, n-1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1
