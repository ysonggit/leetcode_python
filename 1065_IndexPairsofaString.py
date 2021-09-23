class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
    
    def search(self, word):
        # return true if word in trie
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        trie = Trie()
        minWordLen, maxWordLen = len(text), 0
        for word in words:
            trie.insert(word)
            minWordLen = min(minWordLen, len(word))
            maxWordLen = max(maxWordLen, len(word))
        
        for i in range(len(text)):
            for j in range(minWordLen, maxWordLen+1):
                if i + j <= len(text):
                    cur = text[i:i+j]
                    if trie.search(cur):
                        res.append([i,i+j-1])
        res.sort()
        return res
