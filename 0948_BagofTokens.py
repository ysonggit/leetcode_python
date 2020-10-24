class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        n = len(tokens)
        if n == 0:
            return 0
        tokens.sort()
        if tokens[0] > P:
            return 0
        scores = 0
        max_scores = 0
        lo, hi = 0, n-1
        while lo <= hi:
            # still have power
            while P >= tokens[lo]:
                P -= tokens[lo]
                scores += 1
                lo += 1
                max_scores = max(scores, max_scores)
                if lo > hi:
                    break
            # when no power left, check if we can gain more (Greedy: from hi pow to lo pow)
            if scores > 0:
                P += tokens[hi]
                hi -= 1
                scores -= 1
        return max_scores