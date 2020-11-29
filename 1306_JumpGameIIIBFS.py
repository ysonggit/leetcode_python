class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if arr[cur] == 0:
                    return True
                left, right = cur - arr[cur], cur + arr[cur] 
                if 0 <= left < n and left not in visited:
                    queue.append(left)
                    visited.add(left)
                if 0 <= right < n and right not in visited:
                    queue.append(right)
                    visited.add(right)
        return False
