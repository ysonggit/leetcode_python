class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if len(stack)== 0:
                stack.append((c,1))
            else:
                top_c, freq = stack[-1]
                if top_c == c:
                    if freq < k-1:
                        stack[-1] = (c, freq+1)
                    else:
                        stack.pop()
                else:
                    stack.append((c, 1))
        res = ""
        for c, i in stack:
            res += "".join([c]* i)
        return res
            