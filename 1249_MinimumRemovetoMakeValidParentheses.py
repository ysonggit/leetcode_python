class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left = 0
        while left < len(s):
            c = s[left]
            if c == '(':
                stack.append(left)
            elif c == ')':
                if not stack:
                    s = s[:left] + s[left+1:]
                    left -= 1
                else:
                    stack.pop()
            left += 1
                
        while stack:
            idx = stack.pop()
            s= s[:idx] + s[idx+1:]
        return s
