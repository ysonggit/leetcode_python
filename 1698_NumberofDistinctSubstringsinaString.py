class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False 
        
class Solution:
    def countDistinct(self, s: str) -> int:
        res = 0
        root = TrieNode()
        for i in range(len(s)):
            cur = root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    cur.children[s[j]] = TrieNode()
                    res += 1
                cur = cur.children[s[j]]
        return res
