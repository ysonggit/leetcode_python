class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, cur in enumerate(nums):
            if not stack or stack[-1] <= cur:
                stack.append(cur)
            else:
                while stack and stack[-1] > cur and len(stack) - 1 + n - i >= k:
                    stack.pop()
                stack.append(cur)
        return stack[:k]
