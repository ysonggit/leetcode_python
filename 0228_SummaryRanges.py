class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        start, end = 0, 0
        res = []
        while end < len(nums):
            while end < len(nums)-1 and nums[end+1] - nums[end] == 1:
                end += 1
            if end != start:
                res.append("{}->{}".format(nums[start], nums[end]))
            else:
                res.append("{}".format(nums[end]))
            end += 1
            start = end
        return res
