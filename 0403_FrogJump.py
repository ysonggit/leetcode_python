class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jumpPos = {}
        for stonePos in stones:
            jumpPos[stonePos] = set()
        jumpPos[stones[0]].add(0)
        for stonePos in stones:
            jumpUnits = copy.deepcopy(jumpPos[stonePos]) # avoid set size changed during iteration error
            for k in jumpUnits:
                for step in range(max(0,k-1), k+2): # as frog can only jumps forward
                    if stonePos + step in jumpPos:  # make sure the jump step would let frog fall into water
                        jumpPos[stonePos + step].add(step)
        return len(jumpPos[stones[-1]]) > 0
