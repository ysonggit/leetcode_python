class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        cache = defaultdict(int)
        def dfs(i :int, sumsofar :int) -> int:
            if (i, sumsofar) not in cache:
                if i == len(nums):
                    return 1 if sumsofar == S else 0
                cache[(i, sumsofar)] = dfs(i+1, sumsofar+nums[i]) + dfs(i+1, sumsofar-nums[i])
            return cache[(i, sumsofar)]
        return dfs(0, 0)
    