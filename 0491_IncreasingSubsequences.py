class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, cur, res):
            if len(path) > 1:
                res.append(path)
            if len(nums) == cur:
                return
            used = set()
            for i in range(cur, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    dfs(path + [nums[i]], i+1, res)
        res = []
        dfs([], 0, res)
        return res
