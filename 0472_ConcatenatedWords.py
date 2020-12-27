class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        cache = {}
        
        @functools.cache 
        def concatenated(w):
            if w in cache:
                return cache[w]
            for i in range(1, len(w)):
                if w[:i] not in words:
                    continue
                suffix = w[i:]
                if suffix in words or concatenated(suffix):
                    cache[w] = True
                    return True
            cache[w] = False
            return False
        
        res = []
        for word in words:
            if concatenated(word):
                res.append(word)
        return res
