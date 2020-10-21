class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            cur = asteroids[i]
            if not stack or cur > 0 or stack[-1] < 0:
                stack.append(cur)
            elif stack[-1] == abs(cur):
                stack.pop()
                i+= 1
                continue
            elif abs(cur) > abs(stack[-1]):
                stack.pop()
                continue
            i+= 1
        return stack