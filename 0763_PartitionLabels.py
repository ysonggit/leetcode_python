class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = {c: i for i, c in enumerate(S)}
        l, r = 0, 0
        res = []
        for i, c in enumerate(S):
            r = max(r, last_idx[c])
            if r == i:
                res.append(r - l + 1)
                l = r+1
        return res