class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(0, start)])
        while queue:
            mutations, cur = queue.popleft()
            if cur == end:
                return mutations
            for i in range(len(cur)):
                for c in "ACGT":
                    nex = cur[:i] + c + cur[i+1:]
                    if nex in bank:
                        queue.append((mutations+1, nex))
                        bank.remove(nex)
        return -1
