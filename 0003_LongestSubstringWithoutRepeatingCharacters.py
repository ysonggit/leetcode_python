class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}
        max_len, start = 0, -1
        for i in range(len(s)):
            c = s[i]
            if c in char_pos and char_pos[c] > start:
                # duplicated char found, reset start
                start = char_pos[c] 
            char_pos[c] = i
            max_len = max(max_len, i - start)
        return max_len
