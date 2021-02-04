class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        i_upper = 2 if x == 1 else ceil(math.log(bound, x))
        for i in range(i_upper):
            j_upper = 2 if y == 1 else ceil(math.log(bound, y))
            for j in range(j_upper):
                s = x**i + y**j
                if s <= bound:
                    res.add(s)
        return list(res)
