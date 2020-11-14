class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0
        points = []
        for op in ops:
            if op not in ["C", "D", "+"]: # should NOT use isnumeric() because of - sign
                points.append(int(op))
            elif op =="C":
                if points:
                    points.pop()
            elif op =="D":
                points.append(2 * points[-1])
            elif op == "+":
                if len(points) > 1:
                    points.append(points[-2] + points[-1])
        return sum(points)
