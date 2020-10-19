class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        common = set(A).intersection(set(B))
        res = 20001 # because the max len of A is 20000
        ca, cb = Counter(A), Counter(B)
        for c in common:
            a_rot, b_rot = 0, 0
            for i in range(len(A)):
                if c == A[i] and c != B[i]:
                    a_rot += 1
                if c != A[i] and c == B[i]:
                    b_rot += 1
            #print(a_rot, b_rot)
            if a_rot + cb[c] == len(B):
                res = min(res, a_rot)
            if b_rot + ca[c] == len(A):
                res = min(res, b_rot)
        if res == 20001:
            return -1
        return res