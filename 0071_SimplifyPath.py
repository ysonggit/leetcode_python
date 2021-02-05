class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens = path.split("/")
        for cur in tokens:
            if not cur or cur == '.':
                continue
            if cur == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(cur)
        return '/' + '/'.join(stack)
