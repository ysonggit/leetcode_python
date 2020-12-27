class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)
            
        queue = deque([(0, 0)])
        visitedIdx = set()
        visitedNum = set()
        while queue:
            dist, cur = queue.popleft()
            num = arr[cur]
            if cur == n-1:
                return dist
            for nb in [cur-1, cur+1]:
                if 0 <= nb < n and nb not in visitedIdx:
                    visitedIdx.add(nb)
                    queue.append((dist+1, nb))
            if num not in visitedNum:
                for nb in pos[num]:
                    if nb not in visitedIdx:
                        visitedIdx.add(nb)
                        queue.append((dist+1, nb))
            visitedNum.add(num)          
        return 0
