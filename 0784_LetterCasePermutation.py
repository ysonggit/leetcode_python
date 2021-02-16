class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not any(c.isalpha() for c in S):
            return [S]
        def backtrack(s, cur, res):
            if cur == len(s):
                return
            if s[cur].isdigit():
                backtrack(s, cur+1, res)
            else:
                s_high = s[:cur] + s[cur].upper() + s[cur+1:]
                s_low = s[:cur] + s[cur].lower() + s[cur+1:]
                res.add(s_low)
                res.add(s_high)
                backtrack(s_low, cur+1, res) 
                backtrack(s_high, cur+1, res)
        res = set()
        backtrack(S, 0, res)
        return list(res)
