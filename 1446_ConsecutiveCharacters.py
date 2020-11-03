class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        i, j = 0, 1
        power = 1
        while j < len(s):
            while j < len(s) and s[j] == s[i]:
                j+=1
            power = max(power, j-i)
            i = j
            j +=1
        return power