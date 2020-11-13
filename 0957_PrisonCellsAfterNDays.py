class Solution:
    def __init__(self):
        self.cache = {}
    
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cycle_len = 0
        cycle = False
        patterns = set()
        for i in range(N):
            nex = self.cellsNextDay(cells)
            nex_tp = tuple(nex)
            if nex_tp in patterns:
                cycle = True
                break
            patterns.add(nex_tp)
            self.cache[i] = nex
            cells = nex
            cycle_len += 1
        if cycle:
            #print("repeats every {} rounds".format(cycle_len))
            # [1,1,0,1,1,0,1,1] 6 special acyclic case
            if N%cycle_len == 0:
                return cells
            return self.cache[N%cycle_len-1] 
        return cells

    def cellsNextDay(self, cells):
        n = len(cells)
        nex = [0]*n
        for i in range(1, n-1):
            if cells[i-1]==cells[i+1]:
                nex[i] = 1
        return nex