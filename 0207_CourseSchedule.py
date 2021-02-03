class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        indegrees = [0]* numCourses
        for a, b in prerequisites:
            pre[b].append(a) # b is pre of a
            indegrees[a] += 1
        noPre = []
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                noPre.append(course)
        queue = deque(noPre)
        while queue:
            course = queue.popleft()
            for followcourse in pre[course]:
                indegrees[followcourse]-= 1
                if indegrees[followcourse] == 0:
                    queue.append(followcourse)
        courseStillPre = [i for i in indegrees if i > 0]
        return len(courseStillPre) == 0
