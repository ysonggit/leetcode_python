class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = 0
        left = 0
        for i, c in enumerate(S):
            if c == '(':
                left += 1
            else:
                left -= 1
            if i > 0 and S[i-1:i+1] == "()":
                res += 1 << left
        return res
