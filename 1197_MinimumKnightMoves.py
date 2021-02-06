class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # dp: move from target to origin as fast as possible
        @functools.lru_cache(None)
        def minMoves(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                # if at (1,1) or (0,2), (2,0), need 2 more moves:
                # (1,1) -> (-1,2) -> (0,0)
                # (0,2) -> (2,1) -> (0,0)
                return 2
            return min(minMoves(abs(x-1), abs(y-2)), minMoves(abs(x-2), abs(y-1))) + 1
        return minMoves(abs(x), abs(y))
