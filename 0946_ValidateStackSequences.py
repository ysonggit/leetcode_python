class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for c in pushed:
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            stack.append(c)
        while stack and popped and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
        return len(popped) == 0
