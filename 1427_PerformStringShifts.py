class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        queue = deque(s)
        for d, m in shift:
            if d == 0:
                queue.rotate(-m)
            else:
                queue.rotate(m)
        return "".join(queue)