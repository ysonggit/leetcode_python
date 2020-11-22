class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        distincts = 0
        counts = defaultdict(int)
        i = 0
        max_len = 0
        while i < len(s):
            cur = s[i]
            if counts[cur] == 0:
                distincts += 1
            counts[cur] += 1
            while distincts > 2:
                counts[s[start]]-=1
                if counts[s[start]] == 0:
                    distincts -= 1
                start += 1
            max_len = max(max_len, i-start+1)
            i += 1
        return max_len
