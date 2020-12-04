class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedSet = set(banned) 
        p = "".join(c.lower() if c.isalnum() else ' ' for c in paragraph)
        tokens = [w for w in p.split() if w not in bannedSet]
        freq = Counter(tokens)
        return freq.most_common(1)[0][0]
