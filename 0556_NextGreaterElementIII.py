class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # same logic as next permutation problem
        nums = []
        while n > 0:
            nums.append(n%10)
            n = n//10
        nums.reverse()
        # 1. find the 1st decreasing idx (from right to left)
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        pivot = i - 1
        if pivot < 0:
            return -1
        # 2. find the idx which that next digit is less than pivot 
        j = i
        while j < len(nums) and nums[j] > nums[pivot]:
            j += 1
        # 3. swap pivot with j-1
        nums[pivot], nums[j-1] = nums[j-1], nums[pivot]
        # 4. reverse the digits after pivot
        nums = nums[:pivot+1] + nums[pivot+1:][::-1]
        res = 0
        for i in range(len(nums)):
            res = res * 10 + nums[i]
        if res > 2**31 -1:
            return - 1
        return res
