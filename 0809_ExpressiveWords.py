class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # encode S and character_counts pair
        def encodeStretchy(s):
            if not s:
                return [], []
            chars, cnts = [s[0]], [1]
            for i in range(1, len(s)):
                if s[i] == chars[-1]:
                    cnts[-1] += 1
                else:
                    chars.append(s[i])
                    cnts.append(1)
            return chars, cnts
        
        res = 0
        s_chars, s_cnts = encodeStretchy(S)
        for w in words:
            w_chars, w_cnts = encodeStretchy(w)
            if w_chars == s_chars:
                valid = 0
                for k in range(len(w_chars)):
                    if w_cnts[k] == s_cnts[k] or (s_cnts[k] > w_cnts[k] and s_cnts[k] >= 3):
                        valid +=1
                if valid == len(w_chars):
                    res += 1
        return res
