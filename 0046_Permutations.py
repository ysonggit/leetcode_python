class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        def dfs(nums, sol, res):
            if not nums:
                res.append(sol)
            for i in range(len(nums)):
                # if any duplicates, pass by when nums[i] == nums[i-1]
                dfs(nums[:i]+nums[i+1:], sol+[nums[i]], res)
        dfs(nums, [], res)
        return res
