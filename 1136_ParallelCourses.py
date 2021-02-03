class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indegrees = [0] * (N+1)
        pre = defaultdict(set)
        for x, y in relations:
            pre[x].add(y) # x is pre of y
            indegrees[y] += 1
        noPre = []
        for i in range(1, N+1):
            if indegrees[i] == 0:
                noPre.append((i, 1))
        if not noPre: # cyclic graph 
            return -1
        queue = deque(noPre)
        semester = -1
        taken = 0
        while queue:
            course, curSem = queue.popleft()
            taken += 1
            semester = max(curSem, semester)
            for followcourse in pre[course]:
                indegrees[followcourse] -= 1
                if indegrees[followcourse] == 0:
                    queue.append((followcourse, curSem+1))
        if taken == N:
            return semester
        return -1
