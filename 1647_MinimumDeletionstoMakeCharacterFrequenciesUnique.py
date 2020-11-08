class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [c for c in Counter(s).values()]
        freq.sort(reverse=True)
        cnts_set = set()
        res = 0
        for i in freq:
            while i and i in cnts_set:
                i -= 1   
                res += 1
            else:
                cnts_set.add(i)
        return res
