class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = '+'
        for c in s+'+':
            if c== ' ':
                continue
            if '0'<= c <='9':
                num = num * 10 + int(c)
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    prod = stack[-1] * num
                    stack[-1] = prod
                elif sign == '/':
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1]//num)
                    else:
                        stack[-1] = stack[-1]//num
                sign = c
                num = 0
        while stack:
            res += stack.pop()
        return res
