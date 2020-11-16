class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1, n2 = len(word1), len(word2)
        if n1 != n2:
            return False
        if set(word1) != set(word2):
            return False
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt1.values()) == sorted(cnt2.values())
