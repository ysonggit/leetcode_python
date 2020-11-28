class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        local_max_idx = []
        queue = deque()
        for i, cur in enumerate(nums):
            while queue and nums[queue[-1]] <= cur:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                local_max_idx.append(queue[0])
            # [i-k+2, i]
            if queue[0] == i-k+1:
                queue.popleft()
        for i in local_max_idx:
            res.append(nums[i])
        return res
