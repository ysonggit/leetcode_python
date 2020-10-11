class Solution:
    def maxDepth(self, s: str) -> int:
        if s =="" or len(s)<2:
            return 0
        stack = []
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
                max_depth = max(max_depth, len(stack)+1)
            else:
                continue
        return max_depth