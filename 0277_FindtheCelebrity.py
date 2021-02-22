class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if not knows(i, candidate):
                candidate = i
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate
