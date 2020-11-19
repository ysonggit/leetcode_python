class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ""
        cur_num = 0
        stack = []
        for c in s:
            if c == "[":
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ""
                cur_num = 0
            elif c.isalpha():
                cur_str += c
            elif c.isdigit():
                cur_num = cur_num* 10 + int(c)
            else: 
                expand_str = cur_str * stack.pop()
                cur_str = stack.pop() + expand_str 
        return cur_str
