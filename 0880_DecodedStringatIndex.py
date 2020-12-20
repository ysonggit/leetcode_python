class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        i = 0
        n = len(S)
        decodeStrLen = 0
        while i < n:
            if not S[i].isdigit():
                if decodeStrLen == K - 1:
                    return S[i]
                decodeStrLen += 1
            else:
                if decodeStrLen * int(S[i]) >= K:
                    return self.decodeAtIndex(S[:i], (K-1)%decodeStrLen+1) #tricky: targetPosition = (K-1) % lengthOf(S)
                decodeStrLen *= int(S[i])
            i += 1
        return ""
