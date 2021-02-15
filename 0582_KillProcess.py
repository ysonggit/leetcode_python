class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dag = defaultdict(list)
        root = -1
        for i in range(len(pid)):
            if ppid[i] != 0:
                dag[ppid[i]].append(pid[i])
            else:
                root = pid[i]
        
        if kill == root:
            return pid
        # bfs:
        res = []
        queue = deque([kill])
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for nex in dag[cur]:
                queue.append(nex)
        return res
