class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts, res = defaultdict(int), []
        for c in s:
            counts[c]+= 1
        if len(counts) == len(s):
            return s
        for c in s:
            #print(res)
            #print("cur char: ", c)
            while len(res) > 0 and res[-1] > c and counts[res[-1]] > 0 and c not in res:
                res.pop()
            if c not in res:
                res.append(c)
            #print(res)
            counts[c]-=1
        return "".join(res)