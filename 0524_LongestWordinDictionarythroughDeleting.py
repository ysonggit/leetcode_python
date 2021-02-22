class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        
        def wordInString(w, s):
            i, j = 0, 0
            while i < len(w) and j < len(s):
                if w[i] == s[j]:
                    i += 1
                j += 1
            return i == len(w) and j <= len(s)
                    
        for w in d:
            if wordInString(w, s):
                return w
        return ""
