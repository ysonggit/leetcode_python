class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(arr, cur, visited):
            if cur >= len(arr) or cur < 0 or cur in visited:
                return False
            if arr[cur] == 0:
                return True
            visited.add(cur)
            return dfs(arr, cur+arr[cur], visited) or dfs(arr, cur-arr[cur], visited)
        visited = set()
        return dfs(arr, start, visited)
