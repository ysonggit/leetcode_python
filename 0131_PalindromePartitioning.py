class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        self.res = []
        def dfs(sol, cur):
            if cur == len(s):
                self.res.append(sol)
                return 
            for i in range(1, len(s)-cur+1):
                path = s[cur:cur+i]
                if path == path[::-1]:
                    dfs(sol + [path], cur+i)

        dfs([], 0)
        return self.res
