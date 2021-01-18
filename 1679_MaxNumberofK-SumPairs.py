class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        res = 0
        while i < j:
            if nums[i] + nums[j] == k:
                res += 1
                i += 1
                j -= 1
            else:
                if nums[i] + nums[j] < k:
                    i += 1
                else:
                    j -= 1
        return res
